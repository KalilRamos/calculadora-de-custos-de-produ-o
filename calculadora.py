# Quantidade de insumos necessários para cada produto
insumos_por_produto = {
    "Produto A": {"Insumo 1": 25, "Insumo 2": 15, "Insumo 3": 40},
    "Produto B": {"Insumo 1": 30, "Insumo 2": 25, "Insumo 3": 20},
    "Produto C": {"Insumo 1": 20, "Insumo 2": 35, "Insumo 3": 30}
}

# Custos por insumos
custos_insumos = {
    "Insumo 1": 10.00,
    "Insumo 2": 15.00,
    "Insumo 3": 20.00}

# Produção de cada produto
producao_prevista = {
    "Produto A": 1200,
    "Produto B": 900,
    "Produto C": 1500}

# calcular a quantidade total de insumos necessários
def calcular_quantidade_total(insumos_por_produto, producao_prevista):

    quantidade_total = {"Insumo 1": 0, "Insumo 2": 0, "Insumo 3": 0}

    # Loop para calcular a quantidade total de cada insumo
    for produto, insumos in insumos_por_produto.items():
        for insumo, quantidade in insumos.items():
            quantidade_total[insumo] += quantidade * producao_prevista[produto]
    return quantidade_total

# Calcular o custo total de produção
def calcular_custo_total(quantidade_total, custos_insumos):
    custo_total = 0  # Inicializa o custo total

    # Loop para calcular o custo total
    for insumo, quantidade in quantidade_total.items():
        custo_total += quantidade * custos_insumos[insumo]

    return custo_total

# Calcula a quantidade total de insumos necessários
quantidade_total_insumos = calcular_quantidade_total(insumos_por_produto, producao_prevista)

# Calcula o custo total de produção com os custos atuais
custo_total_atual = calcular_custo_total(quantidade_total_insumos, custos_insumos)


# Dicionário com o valor atualizado
custos_insumos_alterado = {
    "Insumo 1": 12.00,  # Novo valor do Insumo 1
    "Insumo 2": custos_insumos["Insumo 2"],
    "Insumo 3": custos_insumos["Insumo 3"] 
}

# Calcula o custo total com o novo valor do Insumo 1
custo_total_alterado = calcular_custo_total(quantidade_total_insumos, custos_insumos_alterado)

# Impacto do aumento custo total
impacto_custo = custo_total_alterado - custo_total_atual

# Exibe os resultados
print("Quantidade total necessária de cada insumo (kg):")
for insumo, quantidade in quantidade_total_insumos.items():
    print(f" => {insumo}: {quantidade} kg")

print("\nCusto total de produção (R$):", custo_total_atual)
print("\nCusto total de produção com Insumo 1 a R$ 12,00/kg (R$):", custo_total_alterado)
print("\nImpacto do aumento do Insumo 1 (R$):", impacto_custo)



# def calcular_custo_total_alternativo(quantidade_total, custos_insumos):
#   return sum(quantidade_total[insumo] * custos_insumos[insumo] for insumo in quantidade_total)

# Acho que dá para melhorar a eficiência, mas funciona por enquanto
