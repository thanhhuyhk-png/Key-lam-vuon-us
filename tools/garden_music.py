"""Nhạc nền acoustic ấm tự tạo bằng code (không dính bản quyền), trộn vào đầu video đã dựng. Không đụng phần hình.

Usage:
    python tools/garden_music.py make scripts/<video>/build/music.wav [--seed 93] [--dur 62]
    python tools/garden_music.py mix scripts/<video>/build/final.mp4 scripts/<video>/build/music.wav

make: đàn gảy (Karplus-Strong) rải hợp âm G-D-Em-C trên nền pad nhẹ, 72 bpm, có vang phòng.
mix:  ra <video>-music.mp4 cạnh file gốc; nhạc chuẩn -14 LUFS rồi hạ theo --vol (mặc định 0.09), chỉ chạy 0:00–1:00 và mờ dần 4 giây cuối.
"""
import argparse
import pathlib
import subprocess
import sys

import numpy as np
from scipy.io import wavfile
from scipy.signal import fftconvolve, lfilter

SR = 44100
BPM = 72
# Mỗi hợp âm: nốt trầm + 3 nốt rải (MIDI).
CHORDS = [(43, [59, 62, 67]), (38, [57, 62, 66]), (40, [59, 64, 67]), (36, [60, 64, 67])]
PATTERN = [0, 1, 2, 3, 2, 1, 2, 3]  # 0 = nốt trầm, 1–3 = nốt rải; mỗi ô là một móc đơn


def hz(m):
    return 440 * 2 ** ((m - 69) / 12)


def pluck(rng, midi, dur, level):
    n = int(dur * SR)
    p = max(2, int(SR / hz(midi)))
    # Xung nhiễu qua lọc thấp cho tiếng dây nylon, vòng trễ tự tắt dần.
    burst = lfilter([0.5], [1, -0.5], rng.uniform(-1, 1, p))
    y = np.zeros(n)
    y[:p] = burst
    decay = 0.996 if midi < 50 else 0.992
    for i in range(p, n):
        y[i] = decay * 0.5 * (y[i - p] + y[i - p - 1])
    return y * level


def pad(midi_notes, dur):
    t = np.arange(int(dur * SR)) / SR
    y = sum(np.sin(2 * np.pi * hz(m) * t + i) + 0.3 * np.sin(2 * np.pi * hz(m) * 2.001 * t) for i, m in enumerate(midi_notes))
    env = np.minimum(1, np.minimum(t / 1.2, (dur - t) / 1.2))
    return y * env * 0.02


def add(buf, y, at, pan=0.0):
    i = int(at * SR)
    y = y[: max(0, len(buf) - i)]
    buf[i:i + len(y), 0] += y * (1 - pan) / 2 * 2 ** 0.5
    buf[i:i + len(y), 1] += y * (1 + pan) / 2 * 2 ** 0.5


def make(out, seed, dur):
    rng = np.random.default_rng(seed)
    eighth = 60 / BPM / 2
    bar = eighth * 8
    buf = np.zeros((int((dur + 3) * SR), 2))
    t, k = 0.0, 0
    while t < dur:
        bass, top = CHORDS[k % len(CHORDS)]
        add(buf, pad([bass + 12, *top], bar + 1.0), t)
        for j, step in enumerate(PATTERN):
            # Lệch nhịp và lực tay ngẫu nhiên chút ít cho khỏi giống máy.
            at = t + j * eighth + rng.normal(0, 0.008)
            vel = rng.uniform(0.75, 1.0)
            if step == 0:
                add(buf, pluck(rng, bass, 3.0, 0.5 * vel), max(0, at))
            else:
                add(buf, pluck(rng, top[step - 1], 2.2, 0.32 * vel), max(0, at), pan=(step - 2) * 0.35)
        t += bar
        k += 1
    n = int(1.8 * SR)
    ir = rng.normal(0, 1, n) * np.exp(-np.arange(n) / (0.35 * SR))
    wet = np.stack([fftconvolve(buf[:, c], ir, mode="full")[: len(buf)] for c in range(2)], axis=1)
    y = buf + wet / np.abs(wet).max() * np.abs(buf).max() * 0.25
    y = y[: int(dur * SR)]
    y = y / np.abs(y).max() * 0.85
    wavfile.write(out, SR, (y * 32767).astype(np.int16))
    print(f"{out} ({dur:.0f}s)")


def mix(video, music, vol, end, fade):
    v = pathlib.Path(video)
    out = v.with_name(v.stem + "-music.mp4")
    fc = (f"[1:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,atrim=0:{end},afade=t=out:st={end - fade}:d={fade},volume={vol}[m];"
          f"[0:a][m]amix=inputs=2:duration=first:normalize=0[a]")
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(v), "-i", str(music), "-filter_complex", fc, "-map", "0:v", "-map", "[a]",
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)],
                       capture_output=True, text=True, encoding="utf-8", errors="ignore")
    if r.returncode:
        sys.exit("ffmpeg lỗi: " + r.stderr[-600:])
    print(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["make", "mix"])
    ap.add_argument("a")
    ap.add_argument("b", nargs="?")
    ap.add_argument("--seed", type=int, default=93)
    ap.add_argument("--dur", type=float, default=62.0)
    ap.add_argument("--vol", type=float, default=0.09)
    ap.add_argument("--end", type=float, default=60.0)
    ap.add_argument("--fade", type=float, default=4.0)
    x = ap.parse_args()
    if x.cmd == "make":
        make(x.a, x.seed, x.dur)
    else:
        mix(x.a, x.b, x.vol, x.end, x.fade)
