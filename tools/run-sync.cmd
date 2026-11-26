@echo off
REM Garden US - manual/weekly YouTube Analytics sync (Phase 3). PORTABLE: tu suy duong dan tu vi tri file.
set PYTHONIOENCODING=utf-8
set HERE=%~dp0
cd /d "%HERE%.."
echo. >> "%HERE%sync.log"
echo [%date% %time%] === sync run === >> "%HERE%sync.log"
python "%HERE%yt_analytics.py" sync >> "%HERE%sync.log" 2>&1
powershell -NoProfile -ExecutionPolicy Bypass -File "%HERE%notify-ctr.ps1"
