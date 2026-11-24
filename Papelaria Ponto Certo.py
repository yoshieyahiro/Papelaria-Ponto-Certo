import os  # biblioteca nativa para checar se o arquivo existe


# ---------------------------------------------------------------
# MENU
# ---------------------------------------------------------------
def mostrar_menu():
    print("\n=== PAPELARIA PONTO CERTO ===")
    print("1 - Listar produtos")
    print("2 - Alterar produto")
    print("3 - Registrar venda")
    print("4 - Cancelar venda")
    print("5 - Classificar desempenho")
    print("0 - Sair")


# ---------------------------------------------------------------
# CONSULTAS
# ---------------------------------------------------------------
# Exibe o catálogo
def listar_produtos(produtos):
    print("\n--- Catálogo de Produtos ---")
    for produto in produtos:
        print(f"- {produto[0]} | R$ {produto[1]:.2f}")


# Consulta o histórico de vendas
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


# ---------------------------------------------------------------
# PERSISTÊNCIA DE PRODUTOS (produtos.csv)
# ---------------------------------------------------------------
# Grava a lista produtos no arquivo produtos.csv
def salvar_produtos(produtos):
    with open("produtos.csv", "w", encoding="utf-8") as arquivo:
        for produto in produtos:
            arquivo.write(f"{produto[0]};{produto[1]:.2f}\n")


# Lê produtos.csv na abertura ou cria o arquivo inicial
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


# ---------------------------------------------------------------
# ALTERAÇÃO DE PRODUTOS
# ---------------------------------------------------------------
# Localiza, valida e altera um produto em memória e no CSV
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


# ---------------------------------------------------------------
# PERSISTÊNCIA DE VENDAS (vendas.csv)
# ---------------------------------------------------------------
# Grava a lista vendas no arquivo vendas.csv
def salvar_vendas(vendas):
    with open("vendas.csv", "w", encoding="utf-8") as arquivo:
        for venda in vendas:
            arquivo.write(f"{venda[0]};{venda[1]};{venda[2]}\n")


# Lê vendas.csv na abertura ou cria o arquivo inicial
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


# ---------------------------------------------------------------
# REGISTRO DE VENDAS
# ---------------------------------------------------------------
# Valida produto e quantidade antes de registrar em vendas e salvar no CSV
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


# ---------------------------------------------------------------
# CANCELAMENTO DE VENDAS
# ---------------------------------------------------------------
# Exibe vendas numeradas, valida o índice, remove da lista e salva o CSV
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


# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
def main():
    produtos_padrao = [
        ["Caderno", 18.50],
        ["Caneta", 4.50],
        ["Lápis", 1.50],
    ]
    produtos = carregar_produtos(produtos_padrao)

    vendas_padrao = [
        ["Caderno", 10, "2026-08-01"],
        ["Caneta", 5, "2026-08-02"],
    ]
    vendas = carregar_vendas(vendas_padrao)

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_produtos(produtos)
        elif opcao == "2":
            alterar_produto(produtos)
        elif opcao == "3":
            registrar_venda(produtos, vendas)
        elif opcao == "4":
            cancelar_venda(vendas)
        elif opcao == "5":
            classificar_desempenho(vendas)
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção ainda não implementada ou inválida.")


if __name__ == "__main__":
    main()