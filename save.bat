@echo off
set /p com= "Commit Text : " 
git.exe pull
git.exe add -A
git.exe commit -m "%com%"
git.exe push dev
echo Done
pause
exit