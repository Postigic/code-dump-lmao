@echo off
echo Updating yt-dlp and youtube-transcript-api packages...
python -m pip install --upgrade yt-dlp youtube-transcript-api
if %ERRORLEVEL% EQU 0 (
    echo Update successful!
) else (
    echo Update failed. Please check your internet connection and Python setup.
)
pause
