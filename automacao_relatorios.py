"""
Projeto demonstrativo de automação de relatórios.

Este código gera oito relatórios fictícios para demonstrar
uma rotina automatizada, sem utilizar sistemas ou dados reais.
"""

import csv
from datetime import datetime
from pathlib import Path


RELATORIOS = [
    "resumo_atendimento",
    "volume_por_periodo",
    "tempo_medio_atendimento",
    "chamadas_recebidas",
    "chamadas_atendidas",
    "chamadas_abandonadas",
    "desempenho_operacional",
    "indicadores_diarios",
]


def gerar_relatorio(nome_relatorio):
    """Gera um arquivo CSV com informações fictícias."""

    pasta_saida = Path("relatorios")
    pasta_saida.mkdir(exist_ok=True)

    data_atual = datetime.now().strftime("%Y-%m-%d")
    nome_arquivo = f"{nome_relatorio}_{data_atual}.csv"
    caminho_arquivo = pasta_saida / nome_arquivo

    dados_ficticios = [
        ["indicador", "valor"],
        ["registros_processados", 100],
        ["status", "concluido"],
        ["data_execucao", data_atual],
    ]

    with caminho_arquivo.open(
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerows(dados_ficticios)

    print(f"Relatório criado: {nome_arquivo}")


def executar_automacao():
    """Executa a geração dos oito relatórios demonstrativos."""

    print("Automação iniciada.")
    print(f"Quantidade de relatórios: {len(RELATORIOS)}")

    for relatorio in RELATORIOS:
        gerar_relatorio(relatorio)

    print("Automação finalizada com sucesso!")


if __name__ == "__main__":
    executar_automacao()
