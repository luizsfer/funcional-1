# -*- coding: utf-8 -*-

### Luiz Ferreira
### Python funcional 1
### Alura

## Codigo para terminal

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


def funcao_pep570 (apenas_posicional1, apenas_posicional2=None, /, *posicional, **relacional):
    print(apenas_posicional1)
    print(apenas_posicional2)
    print(posicional)
    print(relacional)

def funcao_pep570_padrao (apenas_posicional, /, padrao, *, somar):
    print(apenas_posicional)
    print(padrao)
    print(somar)


from estoque import operacoes

def main ():
    """
    Função principal
    """
    print(operacoes.somar(1,3,4,5))
    # print(operacoes.dobrarValor(1,3,4,5))
    # print(operacoes.dobrarValor(operacoes.somar(1,3,4,5)))
    print(operacoes.dobrarValor(sum((1,3,4,5))))

if __name__ == "__main__":
    """
    Ação que permite execução do módulo principal
    """
    main()


