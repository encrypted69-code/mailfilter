# Deploy to VPS Script
# This will SSH in and pull/setup everything

$password = "fwL7SSAu0BMLuna"
$commands = @"
cd /root
mkdir -p indo_mail
cd indo_mail

# Create config.py
cat > config.py << 'CONFIGEOF'
# Telegram Client API Configuration (Your Account)
API_ID = "35535597"
API_HASH = "522434793d76cdf5258d203ffd19fc69"
PHONE_NUMBER = "+13464747619"

# Notification Settings
NOTIFICATION_CHAT_ID = "-1003734324643"

# Mail Bot Monitoring
MAIL_BOT_USERNAME = "@fakemailbot"
TEST_BOT_USERNAME = "@userinfobot"

# Monitor all bots
MONITORED_BOTS = [MAIL_BOT_USERNAME, TEST_BOT_USERNAME, "@testiggnnngigbot"]

# Filter Settings
FILTER_KEYWORD = "Instagram Ads Team"
CONFIGEOF

# Create requirements.txt
cat > requirements.txt << 'REQEOF'
telethon
REQEOF

# Download mail_bot.py from the terminal session
# (We'll paste the code)

echo "Files created. Ready for bot code..."
"@

Write-Host $commands
Write-Host "`n`n=== Copy the above commands and run them after connecting ===" 
Write-Host "`nConnecting to VPS..."
Write-Host "Password: $password`n"

ssh root@159.195.84.250
