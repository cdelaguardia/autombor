import pyperclip, re

passLowerCase = re.compile(r'''(
    [a-z]
    )''', re.VERBOSE)

passUpperCase = re.compile(r'''(
    [A-Z]
    )''', re.VERBOSE)

passNumber = re.compile(r'''(
    [0-9]
    )''', re.VERBOSE)

passChar = re.compile(r'''(
    [\W]
    )''', re.VERBOSE)

password =str(pyperclip.paste())

lower=passLowerCase.search(password)
upper=passUpperCase.search(password)
number=passNumber.search(password)
char=passChar.search(password)

if lower !=None and upper!=None and number !=None and char != None:
    print('pass segura')
else:
    print('pass no segura')
