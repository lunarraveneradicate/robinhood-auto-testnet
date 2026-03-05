#!/usr/bin/env python3
"""
Robinhood Chain Testnet - Интерактивный режим
"""

import json
import os
from colorama import Fore, Style, init
from robinhood_auto import RobinhoodTestnet

init(autoreset=True)

def print_menu():
    """Показать меню"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}🎮 Robinhood Chain Testnet - Интерактивный режим")
    print(f"{Fore.CYAN}{'='*60}\n")
    print(f"{Fore.YELLOW}1.{Fore.WHITE} 💧 Получить токены из faucet")
    print(f"{Fore.YELLOW}2.{Fore.WHITE} 📝 Задеплоить смарт-контракт")
    print(f"{Fore.YELLOW}3.{Fore.WHITE} 💸 Отправить транзакцию")
    print(f"{Fore.YELLOW}4.{Fore.WHITE} 💰 Проверить баланс")
    print(f"{Fore.YELLOW}5.{Fore.WHITE} 🤖 Запустить полную автоматизацию")
    print(f"{Fore.YELLOW}6.{Fore.WHITE} 🔍 Открыть explorer")
    print(f"{Fore.YELLOW}7.{Fore.WHITE} 🔑 Показать приватный ключ")
    print(f"{Fore.YELLOW}8.{Fore.WHITE} 📊 Статистика кошелька")
    print(f"{Fore.YELLOW}0.{Fore.WHITE} ❌ Выход")
    print(f"\n{Fore.CYAN}{'='*60}")

def show_wallet_stats(bot):
    """Показать статистику кошелька"""
    print(f"\n{Fore.CYAN}📊 Статистика кошелька:")
    print(f"{Fore.WHITE}{'='*60}")
    balance = bot.get_balance()
    print(f"{Fore.YELLOW}Адрес:{Fore.WHITE} {bot.address}")
    print(f"{Fore.YELLOW}Баланс:{Fore.WHITE} {balance:.6f} ETH")
    print(f"{Fore.YELLOW}Chain ID:{Fore.WHITE} {bot.chain_id}")
    print(f"{Fore.YELLOW}Network:{Fore.WHITE} Robinhood Chain Testnet")
    print(f"\n{Fore.CYAN}🔍 Explorer:")
    print(f"{Fore.WHITE}{bot.explorer_url}/address/{bot.address}")
    print(f"{Fore.WHITE}{'='*60}\n")

def main():
    """Главная функция интерактивного режима"""
    print(f"{Fore.GREEN}🚀 Загрузка Robinhood Chain Testnet Bot...\n")
    
    # Проверяем кошелек
    try:
        if os.path.exists('wallet.json'):
            with open('wallet.json', 'r') as f:
                wallet_data = json.load(f)
                private_key = wallet_data['private_key']
                print(f"{Fore.GREEN}✅ Кошелек загружен из wallet.json")
        else:
            private_key = None
            print(f"{Fore.YELLOW}⚠️  Создается новый кошелек...")
    except Exception as e:
        print(f"{Fore.RED}❌ Ошибка загрузки кошелька: {e}")
        return
    
    # Создаем бота
    bot = RobinhoodTestnet(private_key)
    
    # Сохраняем новый кошелек если создан
    if not os.path.exists('wallet.json'):
        wallet_data = {
            'address': bot.address,
            'private_key': bot.account.key.hex()
        }
        with open('wallet.json', 'w') as f:
            json.dump(wallet_data, f, indent=2)
        print(f"{Fore.GREEN}✅ Кошелек сохранен в wallet.json\n")
    
    # Основной цикл
    while True:
        print_menu()
        choice = input(f"{Fore.CYAN}Выберите действие (0-8): {Fore.WHITE}").strip()
        
        if choice == '1':
            bot.claim_faucet()
        
        elif choice == '2':
            bot.deploy_simple_contract()
        
        elif choice == '3':
            bot.send_test_transaction()
        
        elif choice == '4':
            balance = bot.get_balance()
            print(f"\n{Fore.GREEN}💰 Текущий баланс: {balance:.6f} ETH\n")
        
        elif choice == '5':
            num_tx = input(f"{Fore.CYAN}Количество транзакций (по умолчанию 5): {Fore.WHITE}").strip()
            try:
                num_tx = int(num_tx) if num_tx else 5
            except ValueError:
                num_tx = 5
            bot.run_automation(num_tx)
        
        elif choice == '6':
            url = f"{bot.explorer_url}/address/{bot.address}"
            print(f"\n{Fore.CYAN}🔍 Explorer: {Fore.WHITE}{url}")
            print(f"{Fore.YELLOW}Скопируйте ссылку выше и откройте в браузере\n")
        
        elif choice == '7':
            print(f"\n{Fore.RED}⚠️  ПРЕДУПРЕЖДЕНИЕ: Никогда не делитесь приватным ключом!")
            confirm = input(f"{Fore.YELLOW}Показать приватный ключ? (yes/no): {Fore.WHITE}").strip().lower()
            if confirm == 'yes':
                print(f"\n{Fore.RED}🔑 Private Key: {bot.account.key.hex()}")
                print(f"{Fore.YELLOW}⚠️  Сохраните в безопасном месте!\n")
            else:
                print(f"{Fore.GREEN}Отменено\n")
        
        elif choice == '8':
            show_wallet_stats(bot)
        
        elif choice == '0':
            print(f"\n{Fore.GREEN}👋 До встречи! Удачи с airdrop!\n")
            break
        
        else:
            print(f"\n{Fore.RED}❌ Неверный выбор. Попробуйте снова.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}⚠️  Прервано пользователем. До встречи!\n")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Ошибка: {e}\n")
