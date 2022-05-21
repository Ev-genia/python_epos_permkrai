"""Заменить все буквы "х" на "у" в исходной строке ("asdxfghyxyx")
без использования дополнительной строки."""

str = 'asdxfghyxyx'
i = 0
while i < len(str):
    if str[i] == 'x':
        str = str[:i] + 'y' + str[i + 1:]
    i += 1
print('str: ', str)