@echo off
cd /d %~dp0
pip install -r requirements.txt
del requirements.txt
pause
