# Instagram Mail Filter Bot 🤖

A powerful Telegram bot that monitors your mail bot messages for Instagram & Meta emails and sends beautifully formatted notifications to your Telegram group.

## ✨ Features

- 📱 **Automated Monitoring**: Watches your Telegram mail bot 24/7
- 🔍 **Smart Detection**: Automatically identifies Instagram & Meta emails
- 📧 **OTP/Verification**: Extracts email, username, and OTP codes
- 🔐 **New Login Alerts**: Detects logins from new devices
- ⚠️ **Ad Account Status**: Monitors ad account restrictions/reinstatements
- 💰 **Payment Alerts**: Notifies when payments fail
- 💳 **Billing Receipts**: Extracts card info, amounts, and account IDs
- 📨 **Formatted Notifications**: Sends clean, organized alerts to your group
- 🚀 **VPS Ready**: Includes deployment scripts for 24/7 operation

## 📋 Requirements

- Python 3.8+
- Telegram Account
- Telegram API credentials (from https://my.telegram.org)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Telegram API Credentials

1. Go to https://my.telegram.org
2. Log in with your phone number
3. Click on "API Development Tools"
4. Create a new application
5. Copy your `API_ID` and `API_HASH`

### 3. Configure the Bot

Edit `config.py` and add your credentials:

**Telegram API Settings:**
- `API_ID`: Your API ID from my.telegram.org
- `API_HASH`: Your API hash from my.telegram.org
- `PHONE_NUMBER`: Your phone number with country code (e.g., `+1234567890`)

**Monitoring Settings:**
- `NOTIFICATION_CHAT_ID`: Your group/channel ID where notifications will be sent
- `MAIL_BOT_USERNAME`: Username of the bot that sends you emails (e.g., `@your_mail_bot`)

### 4. Get Chat IDs

**For your notification group:**
1. Add @RawDataBot to your group
2. It will show you the chat ID (use the negative number for groups)

**For the mail bot:**
- If you know the bot's username: `@botusername`
- Or use the bot's numeric ID

## Running the Bot

```bash
python mail_bot.py
```

**First time login:**
- You'll be prompted to enter the verification code sent to your Telegram app
- After successful login, a session file `mail_monitor_session.session` will be created
- Next time you run the bot, it will use this session (no login required)

The bot will monitor messages from your mail bot in real-time and send notifications when Instagram ads receipts are detected.

## Notification Formats

The bot automatically detects different types of Instagram/Meta emails and sends formatted notifications:

### 1. OTP/Verification Code
When Instagram sends a verification code:
```
📧 Instagram OTP

Mail: gsorxdk@hi2.in
Username: moose.8404027
OTP: `151187`
```

### 2. New Device Login
When someone logs in from a new device:
```
🔐 Login into new device

Mail: gsorxdk@hi2.in
```

### 3. Ad Account Restricted
When ad account is restricted or reinstated:
```
⚠️ Ad account restricted

Mail: gsorxdk@hi2.in
```

### 4. Payment Failed
When a payment fails:
```
💳 Payment Failed

Mail: hqgrnybg@hi2.in
Message: Payment failed
```

### 5. Card Charged (Ads Receipt)
When Instagram ads charge your card:
```
💳 Card Charged

Card: Visa ···· 3236
Amount: $2.00
```

## Customization

- `FILTER_KEYWORD`: Modify keywords to filter different types of messages
- Add more extraction patterns in `extract_card_info()` and `extract_amount()` methods

## Troubleshooting

**Login Error:**
- Verify your API_ID and API_HASH are correct
- Make sure phone number includes country code (e.g., +1234567890)
- Check if you're entering the correct verification code

**Not Receiving Messages:**
- Verify `MAIL_BOT_USERNAME` is correct (include @)
- Make sure your mail bot is actually sending messages
- Check logs for any errors

**Bot Not Sending Notifications:**
- Verify `NOTIFICATION_CHAT_ID` is correct
- For groups, use negative number (e.g., -1001234567890)
- Make sure your account have permission to send messages to that chat

## Security Notes

⚠️ **Never commit `config.py` or session files to version control!**

The session file contains your login credentials. Keep it safe!

Add to `.gitignore`:
```
config.py
*.session
*.pyc
__pycache__/
```

## License

MIT
