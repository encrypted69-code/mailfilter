# Telegram Client API Configuration (Your Account)
API_ID = "35535597"  # Get from https://my.telegram.org
API_HASH = "522434793d76cdf5258d203ffd19fc69"  # Get from https://my.telegram.org
PHONE_NUMBER = "+13464747619"  # Your phone number with country code (e.g., +1234567890)

# Notification Settings
NOTIFICATION_CHAT_ID = "-1003734324643"  # Group/channel ID where to send notifications

# Mail Bot Monitoring
MAIL_BOT_USERNAME = "@fakemailbot"  # Username of the bot that sends you emails

# Test Bot (for testing - you can send messages to this bot to test filtering)
TEST_BOT_USERNAME = "@userinfobot"  # Any bot you want to use for testing

# Monitor both bots
MONITORED_BOTS = [MAIL_BOT_USERNAME, TEST_BOT_USERNAME, "@testiggnnngigbot", "@IndoIgMail_bot"]

# Filter Settings
FILTER_KEYWORD = "Instagram Ads Team"  # Filter messages containing this keyword
