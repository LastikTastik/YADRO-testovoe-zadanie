def search_word(name_file,name_word):
    try:
        with open(name_file,'r') as file:
            strings=file.read().splitlines()
            spisok_stroke=[]
            for stroke in strings:
                if name_word.lower() in stroke.lower():
                   spisok_stroke.append(stroke)
            if len(spisok_stroke)>0:
                print("Найденные строки:")
                print(*spisok_stroke,sep='\n')
            else:
                print(f"Строк со словом {name_word} не нашлось!")
    except FileNotFoundError:
        print(f"Файл '{name_file}' не найден!")


print("Введите имя файла для чтения")
name_file=input()

print("Введите слово, которое нужно найти в файле")
name_word=input()
search_word(name_file,name_word)

