import sys

def search_word(name_file, name_word):
    try:
        with open(name_file, 'r') as file:
            for stroke in file:
                if name_word.lower() in stroke.lower():
                    print("Найденные строки:")
                    print(stroke.strip())
            else:
                print(f"Строк со словом {name_word} не нашлось!")
    except FileNotFoundError:
        print(f"Ошибка: файл '{name_file}' не найден!")

if len(sys.argv) == 3:
    search_word(sys.argv[1], sys.argv[2])
else:
    print("Использование: python script_hard.py <файл> <слово>")