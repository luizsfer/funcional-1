# -*- coding: utf-8 -*-

### Luiz Ferreira
### Python funcional 1
### Alura

## Codigo para terminal
'''
def funcao():
    pass

# funcao()

def funcao_retorno():
    return "Essa função tem um retorno"

# funcao_retorno()

def funcao_retorno_docstring():
    """
    Essa função tem documentação
    """
    return "Essa função tem um retorno"

# funcao_retorno_docstring.__doc__

def funcao_com_parametros(parametro1, parametro2):
    """
    Essa função tem documentação
    """
    return parametro1 + " " + parametro2

# funcao_com_parametros("Olá", "Mundo")
# funcao_com_parametros(parametro2 = "Mundo", parametro1 = "Olá")

def funcao_com_args(parametro1, *args):
    """
    Essa função tem documentação
    """
    print(parametro1)
    for arg in args:
        print(arg)

# funcao_com_args("contando")
# funcao_com_args("contando",1,2,3,4,5)

def funcao_com_kwargs(parametro1, **kwargs):
    """
    Essa função tem documentação
    """
    retirar = kwargs.get('retirar')

    print(parametro1)
    if retirar:
        parametro1 -= retirar 
    print(parametro1)

# funcao_com_kwargs(100)
# funcao_com_kwargs(100, retirar=20)

def funcao_com_args_kwargs(*args, **kwargs):
    """
    Essa função tem documentação
    """
    total = 0
    retirar = kwargs.get('retirar')

    for arg in args:
        total += arg

    print("Total: ", total)

    if retirar:
        total -= retirar
        print("Total com retirar: ", total)

# funcao_com_args_kwargs(10,20,30)
# funcao_com_args_kwargs(10,20,30,retirar=15)
'''

from estoque.gerenciamento import *
from estoque.operacoes import *
# Era built-in em Python2 porém passou a ser parte do pacote functools em Python3
# from functools import reduce

def main ():
    """
    Função principal
    """
    # print(operacoes.somar(1,3,4,5))
    # print(operacoes.dobrarValor(1,3,4,5))
    # print(operacoes.dobrarValor(operacoes.somar(1,3,4,5)))
    # print(operacoes.dobrarValor(sum((1,3,4,5))))

    # Aplicando valores de desconto - função como parâmetro de outra função
    # print(valorDescontoAplicado(100, valorDesconto(100, 0.10)))
    
    # Aplicando função map
    # print(list(map(descontoDezPorcento, (100,200,300))))

    # Aplicando função map para dois argumentos
    # print(list(map(valorDesconto, (100,200,300), (0.10,0.15,0.20))))

    # valores = (100, 150, 200, 300)
    # descontos = (0.10, 0.15, 0.20, 0.30)

    # Grande e confuso? Vamos simplificar nas próximas aulas, não se preocupe
    # print(list(map(valorDescontoAplicado, valores, list(map(valorDesconto, valores,descontos)))))

    # print(reduce(somar,(100,200,300)))
    # print(reduce(somar,valores))

    # Podemos somar as duas funções para obtermos um resultado mais específico, assim como as demais
    # print(reduce(somar, list(map(valorDesconto, valores, descontos))))

    # Função filter
    # print(list(filter(valoresMaiores, valores)))

    # Função filter para valores de descontos
    # Não se assuste, isso ficará mais fácil
    # print(list(map(descontoDezPorcento, list(filter(valoresMaiores, valores)))))

    # Imutabilidade
    # produtos_estoque_abril = [('caderno', 10), ('caneta', 20), ('borracha', 15)]
    # produtos_estoque_maio = produtos_estoque_abril
    # print("Estoque em abril: ", produtos_estoque_abril)
    # print("Estoque em maio: ", produtos_estoque_maio)
    # produtos_estoque_maio += [('apontador', 12), ('lapiseira', 10)]
    # print("Estoque em abril: ", produtos_estoque_abril)
    # print("Estoque em maio: ", produtos_estoque_maio)

    # produtos_estoque_abril = (('caderno', 10), ('caneta', 20), ('borracha', 15))
    # produtos_estoque_maio = produtos_estoque_abril
    # print(type(produtos_estoque_abril))
    # print(type(produtos_estoque_maio))

    produtos_estoque_abril = (('caderno', 10), ('caneta', 20), ('borracha', 15))
    produtos_estoque_maio = produtos_estoque_abril
    print("Estoque em abril: ", produtos_estoque_abril)
    print("Estoque em maio: ", produtos_estoque_maio)

    #produtos_estoque_maio += (('apontador', 12), ('lapiseira', 10))
    produtos_estoque_maio = produtos_estoque_maio + (('apontador', 12), ('lapiseira', 10))
    
    print("Estoque em abril: ", produtos_estoque_abril)
    print("Estoque em maio: ", produtos_estoque_maio)

if __name__ == "__main__":
    """
    Ação que permite execução do módulo principal
    """
    main()

