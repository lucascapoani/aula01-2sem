"""
Fa�a um algoritmo que leia o nome de um produto, seu pre�o e sua quantidade,
armazene isso em 3 listas diferentes.

- Crie uma fun��o que imprima todos os elementos destas listas.
- Crie uma fun��o que receba a posi��o do elemento como par�metro.
    e imprima os elementos destas listas pelo par�metro.
"""

lista_produto = ["Coca Cola", "Pepsi Cola" , "Fanta Cola"]
lista_preco = [4.4, 3.8, 5.2]
lista_quantidade = [11, 22, 33]

def funcao_imprimir():
    for i in range(len(lista_produto)):
        print(f"{i} Produto: {lista_produto[i]}     Pre�o: {lista_preco[i]}    Qt:. {lista_quantidade[i]}") 

while True:
    
    produto = input("Produto: ").upper()

    if produto == 'FIM':
        break

    preco = float(input("Pre�o: "))
    quantidade = int(input("Quantidade: "))

    lista_produto.append(produto)
    lista_preco.append(preco)
    lista_quantidade.append(quantidade)

funcao_imprimir()

    

