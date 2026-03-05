const { ethers } = require('ethers');
const axios = require('axios');
const chalk = require('chalk');
const fs = require('fs');

// Robinhood Chain Testnet Configuration
const CONFIG = {
    rpc: 'https://testnet.rpc.robinhood.com',
    chainId: 51000,
    faucet: 'https://faucet.robinhood.com/api/claim',
    explorer: 'https://testnet.explorer.robinhood.com',
    walletFile: 'wallet.json'
};

class RobinhoodTestnet {
    constructor() {
        this.provider = new ethers.JsonRpcProvider(CONFIG.rpc);
        this.wallet = null;
        this.loadOrCreateWallet();
    }

    loadOrCreateWallet() {
        try {
            if (fs.existsSync(CONFIG.walletFile)) {
                const data = JSON.parse(fs.readFileSync(CONFIG.walletFile, 'utf8'));
                this.wallet = new ethers.Wallet(data.privateKey, this.provider);
                console.log(chalk.green('✅ Wallet loaded'));
                console.log(chalk.cyan(`👛 Address: ${this.wallet.address}\n`));
            } else {
                this.wallet = ethers.Wallet.createRandom().connect(this.provider);
                const walletData = {
                    address: this.wallet.address,
                    privateKey: this.wallet.privateKey
                };
                fs.writeFileSync(CONFIG.walletFile, JSON.stringify(walletData, null, 2));
                console.log(chalk.yellow('⚠️  New wallet created!'));
                console.log(chalk.cyan(`👛 Address: ${this.wallet.address}`));
                console.log(chalk.red(`🔑 Private Key: ${this.wallet.privateKey}`));
                console.log(chalk.yellow('⚠️  SAVE YOUR PRIVATE KEY!\n'));
            }
        } catch (error) {
            console.error(chalk.red('❌ Wallet error:', error.message));
            process.exit(1);
        }
    }

    async getBalance() {
        try {
            const balance = await this.provider.getBalance(this.wallet.address);
            return ethers.formatEther(balance);
        } catch (error) {
            console.error(chalk.red('❌ Balance error:', error.message));
            return '0';
        }
    }

    async claimFaucet() {
        console.log(chalk.yellow('💧 Requesting tokens from faucet...'));
        
        try {
            const response = await axios.post(CONFIG.faucet, {
                address: this.wallet.address,
                chainId: CONFIG.chainId
            }, {
                headers: {
                    'Content-Type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                },
                timeout: 30000
            });

            if (response.status === 200) {
                console.log(chalk.green('✅ Tokens claimed!'));
                await this.delay(5000);
                const balance = await this.getBalance();
                console.log(chalk.cyan(`💰 Balance: ${balance} ETH\n`));
                return true;
            }
        } catch (error) {
            if (error.response) {
                console.log(chalk.red(`❌ Faucet error: ${error.response.data}`));
            } else {
                console.log(chalk.red(`❌ Error: ${error.message}`));
            }
            return false;
        }
    }

    async deployContract() {
        console.log(chalk.yellow('📝 Deploying smart contract...'));
        
        try {
            const balance = await this.getBalance();
            if (parseFloat(balance) < 0.001) {
                console.log(chalk.red('❌ Insufficient funds'));
                return false;
            }

            // Simple contract bytecode
            const bytecode = '0x608060405234801561001057600080fd5b506040516102083803806102088339818101604052602081101561003357600080fd5b810190808051604051939291908464010000000082111561005357600080fd5b90830190602082018581111561006857600080fd5b825164010000000081118282018810171561008257600080fd5b82525081516020918201929091019080838360005b838110156100af578181015183820152602001610097565b50505050905090810190601f1680156100dc5780820380516001836020036101000a031916815260200191505b506040525050600080546100f29082019061012f565b5050506101cc565b634e487b7160e01b600052604160045260246000fd5b601f19601f830116810181811067ffffffffffffffff8211171561014e5761014e6100fa565b6040525050565b600067ffffffffffffffff82111561016f5761016f6100fa565b5060209081020190565b6000610184610110565b905061019082826101b3565b919050565b6000610184610110565b5060209081020190565b634e487b7160e01b600052604160045260246000fd5b601f19601f830116810181811067ffffffffffffffff821117156101d9576101d96100fa565b6040525050565b60cf806101ee6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c8063cfae3217146037578063ef690cc0146053575b600080fd5b603d6059565b60405160499190607c565b60405180910390f35b603d60eb565b60606000805460019190606e90605c565b80601f016020809104026020016040519081016040528092919081815260200182805460019190606e90605c565b80156020020182019050815481529060010190602001808311609b57829003601f168201915b505050505090505b90565b600060208252825180602084015260005b818110156060578581018301518582016040015282016048565b506000604082850101526040601f19601f830116830101915050919050565b634e487b7160e01b600052602260045260246000fdfea26469706673582212';

            const tx = await this.wallet.sendTransaction({
                data: bytecode,
                gasLimit: 500000
            });

            console.log(chalk.cyan(`📤 Transaction: ${tx.hash}`));
            console.log(chalk.yellow('⏳ Waiting for confirmation...'));

            const receipt = await tx.wait();

            if (receipt.status === 1) {
                console.log(chalk.green('✅ Contract deployed!'));
                console.log(chalk.cyan(`📍 Address: ${receipt.contractAddress}`));
                console.log(chalk.cyan(`🔍 ${CONFIG.explorer}/tx/${tx.hash}\n`));
                return true;
            } else {
                console.log(chalk.red('❌ Deployment failed'));
                return false;
            }
        } catch (error) {
            console.error(chalk.red('❌ Deployment error:', error.message));
            return false;
        }
    }

    async sendTransaction() {
        console.log(chalk.yellow('💸 Sending transaction...'));
        
        try {
            const balance = await this.getBalance();
            if (parseFloat(balance) < 0.001) {
                console.log(chalk.red('❌ Insufficient funds'));
                return false;
            }

            const tx = await this.wallet.sendTransaction({
                to: this.wallet.address,
                value: ethers.parseEther('0.0001')
            });

            console.log(chalk.cyan(`📤 TX: ${tx.hash}`));

            const receipt = await tx.wait();

            if (receipt.status === 1) {
                console.log(chalk.green('✅ Transaction successful!'));
                console.log(chalk.cyan(`🔍 ${CONFIG.explorer}/tx/${tx.hash}\n`));
                return true;
            }
        } catch (error) {
            console.error(chalk.red('❌ Error:', error.message));
            return false;
        }
    }

    async delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async runAutomation(numTx = 5) {
        console.log(chalk.green('\n' + '='.repeat(60)));
        console.log(chalk.green('🤖 Robinhood Chain Testnet Automation'));
        console.log(chalk.green('='.repeat(60) + '\n'));
        console.log(chalk.cyan(`👛 Address: ${this.wallet.address}`));
        console.log(chalk.cyan(`🔍 ${CONFIG.explorer}/address/${this.wallet.address}\n`));

        // Step 1: Faucet
        console.log(chalk.magenta('='.repeat(60)));
        console.log(chalk.magenta('STEP 1: Claiming Tokens'));
        console.log(chalk.magenta('='.repeat(60)));
        await this.claimFaucet();

        // Step 2: Deploy
        console.log(chalk.magenta('='.repeat(60)));
        console.log(chalk.magenta('STEP 2: Deploying Contract'));
        console.log(chalk.magenta('='.repeat(60)));
        await this.deployContract();

        // Step 3: Transactions
        console.log(chalk.magenta('='.repeat(60)));
        console.log(chalk.magenta(`STEP 3: Creating Activity (${numTx} transactions)`));
        console.log(chalk.magenta('='.repeat(60)));

        for (let i = 0; i < numTx; i++) {
            console.log(chalk.cyan(`\n📊 Transaction ${i + 1}/${numTx}`));
            await this.sendTransaction();
            if (i < numTx - 1) await this.delay(10000);
        }

        // Final report
        console.log(chalk.green('\n' + '='.repeat(60)));
        console.log(chalk.green('✅ AUTOMATION COMPLETED!'));
        console.log(chalk.green('='.repeat(60) + '\n'));

        const finalBalance = await this.getBalance();
        console.log(chalk.cyan(`💰 Balance: ${finalBalance} ETH`));
        console.log(chalk.cyan(`👤 Address: ${this.wallet.address}`));
        console.log(chalk.cyan(`🔍 ${CONFIG.explorer}/address/${this.wallet.address}`));
        
        console.log(chalk.yellow('\n💡 Next Steps:'));
        console.log(chalk.white('   • Register .hood domain: https://infinityname.io'));
        console.log(chalk.white('   • Send GM on OnchainGM: https://onchaingm.xyz'));
        console.log(chalk.white('   • Mint badge on Robinhood Chain'));
        console.log(chalk.white('   • Return periodically for more activity\n'));
    }
}

async function main() {
    console.log(chalk.cyan('🚀 Robinhood Chain Testnet Automation\n'));
    
    const bot = new RobinhoodTestnet();
    
    try {
        await bot.runAutomation(5);
    } catch (error) {
        console.error(chalk.red('\n❌ Error:', error.message));
        process.exit(1);
    }
}

main();
