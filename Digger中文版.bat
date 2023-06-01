@echo off
start "wumin" "C:\Windows\System32\cmd.exe"
start "Digger" python main_tw.py
taskkill /f /im cmd.exe
exit