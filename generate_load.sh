#!/bin/bash

mkdir -p stress_test/src
mkdir -p stress_test/logs

echo "Generuji 500 souborů pro zátěžový test..."

KEYWORDS=("RSA" "AES" "DES" "Blowfish" "EC_KEY" "EVP_PKEY" "Kyber" "Dilithium")

for i in {1..500}
do
   # Vybere náhodné klíčové slovo
   KEYWORD=${KEYWORDS[$RANDOM % ${#KEYWORDS[@]}]}
   FILENAME="stress_test/src/service_mock_$i.py"
   
   # Vytvoří soubor, který vypadá jako kód
   cat <<EOF > $FILENAME
# Auto-generated mock service $i
import sys
import logging

class CryptoHandler$i:
    def process_data(self, data):
        # TODO: Refactor this logic
        encryption_method = "$KEYWORD" 
        print(f"Processing with {encryption_method}")
        return data[::-1]
EOF

done

echo "Generuji falešné binární soubory..."
for i in {1..20}
do
    dd if=/dev/urandom of=stress_test/logs/dump_$i.bin bs=1M count=1 2>/dev/null
done

echo "Hotovo. Repozitář je nyní naplněn daty."