#!/bin/bash
echo "Executando setup.sh..."
mkdir -p output
python3 main.py
echo "Concluído." > output/status.txt
