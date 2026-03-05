# 🎯 Команды для быстрого использования

## Установка

```bash
# Клонировать проект
git clone https://github.com/YOUR_REPO/robinhood-auto-testnet.git
cd robinhood-auto-testnet

# Установить все зависимости
./install.sh

# Проверить установку
./check.sh
```

## Основное использование

```bash
# Python - автоматический режим (рекомендуется)
python3 robinhood_auto.py

# Python - интерактивный режим
python3 interactive.py

# Node.js - автоматический режим
node index.js
```

## Алиасы (после установки и перезапуска терминала)

```bash
# Python версия
robinhood-auto

# Node.js версия
robinhood-auto-js

# Интерактивный режим
robinhood-interactive
```

## Ручная установка зависимостей

```bash
# Python
pip3 install -r requirements.txt

# Node.js
npm install
```

## Управление кошельком

```bash
# Посмотреть адрес кошелька
cat wallet.json | grep address

# Посмотреть приватный ключ (ОСТОРОЖНО!)
cat wallet.json | grep privateKey

# Создать бэкап
cp wallet.json wallet.backup.json

# Удалить кошелек (создастся новый при следующем запуске)
rm wallet.json
```

## Проверка активности

```bash
# Открыть explorer в браузере
# Замените YOUR_ADDRESS на ваш адрес из wallet.json
open https://testnet.explorer.robinhood.com/address/YOUR_ADDRESS
```

## Полезные ссылки

```bash
# Faucet
open https://faucet.robinhood.com

# InfinityName (.hood domains)
open https://infinityname.io

# OnchainGM
open https://onchaingm.xyz

# Explorer
open https://testnet.explorer.robinhood.com
```

## Расширенное использование

```bash
# Запустить с кастомным количеством транзакций (Python)
# Отредактируйте robinhood_auto.py, измените num_transactions=5 на нужное

# Использовать существующий приватный ключ
# Создайте wallet.json вручную:
echo '{
  "address": "YOUR_ADDRESS",
  "private_key": "YOUR_PRIVATE_KEY"
}' > wallet.json

# Запустить в фоновом режиме
nohup python3 robinhood_auto.py > output.log 2>&1 &

# Посмотреть логи
tail -f output.log
```

## Отладка

```bash
# Проверить подключение к RPC
curl -X POST https://testnet.rpc.robinhood.com \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'

# Проверить баланс (замените ADDRESS)
curl -X POST https://testnet.rpc.robinhood.com \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_getBalance","params":["ADDRESS","latest"],"id":1}'

# Тест faucet API
curl -X POST https://faucet.robinhood.com/api/claim \
  -H "Content-Type: application/json" \
  -d '{"address":"YOUR_ADDRESS","chainId":51000}'
```

## Обновление проекта

```bash
# Обновить из git
git pull origin main

# Переустановить зависимости
./install.sh

# Проверить обновления
./check.sh
```

## Очистка

```bash
# Удалить node_modules
rm -rf node_modules

# Удалить Python кэш
find . -type d -name "__pycache__" -exec rm -r {} +

# Полная очистка (сохранит wallet.json)
rm -rf node_modules
find . -type d -name "__pycache__" -exec rm -r {} +
npm install
pip3 install -r requirements.txt
```

## Безопасность

```bash
# НИКОГДА не выполняйте эти команды публично:
cat wallet.json  # Покажет приватный ключ
echo $PRIVATE_KEY  # Если используете env переменные

# Безопасный способ проверить адрес:
cat wallet.json | grep address | grep -v private

# Изменить права доступа к wallet.json
chmod 600 wallet.json  # Только владелец может читать/писать
```

## Автоматизация

```bash
# Создать cron job для ежедневного запуска
# Откройте crontab
crontab -e

# Добавьте строку (запуск каждый день в 10:00)
0 10 * * * cd /path/to/robinhood-auto-testnet && python3 robinhood_auto.py >> ~/robinhood-cron.log 2>&1

# Проверить cron jobs
crontab -l
```

## Советы

- 💡 Запускайте скрипт 1-2 раза в неделю
- 💡 Делайте бэкап wallet.json регулярно
- 💡 Следите за официальными новостями
- 💡 Не делитесь приватным ключом НИКОГДА
- 💡 Используйте только для testnet
