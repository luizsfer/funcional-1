# -*- coding: utf-8 -*-

# Conhecendo e entendendo o conceito de funções puras
# Toda função que não altera o valor de entrada ou qualquer dado que exista fora do escopo da função

def descontoDezPorcento(valor):
    return valor*0.10

def valorDesconto (valor, desconto):
    return (valor*desconto)

def valorDescontoAplicado (valor, valorDesconto):
    return valor-valorDesconto

def valoresMaiores(valor):
    return valor if (valor >= 200) else ''