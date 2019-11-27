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
    # variavel = [nome, preco, cores]
    # valores_mutaveis = ["Caderno", 12.00, ["azul", "vermelho", "cinza"]]
    # valores_imutaveis = ("Caderno", 12.00, ["azul", "vermelho", "cinza"])
    # Visualizando variáveis - Mesmos valores
    # print("Mutaveis: ", valores_mutaveis[2])
    # print("Imutaveis: ", valores_imutaveis[2])
    # Alterando valores - observamos um erro
    # valores_mutaveis[1] = 15
    # valores_imutaveis[1] = 15
    # TypeError: 'tuple' object does not support item assignment
    # Lista dentro de uma tupla, é mutável ou imutável?
    # valores_imutaveis[2].append("roxo")
    # print("Após append: ", valores_imutaveis)
    # Tentemos mudar o valor para os iniciais, vejamos o que acontece
    # valores_imutaveis[2] = ["azul", "vermelho", "cinza"]
    # Apesar de ser uma lista, uma atribuição de valores diretamente não é possível. Pois não podemos alterar a referência do objeto gravado na memória

    # First-Class Functions e High-Order Functions
    # Já usamos alguns de seus conceitos nas atividades anteriores
    # Uma linguagem que possui First-Class Functions é capaz de:
    # - Utilizar funções como parametro
    #   - Quando aplicamos um desconto tendo seu segundo parametro a chamada da função 
    #       valorDesconto: print(valorDescontoAplicado(100, valorDesconto(100, 0.10)))
    # - Retornar funções como valores
    #   - Quando utilizamos a chamada da função dobrar valor:
    #       print(operacoes.dobrarValor(1,3,4,5))
    #       note que o retorna dessa função é a chamada de uma outra função, dessa vez, built-in, função sum()
    #       return sum(args)*2
    # - Pode ser atribuído a variáveis
    #   - Da mesma forma com que imprimimos os resultados de chamada de função diretamente, podemos atribuí-los a uma variável
    valor = dobrarValor(2,3,4)
    print(valor)
    # - Pode ser armazenado em estruturas de dados
    #   - Podemos adicionar uma chamada de função dentro de uma coleção qualquer, como, por exemplo, uma dict
    valores = {
        "numeros": [1,2,3,4],
        "dobro": dobrarValor(valores["numeros"])
    }
    print(valores)
    print(type(valores["dobro"]))
if __name__ == "__main__":
    """
    Ação que permite execução do módulo principal
    """
    main()

