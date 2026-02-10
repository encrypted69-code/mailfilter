# GitHub Upload Instructions

## Step 1: Install Git (if not already installed)
Download and install Git from: https://git-scm.com/download/win

Or install via winget:
```powershell
winget install --id Git.Git -e --source winget
```

After installation, restart your terminal.

## Step 2: Configure Git (First time only)
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 3: Upload to GitHub
Run these commands in your project folder:

```powershell
cd "c:\projects\indo mail"

# Initialize git repository
git init

# Add all files (respects .gitignore)
git add .

# Commit changes
git commit -m "Initial commit - Instagram Mail Filter Bot"

# Add your GitHub repository as remote
git remote add origin https://github.com/encrypted69-code/mailfilter.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Alternative: Quick Upload Script
Run the batch file created: UPLOAD_TO_GITHUB.bat

---

## Important Notes:
- Your .gitignore file will prevent sensitive files from being uploaded:
  - config.py (contains API credentials)
  - vps_credentials.txt (contains VPS password)
  - *.session files (Telegram session data)
  
- These files will NOT be uploaded to GitHub (kept safe locally)
- Only the code and documentation will be public

## If you need to authenticate:
GitHub may ask for credentials. Use:
- Username: encrypted69-code
- Password: Use a Personal Access Token (not your GitHub password)
  
Generate token at: https://github.com/settings/tokens
