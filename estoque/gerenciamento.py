# -*- coding: utf-8 -*-

def descontoDezPorcento(valor):
    return valor*0.10

def valorDesconto (valor, desconto):
    return (valor*desconto)

def valorDescontoAplicado (valor, valorDesconto):
    return valor-valorDesconto

def valoresMaiores(valor):
    return valor if (valor >= 200) else ''