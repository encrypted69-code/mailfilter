    @echo off
echo ================================================
echo  VPS Deployment - Indo Mail Bot
echo ================================================
echo.
echo VPS Details:
echo IP: 159.195.84.250
echo Username: root
echo Password: fwL7SSAu0BMLuna
echo.
echo ================================================
echo Step 1: Uploading files to VPS...
echo ================================================
echo.
echo When prompted:
echo 1. Type "yes" and press Enter (for fingerprint)
echo 2. Enter password: fwL7SSAu0BMLuna
echo.
pause

scp -r "%~dp0." root@159.195.84.250:/root/indo_mail/

echo.
echo ================================================
echo Step 2: Connecting to VPS to setup...
echo ================================================
echo.
echo After connecting, run these commands:
echo.
echo   cd /root/indo_mail
echo   chmod +x vps_setup.sh
echo   ./vps_setup.sh
echo.
echo Password: fwL7SSAu0BMLuna
echo.
pause

ssh root@159.195.84.250

echo.
echo ================================================
echo Deployment Complete!
echo ================================================
pause
