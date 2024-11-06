def custom_write(file_name, strings, strings_positions = None):
    if strings_positions is None:
        strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, str_ in enumerate(strings, 1):
            pos = file.tell()
            file.write(str_ + '\n')
            strings_positions[(index, pos)] = str_
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
