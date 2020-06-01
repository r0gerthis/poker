import random, time
TIME_TO_READ_SLEEP = 1
ORDER_SLEEP = 0.5

def print_sleep(text, sleep):
    print(text)
    time.sleep(sleep)

iedereen = [
    'Johan',
    'Laurens',
    'Joost',
    'Ruud',
    'Antoon',
    'Mark',
    'Koen v A',
    'Devi',
    'Ralf',
    'Wester'
]
tafelbazen = [
    'Douwe',
    'Rogier'
]
tafel_1 = []
tafel_2 = []
totaalinschr = len(iedereen)+len(tafelbazen)

print_sleep('\nw00t, TAFEL INDELING MACHINE\n', TIME_TO_READ_SLEEP)
print_sleep(f'Totaal aantal inschrijvingen: {totaalinschr}', TIME_TO_READ_SLEEP)
print_sleep('Deelnemers nu zijn:', TIME_TO_READ_SLEEP)

for x in iedereen:
    print_sleep(f' - {x}',ORDER_SLEEP)
for x in tafelbazen:
    print_sleep(f' - {x} (tafel baas)', ORDER_SLEEP)

random.shuffle(iedereen)

i = 0
print_sleep('\n',TIME_TO_READ_SLEEP)
print_sleep('Tafels indelen (en iedereen lekker husselen):', TIME_TO_READ_SLEEP)


while len(iedereen):
    j = random.randrange(0, len(iedereen))
    wie = iedereen.pop(j)
    if i % 2 == 0:
        tafel_1.append(wie)
        print_sleep(f'-> {wie} is ingedeeld op tafel 1', ORDER_SLEEP)
    else:
        tafel_2.append(wie)
        print_sleep(f'-> {wie} is ingedeeld op tafel 2', ORDER_SLEEP)
    i += 1

tfb1 = tafelbazen.pop(0)
tfb2 = tafelbazen.pop(0)
print_sleep(f'-> {tfb1} is ingedeeld op tafel 2 als tafelbaas', ORDER_SLEEP)
tafel_2.append(tfb1)
print_sleep(f'-> {tfb2} is ingedeeld op tafel 1 als tafelbaas', ORDER_SLEEP)
tafel_1.append(tfb2)


print_sleep('\n', TIME_TO_READ_SLEEP)

totaal_tfl1 = len(tafel_1)
totaal_tfl2 = len(tafel_2)
print_sleep(f'\nTafel 1 spelers ({totaal_tfl1}):', TIME_TO_READ_SLEEP)
print(*tafel_1, sep = ", ")  
time.sleep(TIME_TO_READ_SLEEP)
print_sleep(f'\nTafel 2 spelers ({totaal_tfl2}):', TIME_TO_READ_SLEEP)
print(*tafel_2, sep = ", ")  

print_sleep('\n',TIME_TO_READ_SLEEP)

print_sleep('VEEL SUCCESS ALLEMAAL!\n', TIME_TO_READ_SLEEP)