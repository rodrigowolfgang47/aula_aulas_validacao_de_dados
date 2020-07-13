from validate_docbr import CPF, CNPJ
class Cpf_Cpf:
    def __init__(self, document, tipo_documento):
        doc = str(document)
        if self.tipo_de_docuemto == "cpf":
            if self.__valid_cpf(doc):
                self.__cpf = doc
            else:
                raise ValueError('Invalid CPF, please try again!')
        elif tipo_documento == "cnpj":
            if self.__valid_cnpj(doc):
                self.__cnpj = doc
            else:
                raise ValueError('Invalid Cnpj, please try again!')
        else:
            raise ValueError('Invalid document')

    @staticmethod
    def __valid_cpf(document):
            valid = CPF()
            return valid.validate(document)
        else:
            raise ValueError('Ivalid number of digits')

    def cpf_formated(self):
        mask = CPF()
        return mask.mask(self.__cpf)

    def cnpj_formated(self):
        mask = CNPJ()
        return mask.mask(self.__cnpj)

    def __valid_cnpj(self, document):
        if len(document) == 14:
            valid = CNPJ()
            return valid.validate(document)
        else:
            raise ValueError("Invalid Cnpj!")

    def __str__(self):
        if self.tipo_de_docuemto == 'cnpj':
            return self.cnpj_formated()
        else:
            return self.cpf_formated()
