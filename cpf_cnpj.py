from validate_docbr import CPF,CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválido")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
            return self.format()

    def valida(self, documento):
            validador = CPF()
            return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self,documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

class CpfCnpj:
    def __init__(self,documento, tipo_documento):
        self.tipo_documento = tipo_documento
        if self.tipo_documento == "cpf":
            documento = str(documento)
            if self.cpf_eh_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido")
        elif self.tipo_documento == "cnpj":
            documento = str(documento)
            if self.cnpj_e_valido(documento):
                self.cnpj=documento
            else:
                raise ValueError("CNPJ inválido")
        else:
            raise ValueError("Documento inválido")

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.format_cpf()
        elif self.tipo_documento == "cnpj":
            return self.format_cnpj()

    def cpf_eh_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos invalida")

    def format_cpf(self):
        mascara =CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara =CNPJ()
        return mascara.mask(self.cnpj)

    def cnpj_e_valido(self,cnpj):
        if len(cnpj)==14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos inválidos")

