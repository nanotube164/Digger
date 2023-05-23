@echo off
start "wumin" "C:\Windows\System32\cmd.exe"
start "PI Catcher" python main.py
taskkill /f /im cmd.exe
exit