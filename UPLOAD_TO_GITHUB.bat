@echo off
echo ================================================
echo  Upload to GitHub - Mail Filter Bot
echo ================================================
echo.
echo Repository: https://github.com/encrypted69-code/mailfilter
echo.
echo NOTE: Your sensitive files (config.py, vps_credentials.txt, *.session)
echo       will NOT be uploaded due to .gitignore protection.
echo.
pause

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    echo Or run: winget install --id Git.Git -e --source winget
    echo.
    pause
    exit /b 1
)

echo.
echo ================================================
echo Step 1: Initializing Git Repository
echo ================================================
git init

echo.
echo ================================================
echo Step 2: Adding Files
echo ================================================
git add .

echo.
echo ================================================
echo Step 3: Committing Changes
echo ================================================
git commit -m "Initial commit - Instagram Mail Filter Bot"

echo.
echo ================================================
echo Step 4: Adding Remote Repository
echo ================================================
git remote remove origin 2>nul
git remote add origin https://github.com/encrypted69-code/mailfilter.git

echo.
echo ================================================
echo Step 5: Pushing to GitHub
echo ================================================
echo.
echo You may need to authenticate with GitHub.
echo Use your GitHub Personal Access Token as password.
echo Generate one at: https://github.com/settings/tokens
echo.
git branch -M main
git push -u origin main

echo.
echo ================================================
echo Upload Complete!
echo ================================================
echo.
echo View your repository at:
echo https://github.com/encrypted69-code/mailfilter
echo.
pause
