#!/bin/bash

# Проверка системы перед использованием

echo "🔍 Проверка системных требований..."
echo ""

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

ERRORS=0

# Проверка macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo -e "${RED}❌ Не macOS${NC}"
    ERRORS=$((ERRORS + 1))
else
    echo -e "${GREEN}✅ macOS${NC}"
fi

# Проверка Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo -e "${GREEN}✅ Python 3 установлен (версия $PYTHON_VERSION)${NC}"
else
    echo -e "${RED}❌ Python 3 не найден${NC}"
    ERRORS=$((ERRORS + 1))
fi

# Проверка Node.js
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✅ Node.js установлен (версия $NODE_VERSION)${NC}"
else
    echo -e "${RED}❌ Node.js не найден${NC}"
    ERRORS=$((ERRORS + 1))
fi

# Проверка npm
if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✅ npm установлен (версия $NPM_VERSION)${NC}"
else
    echo -e "${RED}❌ npm не найден${NC}"
    ERRORS=$((ERRORS + 1))
fi

# Проверка pip
if command -v pip3 &> /dev/null; then
    PIP_VERSION=$(pip3 --version | cut -d' ' -f2)
    echo -e "${GREEN}✅ pip3 установлен (версия $PIP_VERSION)${NC}"
else
    echo -e "${RED}❌ pip3 не найден${NC}"
    ERRORS=$((ERRORS + 1))
fi

echo ""
echo "🔍 Проверка Python библиотек..."

# Проверка Python библиотек
for lib in web3 eth_account requests colorama; do
    if python3 -c "import $lib" 2>/dev/null; then
        echo -e "${GREEN}✅ $lib${NC}"
    else
        echo -e "${YELLOW}⚠️  $lib не установлен${NC}"
    fi
done

echo ""
echo "🔍 Проверка Node.js библиотек..."

# Проверка Node.js пакетов
if [ -d "node_modules" ]; then
    for pkg in ethers axios chalk dotenv; do
        if [ -d "node_modules/$pkg" ]; then
            echo -e "${GREEN}✅ $pkg${NC}"
        else
            echo -e "${YELLOW}⚠️  $pkg не установлен${NC}"
        fi
    done
else
    echo -e "${YELLOW}⚠️  node_modules не найдена. Запустите: npm install${NC}"
fi

echo ""
echo "🔍 Проверка файлов проекта..."

# Проверка файлов
for file in robinhood_auto.py index.js install.sh package.json requirements.txt README.md; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✅ $file${NC}"
    else
        echo -e "${RED}❌ $file не найден${NC}"
        ERRORS=$((ERRORS + 1))
    fi
done

echo ""
echo "================================"
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✅ Все проверки пройдены!${NC}"
    echo "Можно запускать:"
    echo "  python3 robinhood_auto.py"
    echo "  или"
    echo "  node index.js"
else
    echo -e "${RED}❌ Найдено ошибок: $ERRORS${NC}"
    echo "Запустите: ./install.sh"
fi
echo "================================"
echo ""
