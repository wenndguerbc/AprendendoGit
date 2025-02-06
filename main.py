""" Script que gera números de CPF válidos 
    seguindo as regras do sistema brasileiro de validação """
from random import randint

nove_digito_cpf= ""
for i in range(9): # Gerando os primeiros 9 digitos do CPF
    nove_digito_cpf += str(randint(0, 9))
    
# Gerando o decimo digito do CPF
contagem_regressiva1 = 10
soma1 = 0
# Fazendo os calculos para gerar o decimo digito
for primeiro_digito in nove_digito_cpf: 
     soma1 += int(primeiro_digito) * contagem_regressiva1
     contagem_regressiva1 -= 1
result = (soma1 * 10) % 11
result_primeiro_digito = result if result <= 9 else 0

# Gerando o decimo-primeiro digito do CPF
dez_digito = nove_digito_cpf + str(result_primeiro_digito)
contagem_regressiva2 = 11
soma2 = 0
# Fazendo os calculos para gerar o decimo-primeiro digito
for segundo_digito in dez_digito: 
     soma2 += int(segundo_digito) * contagem_regressiva2
     contagem_regressiva2 -= 1
result2 = (soma2 * 10) % 11
result_segundo_digito = result2 if result2 <= 9 else 0

# Gerando o CPF com os 11 digitos
cpf_gerado = f"{nove_digito_cpf[0:3]}.{nove_digito_cpf[3:6]}.{nove_digito_cpf[6:]}-\
{result_primeiro_digito}{result_segundo_digito}"
print(f"CPF:{cpf_gerado}")
