@echo off
set /p com= "Commit Text : " 
git.exe checkout main
git.exe pull https://github.com/MysteriB/KKK-Vizsga-Feladat.git
git.exe add -A
git.exe commit -m "%com%"
git.exe push --set-upstream origin main
echo Done
pause
exit