import pyperclip, re

def validate(fecha):
    day = int(fecha[:2])
    #print(day)
    month = int(fecha[3:5])
    #print(month)
    year = int(fecha [6:10])
    #print(year)
    if year < 1000 or year > 2999:
        return False

    if month < 1 or month > 12:
        return False

    mes30 = [4, 6, 11, 9]
    mes31 = [1, 3, 5, 7, 8, 10, 12]

    if (month in mes30) and (day < 1 or day > 30):
        return False
    elif (month in mes31) and (day < 1 or day > 31):
        return False
    elif (year%4 != 0) and (day < 1 or day > 28):
        return False
    elif (year%4 == 0) and (year%100 != 0) and (day < 1 or day > 29) :
        return False
    elif (year%4 == 0) and (year%100 == 0) and (year%400 != 0) and (day < 1 or day > 28) :
        return False
    elif (year%4 == 0) and (year%100 == 0) and (year%400 == 0) and (day < 1 or day > 29):
        return False
    else:
        return True




dateRegex = re.compile(r'''(
    (\d{2})
    (\/)
    (\d{2})
    (\/)
    (\d{4})
    )''', re.VERBOSE)


text =str(pyperclip.paste())

groups = dateRegex.search(text)
print(groups)

if groups != None:

    date = groups[0]

    print(date)


    if validate(date):
        print(f'La fecha identificada es {date}')
    else:
        print('Se encontro coincidencia pero no es una fecha valida')

else:
    print('No se encontro coincidencia con el formato establecido. No hay fecha en el texto')


#pyperclip.copy(str(matches))
