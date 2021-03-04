datatyp = []
ex_datatyp = []
info_datatyp = []

with open('datatyper.txt') as f:
    for rad in f:
        rad = rad.split('|')


        datatyp.append(rad[0].lstrip())
        ex_datatyp.append(rad[1].lstrip())
        info_datatyp.append(rad[2].lstrip())
    for i, t in enumerate(datatyp):

      print('{:<15}{}\n{:<15}{}\n{:<15}{}'.format('Datatyp:', t, 'Exempel:', ex_datatyp[i], 'Förklaring:', info_datatyp[i]))
