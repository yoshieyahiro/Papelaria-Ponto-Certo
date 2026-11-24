[README.md](https://github.com/user-attachments/files/35363389/README.md)
# Passo a Passo: Sistema da Papelaria Ponto Certo (Python)

Este guia mostra como construir, do zero e em pequenas etapas, o sistema de terminal da **Papelaria Ponto Certo**.  
Ele foi pensado para quem já conhece o básico (`variáveis`, `input`, `print`, `for`, `while`, `if/else`) e quer consolidar o uso de **funções (`def`)**, **organização com `main()`** e **gravação em arquivos `.csv`**.

> **Sobre bibliotecas externas e `venv`:**  
> Neste projeto usaremos **apenas recursos nativos do Python** (`open()` e o módulo padrão `os`). Como não há bibliotecas externas para instalar, **não é necessário criar uma `venv`**. Basta abrir a pasta do projeto no Visual Studio Code e criar um arquivo chamado `papelaria.py`.

---

## Etapa 0 — Construção Lógica (Antes de escrever código)

Antes de digitar qualquer linha, precisamos entender como o sistema funciona por partes, evitando o famoso **"script tudão"** (um arquivo gigante com tudo misturado dentro de um único `while`).

### 1. As 4 partes do sistema
1. **Menu (`mostrar_menu`)**: apenas exibe as opções na tela. Ele não altera listas nem grava arquivos.
2. **Funções (`def`)**: cada tarefa do sistema ganha sua própria função com uma responsabilidade clara:
   * `listar_produtos(produtos)` → lê e mostra o catálogo.
   * `alterar_produto(produtos)` → altera nome/preço em `produtos`.
   * `registrar_venda(produtos, vendas)` → confere se o produto existe e adiciona em `vendas`.
   * `cancelar_venda(vendas)` → remove um registro de `vendas`.
   * `classificar_desempenho(vendas)` → analisa o histórico em `vendas`.
   * `salvar_produtos`, `carregar_produtos`, `salvar_vendas`, `carregar_vendas` → cuidam apenas dos arquivos `.csv`.
3. **Dados em memória (listas)**:
   * `produtos`: guarda o catálogo atual, por exemplo `["Caderno", 18.50]`.
   * `vendas`: guarda o histórico do que já foi vendido, por exemplo `["Caderno", 10, "2026-08-01"]`.
4. **Fluxo (`main`)**: coordena o programa do início ao fim.

### 2. Por que usar `def` e `main()`?
* **`def` (função)** é um bloco de código com nome próprio que recebe dados (**parâmetros**), executa uma tarefa específica e pode devolver um resultado (`return`). Se algo der errado ao alterar um produto, você já sabe exatamente em qual função procurar.
* **`def main():`** é a função principal (coordenadora). Em vez de deixar comandos soltos pelo arquivo, colocamos o carregamento inicial dos dados e o `while` do menu dentro de `main()`.
* **`if __name__ == "__main__":`**: é a porta de entrada padrão em Python. Ela garante que `main()` só seja executada quando você rodar o arquivo `papelaria.py` diretamente.

---

## Passo 1 — Criando o esqueleto com `main()` e o Menu

Vamos começar com um programa mínimo que apenas exibe o menu, lê a escolha do usuário e sai quando ele digitar `0`.

**O que estamos criando neste passo:**
* A função `mostrar_menu()`.
* A função `main()` com os dados iniciais (`produtos_padrao` e `vendas_padrao`) e o laço `while True`.
* O bloco `if __name__ == "__main__":` no final do arquivo.

Crie o arquivo `papelaria.py` e digite:

```python
def mostrar_menu():
    print("\n=== PAPELARIA PONTO CERTO ===")
    print("1 - Listar produtos")
    print("2 - Alterar produto")
    print("3 - Registrar venda")
    print("4 - Cancelar venda")
    print("5 - Classificar desempenho")
    print("0 - Sair")


def main():
    produtos = [
        ["Caderno", 18.50],
        ["Caneta", 4.50],
        ["Lápis", 1.50],
    ]

    vendas = [
        ["Caderno", 10, "2026-08-01"],
        ["Caneta", 5, "2026-08-02"],
    ]

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção ainda não implementada ou inválida.")


if __name__ == "__main__":
    main()
```

Teste executando o arquivo: verifique se o menu aparece e se digitar `0` encerra o programa.

---

## Passo 2 — Listando produtos e classificando desempenho

Agora vamos criar as duas primeiras funções de consulta. Repare que **`listar_produtos` recebe `produtos`**, enquanto **`classificar_desempenho` recebe `vendas`** — cada função trabalha apenas com a sua lista.

**O que foi modificado/adicionado:**
* Adicionadas as funções `listar_produtos(produtos)` e `classificar_desempenho(vendas)` acima de `main()`.
* Na função `main()`, adicionados os `elif` para as opções `"1"` e `"5"`.

```python
# ... (mostrar_menu continua igual)

# NOVO: função para exibir o catálogo
def listar_produtos(produtos):
    print("\n--- Catálogo de Produtos ---")
    for produto in produtos:
        print(f"- {produto[0]} | R$ {produto[1]:.2f}")


# NOVO: função para consultar o histórico de vendas
def classificar_desempenho(vendas):
    print("\n--- Desempenho de Vendas ---")
    nome = input("Digite o nome do produto: ").strip()
    total_vendido = 0

    for venda in vendas:
        if venda[0].lower() == nome.lower():
            total_vendido += venda[1]

    if total_vendido == 0:
        print("Sem histórico.")
    elif total_vendido >= 10:
        print(f"{nome}: Alto desempenho ({total_vendido} unidades vendidas).")
    else:
        print(f"{nome}: Desempenho regular ({total_vendido} unidades vendidas).")


def main():
    produtos = [
        ["Caderno", 18.50],
        ["Caneta", 4.50],
        ["Lápis", 1.50],
    ]

    vendas = [
        ["Caderno", 10, "2026-08-01"],
        ["Caneta", 5, "2026-08-02"],
    ]

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":                                # NOVO
            listar_produtos(produtos)                   # NOVO
        elif opcao == "5":                              # NOVO
            classificar_desempenho(vendas)              # NOVO
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção ainda não implementada ou inválida.")
```

---

## Passo 3 — Persistência de produtos (`produtos.csv`)

Até aqui, se o programa for fechado, qualquer alteração em `produtos` se perde porque tudo está apenas na memória RAM. Vamos resolver isso gravando e lendo o arquivo `produtos.csv`.

**O que foi modificado/adicionado:**
* Adicionado `import os` no topo do arquivo (para verificar se o `.csv` já existe com `os.path.exists`).
* Criadas as funções `salvar_produtos(produtos)` e `carregar_produtos(produtos_padrao)`.
* Na função `main()`, substituída a lista fixa pela chamada `produtos = carregar_produtos(produtos_padrao)`. Se `produtos.csv` ainda não existir, a função cria o arquivo inicial automaticamente.

```python
import os  # NOVO: biblioteca nativa para checar se o arquivo existe


# NOVO: grava a lista produtos no arquivo produtos.csv
def salvar_produtos(produtos):
    with open("produtos.csv", "w", encoding="utf-8") as arquivo:
        for produto in produtos:
            arquivo.write(f"{produto[0]};{produto[1]:.2f}\n")


# NOVO: lê produtos.csv na abertura ou cria o arquivo inicial
def carregar_produtos(produtos_padrao):
    if not os.path.exists("produtos.csv"):
        salvar_produtos(produtos_padrao)
        return produtos_padrao

    produtos = []
    with open("produtos.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                partes = linha.split(";")
                nome = partes[0]
                preco = float(partes[1])
                produtos.append([nome, preco])
    return produtos
```

E dentro de `main()`, altere o início da função para usar `carregar_produtos`:

```python
def main():
    produtos_padrao = [                                 # MODIFICADO
        ["Caderno", 18.50],
        ["Caneta", 4.50],
        ["Lápis", 1.50],
    ]
    produtos = carregar_produtos(produtos_padrao)       # NOVO

    vendas = [
        ["Caderno", 10, "2026-08-01"],
        ["Caneta", 5, "2026-08-02"],
    ]
    # ... (o while True continua igual)
```

Rode o programa uma vez e confira na barra lateral do VS Code que o arquivo `produtos.csv` foi criado!

---

## Passo 4 — Alterando produtos (`alterar_produto`)

Agora vamos implementar a opção `2 - Alterar produto`. Ela precisa:
1. Localizar o produto pelo nome (avisar e sair se não existir).
2. Pedir o novo nome (se o usuário apertar Enter sem digitar nada, mantém o nome atual).
3. Pedir o novo preço e validar se é um número válido e `>= 0`.
4. Atualizar a lista em memória e chamar `salvar_produtos(produtos)`.

**O que foi modificado/adicionado:**
* Criada a função `alterar_produto(produtos)`.
* Na função `main()`, adicionado o `elif opcao == "2":` chamando `alterar_produto(produtos)`.

```python
# NOVO: localiza, valida e altera um produto em memória e no CSV
def alterar_produto(produtos):
    print("\n--- Alterar Produto ---")
    nome_busca = input("Nome do produto que deseja alterar: ").strip()

    produto_encontrado = None
    for produto in produtos:
        if produto[0].lower() == nome_busca.lower():
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print("Produto não encontrado no catálogo.")
        return

    novo_nome = input(f"Novo nome (Enter para manter '{produto_encontrado[0]}'): ").strip()
    if novo_nome == "":
        novo_nome = produto_encontrado[0]

    preco_texto = input("Novo preço: ").strip().replace(",", ".")
    try:
        novo_preco = float(preco_texto)
    except ValueError:
        print("Erro: o preço precisa ser um número válido.")
        return

    if novo_preco < 0:
        print("Erro: o preço não pode ser negativo.")
        return

    produto_encontrado[0] = novo_nome
    produto_encontrado[1] = novo_preco
    salvar_produtos(produtos)
    print("Produto alterado e salvo com sucesso!")
```

Na função `main()`, ligue a opção `"2"` ao menu:

```python
        if opcao == "1":
            listar_produtos(produtos)
        elif opcao == "2":                              # NOVO
            alterar_produto(produtos)                   # NOVO
        elif opcao == "5":
            classificar_desempenho(vendas)
```

---

## Passo 5 — Persistência de vendas (`vendas.csv`)

Seguindo exatamente o mesmo padrão de `produtos.csv`, vamos salvar e carregar o histórico em `vendas.csv`.

**O que foi modificado/adicionado:**
* Criadas as funções `salvar_vendas(vendas)` e `carregar_vendas(vendas_padrao)`.
* Na função `main()`, substituída a lista fixa pela chamada `vendas = carregar_vendas(vendas_padrao)`.

```python
# NOVO: grava a lista vendas no arquivo vendas.csv
def salvar_vendas(vendas):
    with open("vendas.csv", "w", encoding="utf-8") as arquivo:
        for venda in vendas:
            arquivo.write(f"{venda[0]};{venda[1]};{venda[2]}\n")


# NOVO: lê vendas.csv na abertura ou cria o arquivo inicial
def carregar_vendas(vendas_padrao):
    if not os.path.exists("vendas.csv"):
        salvar_vendas(vendas_padrao)
        return vendas_padrao

    vendas = []
    with open("vendas.csv", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                partes = linha.split(";")
                produto = partes[0]
                quantidade = int(partes[1])
                data = partes[2]
                vendas.append([produto, quantidade, data])
    return vendas
```

Atualize o início de `main()`:

```python
    vendas_padrao = [                                   # MODIFICADO
        ["Caderno", 10, "2026-08-01"],
        ["Caneta", 5, "2026-08-02"],
    ]
    vendas = carregar_vendas(vendas_padrao)             # NOVO
```

---

## Passo 6 — Registrando uma venda (`registrar_venda`)

Para registrar uma venda com segurança, a função precisa **receber as duas listas (`produtos` e `vendas`)**: ela consulta `produtos` para confirmar que o item existe no catálogo e, só então, grava a venda em `vendas` e em `vendas.csv`.

**O que foi modificado/adicionado:**
* Criada a função `registrar_venda(produtos, vendas)`.
* Na função `main()`, adicionado o `elif opcao == "3":` chamando `registrar_venda(produtos, vendas)`.

```python
# NOVO: valida produto e quantidade antes de registrar em vendas e salvar no CSV
def registrar_venda(produtos, vendas):
    print("\n--- Registrar Venda ---")
    nome_produto = input("Nome do produto vendido: ").strip()

    produto_existe = False
    nome_oficial = ""
    for produto in produtos:
        if produto[0].lower() == nome_produto.lower():
            produto_existe = True
            nome_oficial = produto[0]
            break

    if not produto_existe:
        print("Erro: produto não encontrado no catálogo.")
        return

    qtd_texto = input("Quantidade vendida: ").strip()
    try:
        quantidade = int(qtd_texto)
    except ValueError:
        print("Erro: a quantidade precisa ser um número inteiro.")
        return

    if quantidade <= 0:
        print("Erro: a quantidade precisa ser maior que zero.")
        return

    data = input("Data da venda (ex: 2026-08-15): ").strip()
    if data == "":
        print("Erro: a data não pode ficar vazia.")
        return

    vendas.append([nome_oficial, quantidade, data])
    salvar_vendas(vendas)
    print("Venda registrada e salva com sucesso!")
```

Na função `main()`, adicione a opção `"3"`:

```python
        elif opcao == "2":
            alterar_produto(produtos)
        elif opcao == "3":                              # NOVO
            registrar_venda(produtos, vendas)           # NOVO
        elif opcao == "5":
            classificar_desempenho(vendas)
```

---

## Passo 7 — Cancelando uma venda (`cancelar_venda`)

Por fim, vamos permitir corrigir vendas lançadas por engano exibindo os registros numerados na tela (`1`, `2`, `3`...), validando a escolha do usuário, removendo o item da lista `vendas` e regravando `vendas.csv`.

**O que foi modificado/adicionado:**
* Criada a função `cancelar_venda(vendas)`.
* Na função `main()`, adicionado o `elif opcao == "4":` chamando `cancelar_venda(vendas)`.

```python
# NOVO: exibe vendas numeradas, valida o índice, remove da lista e salva o CSV
def cancelar_venda(vendas):
    print("\n--- Cancelar Venda ---")
    if len(vendas) == 0:
        print("Nenhuma venda registrada para cancelar.")
        return

    for i in range(len(vendas)):
        venda = vendas[i]
        print(f"{i + 1} - {venda[0]} | Qtd: {venda[1]} | Data: {venda[2]}")

    escolha_texto = input("Digite o número da venda para cancelar: ").strip()
    try:
        numero = int(escolha_texto)
    except ValueError:
        print("Erro: digite um número válido.")
        return

    if numero < 1 or numero > len(vendas):
        print("Erro: número de registro inexistente.")
        return

    removida = vendas.pop(numero - 1)
    salvar_vendas(vendas)
    print(f"Venda de '{removida[0]}' ({removida[1]} un.) cancelada com sucesso!")
```

Na função `main()`, adicione a opção `"4"`:

```python
        elif opcao == "3":
            registrar_venda(produtos, vendas)
        elif opcao == "4":                              # NOVO
            cancelar_venda(vendas)                      # NOVO
        elif opcao == "5":
            classificar_desempenho(vendas)
```

---

## Passo 8 — Roteiro de Testes Finais

Com todas as etapas prontas, execute `papelaria.py` e valide cada cenário abaixo:

1. **Alteração de produto (Aula 3):**
   * Altere o preço de um produto existente para um valor válido (ex.: `19.90`).
   * Tente alterar um produto inexistente e verifique a mensagem de erro.
   * Tente informar um preço negativo ou texto no preço e verifique se o sistema bloqueia.
2. **Registro e cancelamento de vendas (Aula 4):**
   * Registre uma venda de um produto que está no catálogo com quantidade positiva.
   * Tente registrar uma venda de um produto que não existe no catálogo (deve recusar).
   * Cancele um registro existente pelo número e tente cancelar um número inválido (ex.: `99`).
3. **Teste de persistência (fechar e reabrir):**
   * Escolha `0 - Sair` para encerrar o programa.
   * Abra `produtos.csv` e `vendas.csv` no VS Code para conferir os dados salvos.
   * Execute `papelaria.py` novamente e liste os produtos/consulte o desempenho: todas as alterações, registros novos e cancelamentos devem continuar valendo.
