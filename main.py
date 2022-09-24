# Python Brasil: validação de dados no padrão nacional.

# 22/09/2022

from cpf_cnpj import Documento
from TelefonesBr import TelefonesBr
from validate_docbr import CNPJ
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

''' Validando CPF e CNPJ'''
exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"
cnpj = CNPJ()
print(cnpj.validate(exemplo_cnpj))

documento = Documento.cria_documento(exemplo_cpf)
print(documento)


''' Validando Telefone'''
Telefone = "551226481234"
telefone_objeto = TelefonesBr(Telefone)
print(telefone_objeto)

'''Data cadastro'''
cadastro = DatasBr()
print(cadastro)

''' Validando Cep'''
cep = "01001000"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)


bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)