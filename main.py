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