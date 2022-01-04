@echo off
set /p com= "Commit Text : " 
git.exe checkout main
git.exe pull
git.exe add -A
git.exe commit -m "%com%"
git.exe push
echo Done
pause
exit