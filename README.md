# Controle de Níveis de Água — Agenda 11 (DSI)

**Aluno:** Luiz dos Santos Menino Neto  
**Atividade:** Ag11_DSI — Controle de Níveis de Água

## Descrição

Projeto em Python que simula, no terminal, o monitoramento de um reservatório de água. O programa percorre cinco níveis pré-definidos, exibe a situação correspondente com uma cor distinta e restaura o estilo padrão do terminal após cada alerta.

| Nível | Situação | Cor |
| --- | --- | --- |
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Requisitos

- Python 3.9 ou superior.
- Biblioteca `colorama` (declarada em `requirements.txt`).

## Como executar

Abra um terminal na pasta do projeto e instale a dependência:

```bash
python -m pip install -r requirements.txt
```

Execute o programa:

```bash
python Luiz_dos_Santos_Menino_Neto_Ag11_DSI.py
```

Em computadores nos quais o comando `python` não esteja disponível, experimente `python3` ou, no Windows, `py`.

## Funcionamento do código

1. A lista `SITUACOES` armazena as mensagens dos cinco níveis.
2. A função `definir_cor(nivel)` associa cada número à cor adequada utilizando `Fore`, da biblioteca `colorama`.
3. A função `exibir_situacao(nivel)` imprime o nível e sua mensagem colorida e aplica `Style.RESET_ALL` para restaurar o estilo.
4. A função `main()` inicializa o `colorama` e simula sequencialmente os níveis `[1, 2, 3, 4, 5]`, sem solicitar dados ao usuário.

## Saída esperada

As cinco linhas a seguir são exibidas no terminal, cada uma com sua respectiva cor:

```text
=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===
Simulação dos cinco níveis do reservatório:

Nível 1: Muito baixo (crítico)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (alerta)

Simulação concluída.
```

As cores dependem do suporte a ANSI do terminal utilizado.

## Arquivos

- `Luiz_dos_Santos_Menino_Neto_Ag11_DSI.py`: código-fonte da atividade.
- `requirements.txt`: dependência do projeto.
- `.gitignore`: exclusões recomendadas para o repositório.
- `README.md`: documentação e instruções de execução.

## Publicação no GitHub

1. Crie um repositório público no GitHub, por exemplo, com o nome `Luiz_dos_Santos_Menino_Neto_Ag11_DSI`.
2. Envie os quatro arquivos deste projeto para a raiz do repositório, sem colocar apenas o ZIP.
3. Confira se o arquivo `.py` aparece no repositório e se o `README.md` é exibido na página inicial.
4. Copie a **URL real do repositório** e envie-a no fichário da atividade.

> O projeto está preparado para publicação, mas a criação do repositório e o envio dos arquivos devem ser concluídos na conta GitHub do aluno.
