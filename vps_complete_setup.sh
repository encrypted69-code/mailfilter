#!/bin/bash
# Complete VPS Setup Script - Run this on your VPS

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================"
echo "  Instagram Mail Filter Bot - VPS Setup"
echo "========================================"
echo ""

# Create project directory
echo -e "${YELLOW}Creating project directory...${NC}"
mkdir -p /root/indo_mail
cd /root/indo_mail

# Download files from GitHub
echo -e "${YELLOW}Downloading files from GitHub...${NC}"
curl -sL https://raw.githubusercontent.com/encrypted69-code/mailfilter/main/mail_bot.py -o mail_bot.py
curl -sL https://raw.githubusercontent.com/encrypted69-code/mailfilter/main/requirements.txt -o requirements.txt

# Create config.py
echo -e "${YELLOW}Creating config.py...${NC}"
cat > config.py << 'EOF'
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
MONITORED_BOTS = [MAIL_BOT_USERNAME, TEST_BOT_USERNAME, "@testiggnnngigbot", "@IndoIgMail_bot", "@cskmailbot"]

# Filter Settings
FILTER_KEYWORD = "Instagram Ads Team"
EOF

echo -e "${GREEN}✓ Files downloaded${NC}"

# Install system packages
echo -e "${YELLOW}Installing system packages...${NC}"
apt update -qq
apt install -y python3 python3-pip python3-venv screen curl wget -qq
echo -e "${GREEN}✓ System packages installed${NC}"

# Create virtual environment
echo -e "${YELLOW}Creating virtual environment...${NC}"
python3 -m venv .venv
source .venv/bin/activate
echo -e "${GREEN}✓ Virtual environment created${NC}"

# Install Python packages
echo -e "${YELLOW}Installing Python packages...${NC}"
pip install -q --upgrade pip
pip install -q telethon
echo -e "${GREEN}✓ Python packages installed${NC}"

# Create systemd service
echo -e "${YELLOW}Creating systemd service...${NC}"
cat > /etc/systemd/system/mailbot.service << 'SVCEOF'
[Unit]
Description=Instagram Mail Filter Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/indo_mail
Environment=PATH=/root/indo_mail/.venv/bin
ExecStart=/root/indo_mail/.venv/bin/python mail_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
SVCEOF

systemctl daemon-reload
systemctl enable mailbot.service
echo -e "${GREEN}✓ Service configured${NC}"

echo ""
echo "========================================"
echo "  Setup Complete!"
echo "========================================"
echo ""
echo -e "${YELLOW}IMPORTANT: First-time Telegram login required${NC}"
echo ""
echo "The bot will now start and ask for your Telegram verification code."
echo "After successful login:"
echo "  1. Press Ctrl+C to stop the bot"
echo "  2. Run: systemctl start mailbot"
echo "  3. Your bot will run 24/7 automatically"
echo ""
echo "Useful commands:"
echo "  • Check status: systemctl status mailbot"
echo "  • View logs: journalctl -u mailbot -f"
echo "  • Restart: systemctl restart mailbot"
echo "  • Stop: systemctl stop mailbot"
echo ""
echo "========================================"
echo "Starting bot for first-time login..."
echo "========================================"
echo ""

# Start bot for first-time authentication
source .venv/bin/activate
python mail_bot.py
