listaProdutos = []
def cadastrarProduto(codigo):
   print('Bem Vindo ao Controle de Estoque do Eduardo Da Costa Santos ★')
   print(' O CÓDIGO do produto é : {}'.format(codigo))
   nome = input('Digite o nome do produto:')
   fabricante = input('Digite a Fabricante do produto:')
   valorProduto = float(input('Digite o valor do produto:'))
   dicionarioProduto = {'Código' : codigo,
                        'Nome' : nome,
                        'Fabricante' : fabricante,
                        'Valor': valorProduto}
   listaProdutos.append(dicionarioProduto.copy())

def consultarProduto():
   while True:
       try:
           consultar = int(input('Digite a opção desejada:\n1 - Consultar todos os Produto\n2 - Consultar Produto por código\n3 - Consultar Produto por fabricante\n4 - Retornar\n'))
           if consultar == 1:
               print('Consultar todos os Produtos')
               for produto in  listaProdutos:
                   for key, value in produto.items():
                       print('{} : {}'.format(key, value))
           elif consultar == 2:
               print('Consultar código do Produto')
               entrada = int(input('Digite o código desejado:'))
               for produto in listaProdutos:
                   if(produto['Código'] == entrada):
                       for key, value in produto.items():
                           print('{} : {}'.format(key, value))
           elif consultar == 3:
               print('Consultar o Fabricante')
               entrada = input('Digite o Fabricante desejado:')
               for produto in listaProdutos:
                   if (produto['Fabricante'] == entrada):
                       for key, value in produto.items():
                           print('{} : {}'.format(key, value))
           elif consultar == 4:
               return
           else:
               print('Opção inválida no menu!')
           continue
       except ValueError:
           print('Pare de digitar opção inválida!')

def removerProduto():
   print('Remover Produto')
   entrada = int(input('Digite o código do Produto que deseja remover:'))
   for produto in listaProdutos:
       if (produto['Código'] == entrada):
           listaProdutos.remove(produto)

print('Bem Vindo ao Controle de Estoque do Eduardo Da Costa Santos ★')
acumuladorProdutos = 0
while True:
   try:
       opcao = int(input('Digite a opção desejada:\n1 - Cadastrar Produto\n2 - Consultar Produto\n3 - Remover Produto\n4 - Sair\n'))
       if opcao == 1:
           acumuladorProdutos = acumuladorProdutos + 1
           cadastrarProduto(acumuladorProdutos)
       elif opcao == 2:
           consultarProduto()
       elif opcao == 3:
           removerProduto()
       elif opcao == 4:
           print('Programa finalizado')
           break
       else :
           print('Opção invalida!')
       continue
   except:
       print('Pare de digitar opções inválidas!')
