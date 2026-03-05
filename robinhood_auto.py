#!/usr/bin/env python3
"""
Robinhood Chain Testnet Automation Tool
Automate interactions with Robinhood Chain testnet
"""

import json
import time
from web3 import Web3
from eth_account import Account
import requests
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

class RobinhoodTestnet:
    def __init__(self, private_key=None):
        # Robinhood Chain Testnet RPC
        self.rpc_url = "https://testnet.rpc.robinhood.com"
        self.chain_id = 51000  # Robinhood Chain testnet chain ID
        self.faucet_url = "https://faucet.robinhood.com/api/claim"
        self.explorer_url = "https://testnet.explorer.robinhood.com"
        
        # Initialize Web3
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
        
        # Account setup
        if private_key:
            self.account = Account.from_key(private_key)
        else:
            self.account = Account.create()
            print(f"{Fore.YELLOW}⚠️  New wallet created!")
            print(f"{Fore.CYAN}Address: {self.account.address}")
            print(f"{Fore.RED}Private Key: {self.account.key.hex()}")
            print(f"{Fore.YELLOW}⚠️  SAVE YOUR PRIVATE KEY IN A SECURE PLACE!\n")
        
        self.address = self.account.address

    def print_header(self):
        """Display header"""
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"{Fore.GREEN}🤖 Robinhood Chain Testnet Automation Tool")
        print(f"{Fore.GREEN}{'='*60}\n")
        print(f"{Fore.CYAN}Wallet Address: {self.address}")
        print(f"{Fore.CYAN}Explorer: {self.explorer_url}/address/{self.address}\n")

    def get_balance(self):
        """Get wallet balance"""
        try:
            balance_wei = self.w3.eth.get_balance(self.address)
            balance_eth = self.w3.from_wei(balance_wei, 'ether')
            return float(balance_eth)
        except Exception as e:
            print(f"{Fore.RED}❌ Error getting balance: {e}")
            return 0

    def claim_faucet(self):
        """Claim testnet tokens from faucet"""
        print(f"{Fore.YELLOW}💧 Requesting testnet tokens from faucet...")
        
        try:
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
            }
            
            payload = {
                'address': self.address,
                'chainId': self.chain_id
            }
            
            response = requests.post(
                self.faucet_url,
                json=payload,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                print(f"{Fore.GREEN}✅ Tokens claimed successfully!")
                time.sleep(5)  # Wait for transaction confirmation
                balance = self.get_balance()
                print(f"{Fore.CYAN}💰 Balance: {balance:.6f} ETH")
                return True
            else:
                print(f"{Fore.RED}❌ Faucet error: {response.text}")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}❌ Error requesting faucet: {e}")
            return False

    def deploy_simple_contract(self):
        """Deploy a simple smart contract"""
        print(f"\n{Fore.YELLOW}📝 Deploying smart contract...")
        
        # Simple contract bytecode
        bytecode = "0x608060405234801561001057600080fd5b506040516102083803806102088339818101604052602081101561003357600080fd5b810190808051604051939291908464010000000082111561005357600080fd5b90830190602082018581111561006857600080fd5b825164010000000081118282018810171561008257600080fd5b82525081516020918201929091019080838360005b838110156100af578181015183820152602001610097565b50505050905090810190601f1680156100dc5780820380516001836020036101000a031916815260200191505b506040525050600080546100f29082019061012f565b5050506101cc565b634e487b7160e01b600052604160045260246000fd5b601f19601f830116810181811067ffffffffffffffff8211171561014e5761014e6100fa565b6040525050565b600067ffffffffffffffff82111561016f5761016f6100fa565b5060209081020190565b6000610184610110565b905061019082826101b3565b919050565b6000610184610110565b5060209081020190565b634e487b7160e01b600052604160045260246000fd5b601f19601f830116810181811067ffffffffffffffff821117156101d9576101d96100fa565b6040525050565b60cf806101ee6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c8063cfae3217146037578063ef690cc0146053575b600080fd5b603d6059565b60405160499190607c565b60405180910390f35b603d60eb565b60606000805460019190606e90605c565b80601f016020809104026020016040519081016040528092919081815260200182805460019190606e90605c565b80156020020182019050815481529060010190602001808311609b57829003601f168201915b505050505090505b90565b600060208252825180602084015260005b818110156060578581018301518582016040015282016048565b506000604082850101526040601f19601f830116830101915050919050565b634e487b7160e01b600052602260045260246000fdfea26469706673582212"
        
        try:
            balance = self.get_balance()
            if balance < 0.001:
                print(f"{Fore.RED}❌ Insufficient funds for deployment. Claim from faucet first.")
                return False
            
            # Create deployment transaction
            nonce = self.w3.eth.get_transaction_count(self.address)
            
            transaction = {
                'from': self.address,
                'nonce': nonce,
                'gas': 500000,
                'gasPrice': self.w3.eth.gas_price,
                'data': bytecode,
                'chainId': self.chain_id
            }
            
            # Sign transaction
            signed_txn = self.w3.eth.account.sign_transaction(transaction, self.account.key)
            
            # Send transaction
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            
            print(f"{Fore.CYAN}📤 Transaction sent: {tx_hash.hex()}")
            print(f"{Fore.YELLOW}⏳ Waiting for confirmation...")
            
            # Wait for confirmation
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
            
            if receipt['status'] == 1:
                contract_address = receipt['contractAddress']
                print(f"{Fore.GREEN}✅ Contract deployed successfully!")
                print(f"{Fore.CYAN}📍 Contract Address: {contract_address}")
                print(f"{Fore.CYAN}🔍 {self.explorer_url}/tx/{tx_hash.hex()}")
                return True
            else:
                print(f"{Fore.RED}❌ Transaction failed")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}❌ Deployment error: {e}")
            return False

    def send_test_transaction(self):
        """Send a test transaction"""
        print(f"\n{Fore.YELLOW}💸 Sending test transaction...")
        
        try:
            balance = self.get_balance()
            if balance < 0.001:
                print(f"{Fore.RED}❌ Insufficient funds")
                return False
            
            # Send small amount to self
            nonce = self.w3.eth.get_transaction_count(self.address)
            
            transaction = {
                'from': self.address,
                'to': self.address,
                'value': self.w3.to_wei(0.0001, 'ether'),
                'nonce': nonce,
                'gas': 21000,
                'gasPrice': self.w3.eth.gas_price,
                'chainId': self.chain_id
            }
            
            signed_txn = self.w3.eth.account.sign_transaction(transaction, self.account.key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            
            print(f"{Fore.CYAN}📤 Transaction sent: {tx_hash.hex()}")
            
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=60)
            
            if receipt['status'] == 1:
                print(f"{Fore.GREEN}✅ Transaction successful!")
                print(f"{Fore.CYAN}🔍 {self.explorer_url}/tx/{tx_hash.hex()}")
                return True
            else:
                print(f"{Fore.RED}❌ Transaction failed")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}❌ Error: {e}")
            return False

    def run_automation(self, num_transactions=5):
        """Run full automation"""
        self.print_header()
        
        # Step 1: Claim tokens
        print(f"{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}STEP 1: Claiming Testnet Tokens")
        print(f"{Fore.MAGENTA}{'='*60}")
        self.claim_faucet()
        
        # Step 2: Deploy contract
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}STEP 2: Deploying Smart Contract")
        print(f"{Fore.MAGENTA}{'='*60}")
        self.deploy_simple_contract()
        
        # Step 3: Create transactions
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}STEP 3: Creating Activity ({num_transactions} transactions)")
        print(f"{Fore.MAGENTA}{'='*60}")
        
        for i in range(num_transactions):
            print(f"\n{Fore.CYAN}📊 Transaction {i+1}/{num_transactions}")
            self.send_test_transaction()
            if i < num_transactions - 1:
                time.sleep(10)  # Pause between transactions
        
        # Final report
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"{Fore.GREEN}✅ AUTOMATION COMPLETED!")
        print(f"{Fore.GREEN}{'='*60}\n")
        
        balance = self.get_balance()
        print(f"{Fore.CYAN}💰 Final Balance: {balance:.6f} ETH")
        print(f"{Fore.CYAN}👤 Your Address: {self.address}")
        print(f"{Fore.CYAN}🔍 Explorer: {self.explorer_url}/address/{self.address}")
        print(f"\n{Fore.YELLOW}💡 Next Steps:")
        print(f"{Fore.WHITE}   • Register .hood domain: https://infinityname.io")
        print(f"{Fore.WHITE}   • Send GM on OnchainGM: https://onchaingm.xyz")
        print(f"{Fore.WHITE}   • Mint badge on Robinhood Chain")
        print(f"{Fore.WHITE}   • Return periodically to create more activity\n")


def main():
    """Main function"""
    print(f"{Fore.CYAN}🚀 Robinhood Chain Testnet Automation\n")
    
    # Check for saved wallet
    try:
        with open('wallet.json', 'r') as f:
            wallet_data = json.load(f)
            private_key = wallet_data['private_key']
            print(f"{Fore.GREEN}✅ Loaded saved wallet")
    except FileNotFoundError:
        private_key = None
        print(f"{Fore.YELLOW}⚠️  No wallet found, creating new one...")
    
    # Create bot instance
    bot = RobinhoodTestnet(private_key)
    
    # Save wallet
    if not private_key:
        wallet_data = {
            'address': bot.address,
            'private_key': bot.account.key.hex()
        }
        with open('wallet.json', 'w') as f:
            json.dump(wallet_data, f, indent=2)
        print(f"{Fore.GREEN}✅ Wallet saved to wallet.json\n")
    
    # Run automation
    try:
        bot.run_automation(num_transactions=5)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error: {e}")


if __name__ == "__main__":
    main()
