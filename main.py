import re

file = open("MOCK_DATA.txt", encoding="utf-8")
content = file.read()

while True:
    cmd = input("\tМеню:\n1 - Считать имена и фамилии\n2 - Считать все емайлы\n3 - Считать названия файлов\n\
4 - Считать цвета\n5 - Выход\n")
    if cmd == '1':
        f2 = open("names.txt", "w")
        names = re.findall(r"^\b[A-Za-z'-]*\s[A-Za-z'-]*(?:\s[A-Z][a-z'-]*|\s|\.)", content, re.MULTILINE)
        for name in names:
            f2.write(name + "\n")
        print("Имена записаны в файле names.txt")
        f2.close()

    elif cmd == '2':
        f2 = open("emails.txt", "w")
        emails = re.findall(r"\b[a-z\d]*@[a-z\d\.-]*", content)
        for email in emails:
            f2.write(email + "\n")
        print("Эл. почты записаны в файле emails.txt")
        f2.close()
    elif cmd == '3':
        f2 = open("files.txt", "w")
        files = re.findall(r"\s\b[A-Za-z]*\.[a-z\d]*\b", content)
        for f in files:
            f2.write(f.strip() + "\n")
        print("Имена файлов записаны в файле emails.txt")
        f2.close()
    elif cmd == '4':
        f2 = open("colors.txt", "w")
        colors = re.findall(r"#[\da-zA-Z]*", content)
        for color in colors:
            f2.write(color + "\n")
        print("Цвета записаны в файле colors.txt")
        f2.close()
    elif cmd == '5':
        break
    else:
        print("Ошибка. Попробуйте снова!")

file.close()
