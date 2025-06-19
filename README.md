# Bob-Sponja Report Generator

This repository contains a simple Python script for generating customizable text reports.

## Usage

```bash
python report_generator.py \
    --title "My Report" \
    --author "Seu Nome" \
    --section "Introducao:Este e o texto de introducao" \
    --section "Resultados:Os resultados estao aqui" \
    --output meu_relatorio.txt
```

The script accepts multiple `--section` arguments, each in the format `"Titulo:Conteudo"`. The generated report is saved to the file provided via `--output`.
