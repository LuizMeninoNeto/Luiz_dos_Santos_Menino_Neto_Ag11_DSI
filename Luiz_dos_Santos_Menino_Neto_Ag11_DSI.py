"""Atividade Ag11_DSI - Controle de Níveis de Água.

Aluno: Luiz dos Santos Menino Neto
Objetivo: simular o monitoramento de um reservatório usando cores no terminal.
"""

from colorama import Fore, Style, init

# Lista com as situações correspondentes aos cinco níveis do reservatório.
SITUACOES = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)",
]


def definir_cor(nivel):
    """Retorna a cor adequada ao nível informado (de 1 a 5)."""
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]

    if nivel < 1 or nivel > len(cores):
        raise ValueError("O nível deve estar entre 1 e 5.")

    return cores[nivel - 1]


def exibir_situacao(nivel):
    """Mostra o alerta colorido e restaura a cor padrão do terminal."""
    cor = definir_cor(nivel)
    mensagem = SITUACOES[nivel - 1]
    print(f"{cor}Nível {nivel}: {mensagem}{Style.RESET_ALL}")


def main():
    # Habilita o suporte a cores, inclusive no terminal do Windows.
    init(autoreset=False)

    print("=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===")
    print("Simulação dos cinco níveis do reservatório:\n")

    # Valores definidos no próprio código: não é necessária entrada do usuário.
    niveis_simulados = [1, 2, 3, 4, 5]

    for nivel in niveis_simulados:
        exibir_situacao(nivel)

    print("\nSimulação concluída.")
    print(Style.RESET_ALL, end="")


if __name__ == "__main__":
    main()
