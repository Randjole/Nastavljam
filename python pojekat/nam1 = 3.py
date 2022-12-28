import random


komp = random.randint(1,100)


def get_inputs():
    ime = input('Unesi svoje ime: ')
    pol = input('Unesi pol M/Z: ')
    if pol not in ['M', 'Z']:
        return None, None

    return ime, pol


def check_inputs(ime, pol):
    if pol == 'M':
        print('Desi Care', ime)
        pol = 'Care'

    elif pol == 'Z':
        print('Desi Carice', ime)
        pol = 'Carice'

    else:
        print('Sta si ti druzee??')

    return ime, pol


def get_number(ime):
    tvoj = int(input('Ukucaj broj: '))
    print('Broj kompa je', komp)
    print('A tvoj', ime, tvoj, 'sto znaci')
    return tvoj


def check_number(tvoj, pol):
    if tvoj > 100 or tvoj < 1:
        print('Hej', pol, 'rekli smo samo od 1 do 100')

    else:
        if tvoj < komp:
            print('E GLUPANE GLUPI')

        elif tvoj == komp:
            print('NEMA POBEDNIKA', pol)

        else:
            print('Bravo', pol, 'ti si pobedio')


while True: # Do this forevaaa
    ime, pol = get_inputs()
    if pol is not None:
        break # Well, almost forever


ime, pol = check_inputs(ime, pol)
tvoj = get_number(ime)
check_number(tvoj, pol)