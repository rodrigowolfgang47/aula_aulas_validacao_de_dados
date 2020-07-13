import re

class Telefone:

    def __init__(self, telephone):
        if len(self.telephone_validator(telephone)) > 0:
            self.number = self.telephone_validator(telephone)

        else:
            raise ValueError('Ivalid phone number')

    def telephone_validator(self, telephone):
        pattern = '([0-9]{2,3})([0-9]{2})?([0-9]{4,5})([0-9]{5})'
        respose = re.findall(pattern, telephone)
        if respose:
            return respose
        else:
            False



phone = '11948719660'

pri_number = Telefone(phone)

print(pri_number.number)