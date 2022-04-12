class Telefon:
    counter = 0

    def __init__(self, numar):
        self.numar = numar
        Telefon.counter += 1

    def apelare(self, numar_apelat):
        mesaj = f'Apelati {numar_apelat} folosind propriul numar'
        return mesaj


class TelefonFix(Telefon):
    last_SN = 0

    def __init__(self, numar):
        super().__init__(numar)
        TelefonFix.last_SN += 1
        self.SN = f'TF - {TelefonFix.last_SN}'

class TelefonMobil(Telefon):
    last_SN = 0

    def __init__(self, numar):
        super().__init__(numar)
        TelefonMobil.last_SN += 1
        self.SN = f'TF - {TelefonMobil.last_SN}'

print(f'Numarul total de deviceuri create: {Telefon.counter}')
t1 = TelefonFix('1234')
t2 = TelefonFix('5678')

t3 = TelefonMobil('0000')
t4 = TelefonMobil('1111')
print(f'Numarul total de deviceuri create: {Telefon.counter}')
print(t4.SN)