# Garden US - toast nhac nhap CTR sau weekly sync (Phase 3)
# ASCII-only de PowerShell 5.1 (cp1252, no-BOM) parse dung.
# PORTABLE: tu suy workspace tu $PSScriptRoot, doc slug tu channel.config.json -> dung cho moi kenh.
param([string]$Week = "")
$root = Split-Path $PSScriptRoot -Parent
$chan = "Channel"
try {
    $cfg = Get-Content (Join-Path $root "channel.config.json") -Raw | ConvertFrom-Json
    $chan = $cfg.channel_name
    if (-not $Week) {
        $slug = $cfg.youtube_channel_slug
        $statsPath = Join-Path $root ("references\channel-stats-{0}.json" -f $slug)
        $end = (Get-Content $statsPath -Raw | ConvertFrom-Json).date_range.end
        $d = [datetime]$end
        $wk = Get-Date $d -UFormat %V    # ISO 8601 week number
        $Week = "{0}-W{1}" -f $d.Year, $wk
    }
} catch {
    if (-not $Week) { $Week = "tuan nay" }
}
try {
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $n = New-Object System.Windows.Forms.NotifyIcon
    $n.Icon = [System.Drawing.SystemIcons]::Information
    $n.BalloonTipTitle = "$chan - CTR Reminder ($Week)"
    $n.BalloonTipText = "Sync done. CTR khong co qua API. Nhap tay: YouTube Studio / Analytics / Reach / CTR (28d). Dien manual_ctr_pct trong channel-stats JSON roi chay: yt_analytics.py update-truth."
    $n.Visible = $true
    $n.ShowBalloonTip(20000)
    Start-Sleep -Seconds 7
    $n.Dispose()
} catch {
    # Khong hien duoc (session khong tuong tac) -> reminder van nam trong channel-truth.md + sync.log
}
