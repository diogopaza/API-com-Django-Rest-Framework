import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    resposta =cpf.validate(numero_cpf)  
    return resposta

def celular_valido(numero_celular):
    """verifica se o celular e valido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,  numero_celular)
    return resposta 