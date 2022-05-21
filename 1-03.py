"""Заменить в строке "asdxfghyxyx" все буквы 'х' на 'у'"""

src = 'asdxfghyxyx'
rez = ''
for c in src:
    if c == 'x':
        rez = rez + 'y'
    else:
        rez = rez + c
