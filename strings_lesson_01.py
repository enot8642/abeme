student_name_1 = 'ehor'
print(student_name_1)

print(id('Bob'))

emoji = """

🏁
\000U+1F3C1
"""
print(emoji)

print(chr(555))
print(ord('ꓥ'))



template = 'Вiтаю тебе, {first_name} {last_name}!'
result = template.format(first_name=user_first_name, last_name=user_last_name)
