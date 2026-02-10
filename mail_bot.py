import re
import logging
from telethon import TelegramClient, events
from telethon.tl.types import User, Channel
from config import *

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MailFilterBot:
    def __init__(self):
        self.client = TelegramClient('mail_monitor_session', API_ID, API_HASH)
        self.notification_chat = None
        
    def extract_email(self, text):
        """Extract email address from message"""
        patterns = [
            r'To:\s*<?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>?',
            r'sent to\s+<?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>?',
            r'for\s+<?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>?',
            r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'  # General email pattern
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1)
        return None
    
    def extract_username(self, text):
        """Extract Instagram username from message"""
        patterns = [
            r'Hi\s+([a-zA-Z0-9._]+),',
            r'intended for\s+([a-zA-Z0-9._]+)',
            r'username=([a-zA-Z0-9._]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(1)
        return None
    
    def extract_otp(self, text):
        """Extract OTP/verification code from message"""
        pattern = r'(?:code|OTP).*?(\d{6})'
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1)
        return None
    
    def extract_card_info(self, text):
        """Extract card last 4 digits from message text"""
        # Pattern: Visa ···· 3236 or Mastercard ···· 1234, etc.
        pattern = r'(Visa|Mastercard|Master Card|American Express|Amex|Discover)[\s·]+[\·\s]*(\d{4})'
        match = re.search(pattern, text, re.IGNORECASE)
        
        if match:
            card_type = match.group(1)
            last_digits = match.group(2)
            return f"{card_type} ···· {last_digits}"
        return None
    
    def extract_amount(self, text):
        """Extract billing amount from message text"""
        # Pattern: Amount billed: $2.00 USD
        patterns = [
            r'Amount billed:\s*\$?([\d,]+\.?\d*)\s*USD',
            r'TOTAL:\s*\$?([\d,]+\.?\d*)\s*USD',
            r'Amount:\s*\$?([\d,]+\.?\d*)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                amount = match.group(1)
                return f"${amount}"
        return None
    
    def extract_account_id(self, text):
        """Extract Instagram Account ID from message"""
        pattern = r'Account ID:\s*(\d+)'
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        return None
    
    def get_email_type(self, text):
        """Determine the type of email"""
        text_lower = text.lower()
        
        # Check for OTP/Verification
        if "verify your account" in text_lower or "verification code" in text_lower or "confirm your identity" in text_lower:
            return "otp"
        
        # Check for new login
        if "new login" in text_lower and ("device you don't usually use" in text_lower or "noticed a login" in text_lower):
            return "new_login"
        
        # Check for ad account restricted/reinstated
        if "advertising access was reinstated" in text_lower or "ad account's advertising access" in text_lower:
            return "ad_restricted"
        
        # Check for payment failed
        if "payment failed" in text_lower or "last payment failed" in text_lower or "pay now" in text_lower:
            return "payment_failed"
        
        # Check for Instagram ads receipt
        if "instagram ads receipt" in text_lower or ("payment summary" in text_lower and "instagram ads team" in text_lower):
            return "ads_receipt"
        
        return None
    
    async def send_otp_notification(self, email, username, otp):
        """Send OTP notification to Telegram group"""
        message = f"📧 Instagram OTP\n\n"
        message += f"Mail: {email}\n"
        message += f"Username: {username}\n"
        message += f"OTP: `{otp}`"
        
        try:
            await self.client.send_message(self.notification_chat, message)
            logger.info(f"OTP notification sent for {username}")
        except Exception as e:
            logger.error(f"Failed to send OTP notification: {e}")
    
    async def send_new_login_notification(self, email):
        """Send new login notification"""
        message = f"🔐 Login into new device\n\n"
        message += f"Mail: {email}"
        
        try:
            await self.client.send_message(self.notification_chat, message)
            logger.info(f"New login notification sent for {email}")
        except Exception as e:
            logger.error(f"Failed to send new login notification: {e}")
    
    async def send_ad_restricted_notification(self, email):
        """Send ad account restricted notification"""
        message = f"⚠️ Ad account restricted\n\n"
        message += f"Mail: {email}"
        
        try:
            await self.client.send_message(self.notification_chat, message)
            logger.info(f"Ad restricted notification sent for {email}")
        except Exception as e:
            logger.error(f"Failed to send ad restricted notification: {e}")
    
    async def send_payment_failed_notification(self, email):
        """Send payment failed notification"""
        message = f"💳 Payment Failed\n\n"
        message += f"Mail: {email}\n"
        message += f"Message: Payment failed"
        
        try:
            await self.client.send_message(self.notification_chat, message)
            logger.info(f"Payment failed notification sent for {email}")
        except Exception as e:
            logger.error(f"Failed to send payment failed notification: {e}")
    
    async def send_card_charged_notification(self, card_info, amount, email, account_id):
        """Send card charged notification to Telegram group"""
        message = f"💳 Card Charged\n\n"
        message += f"Card: {card_info}\n"
        message += f"Amount: {amount}\n"
        message += f"Mail: {email}\n"
        message += f"Instagram ad id: {account_id}"
        
        try:
            await self.client.send_message(self.notification_chat, message)
            logger.info(f"Card charged notification sent: {amount} charged to {card_info}")
        except Exception as e:
            logger.error(f"Failed to send card charged notification: {e}")

    
    def is_instagram_or_meta_email(self, text):
        """Check if message is from Instagram or Meta"""
        keywords = [
            "Instagram",
            "instagram.com",
            "security@mail.instagram.com",
            "business-noreply@mail.instagram.com",
            "advertise-noreply@support.facebook.com",
            "noreply@business.facebook.com",
            "Meta for Business",
            "Meta Platforms",
            "Account ID:",
        ]
        
        text_lower = text.lower()
        return any(keyword.lower() in text_lower for keyword in keywords)
    
    async def setup(self):
        """Setup the Telegram client and handlers"""
        # Start the client
        await self.client.start(phone=PHONE_NUMBER)
        logger.info("Logged in to Telegram")
        
        # Get notification chat
        try:
            # Try to get the entity, if it fails, get dialogs first to cache entities
            try:
                self.notification_chat = await self.client.get_entity(int(NOTIFICATION_CHAT_ID))
            except ValueError:
                # Load dialogs to cache entities
                logger.info("Loading dialogs to cache entities...")
                await self.client.get_dialogs()
                self.notification_chat = await self.client.get_entity(int(NOTIFICATION_CHAT_ID))
            
            logger.info(f"Notification chat set: {NOTIFICATION_CHAT_ID}")
        except Exception as e:
            logger.error(f"Failed to get notification chat: {e}")
            return False
        
        # Get mail bot entities
        mail_bots = []
        try:
            for bot_username in MONITORED_BOTS:
                bot_entity = await self.client.get_entity(bot_username)
                mail_bots.append(bot_entity)
                logger.info(f"Monitoring: {bot_username}")
        except Exception as e:
            logger.error(f"Failed to get bot entities: {e}")
            return False
        
        # Register message handler for all monitored bots
        @self.client.on(events.NewMessage(chats=mail_bots))
        async def handle_new_message(event):
            message_text = event.message.text or event.message.message
            
            if not message_text:
                return
            
            # Check if it's an Instagram/Meta email
            if not self.is_instagram_or_meta_email(message_text):
                logger.info(f"Message received but not Instagram/Meta email")
                return
            
            logger.info("Received Instagram/Meta email")
            
            # Determine email type
            email_type = self.get_email_type(message_text)
            
            if not email_type:
                logger.warning("Could not determine email type")
                return
            
            logger.info(f"Email type: {email_type}")
            
            # Process based on email type
            if email_type == "otp":
                email_addr = self.extract_email(message_text)
                username = self.extract_username(message_text)
                otp = self.extract_otp(message_text)
                
                if email_addr and username and otp:
                    await self.send_otp_notification(email_addr, username, otp)
                else:
                    logger.warning(f"Could not extract OTP info: email={email_addr}, username={username}, otp={otp}")
            
            elif email_type == "new_login":
                email_addr = self.extract_email(message_text)
                if email_addr:
                    await self.send_new_login_notification(email_addr)
                else:
                    logger.warning("Could not extract email for new login")
            
            elif email_type == "ad_restricted":
                email_addr = self.extract_email(message_text)
                if email_addr:
                    await self.send_ad_restricted_notification(email_addr)
                else:
                    logger.warning("Could not extract email for ad restricted")
            
            elif email_type == "payment_failed":
                email_addr = self.extract_email(message_text)
                if email_addr:
                    await self.send_payment_failed_notification(email_addr)
                else:
                    logger.warning("Could not extract email for payment failed")
            
            elif email_type == "ads_receipt":
                card_info = self.extract_card_info(message_text)
                amount = self.extract_amount(message_text)
                email_addr = self.extract_email(message_text)
                account_id = self.extract_account_id(message_text)
                
                if card_info and amount and email_addr and account_id:
                    await self.send_card_charged_notification(card_info, amount, email_addr, account_id)
                else:
                    logger.warning(f"Could not extract card info: card={card_info}, amount={amount}, email={email_addr}, account_id={account_id}")
        
        logger.info("Message handler registered successfully")
        return True
    
    async def run(self):
        """Main function to run the bot"""
        logger.info("Starting Mail Filter Bot...")
        
        if not await self.setup():
            logger.error("Failed to setup bot")
            return
        
        logger.info("Bot is running and monitoring messages...")
        logger.info("Press Ctrl+C to stop")
        
        try:
            # Keep the client running
            await self.client.run_until_disconnected()
        except KeyboardInterrupt:
            logger.info("Bot stopped by user")
        except Exception as e:
            logger.error(f"Bot crashed: {e}")
        finally:
            await self.client.disconnect()
            logger.info("Disconnected from Telegram")


async def main():
    bot = MailFilterBot()
    await bot.run()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
