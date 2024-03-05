import os
def clear_console():
    os.system('cls')
clear_console()

def work_with_phonebook():
    # os.system('cls')
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')

    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(p,last_name))
        elif choice==3:
            add_contact_line(phone_book)
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            remove_contact_line(phone_book)
        elif choice==6:
            write_txt(phone_book, 'phonebook.txt')
        
        choice=show_menu()
    clear_console()








def show_menu():
    print("\nВыберите необходимое действие:\n",
          "1. Отобразить весь справочник\n",
        #   "2. Найти абонента\n",
          "3. Добавить абонента в справочник\n",
        #   "4. Изменить абонента\n",
          "5. Удалить абонента\n",
          "6. Сохранить справочник в текстовом формате\n",
          "7. Закончить работу"),
    choice = int(input())
    return choice


def read_txt(filename): 

    phone_book=[]
    fields=['Фамилия','Имя','Телефон','Описание']
    with open(filename,'r',encoding='utf-8') as book_file:
        for line in book_file:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    # print(phone_book)
    return phone_book


def print_result(book_list):
    if book_list == None:
        os.system('cls')
        print("Нет ни одной записи")
        return
    surname_width = max(len(line_in_book["Фамилия"]) for line_in_book in book_list)
    name_width = max(len(line_in_book["Имя"]) for line_in_book in book_list)
    phone_width = max(len(line_in_book["Телефон"]) for line_in_book in book_list)
    description_width = max(len(line_in_book["Описание"]) for line_in_book in book_list)

    print(" {:<{}}  || {:<{}}  || {:<{}}  || {:<{}}".format("Фамилия", surname_width, "Имя", name_width, "Телефон", phone_width, "Описание", description_width))
    print("=" * (surname_width + name_width + phone_width + description_width + 15))
    for line_in_book in book_list:
        print(" {:>{}}  || {:>{}}  || {:>{}}  || {:>{}}".format(line_in_book["Фамилия"], surname_width, line_in_book["Имя"], name_width, line_in_book["Телефон"], phone_width, line_in_book["Описание"], description_width), end='')


def add_contact_line(book_list):
    new_surname = input("Информация для поля ФАМИЛИЯ: ").lower().title()
    new_name = input("Информация для поля ИМЯ: ").lower().title()
    new_phone = input("Информация для поля ТЕЛЕФОН: ")
    new_description = input("Информация для поля ОПИСАНИЕ: ")
    line = {"Фамилия": new_surname, "Имя": new_name, "Телефон": new_phone, "Описание": new_description}
    book_list.append(line)
    return book_list

def remove_contact_line(book_list):
    temporary = []
    search = 0
    remove_surname = input("Укажите значение для поля ФАМИЛИЯ удалаяеммого контакта: ").lower().title()
    for line in book_list:
        if remove_surname in line['Фамилия']:
            temporary.append(line)
            search +=1
    if search == 0:
        print("Не найден объект для удаления")
        return book_list
    if search > 1:
        search = 0
        temporary_1 = temporary
        temporary = []
        remove_name = input("Контактов с такой фамилией несколько, укажите значение для поля ИМЯ удалаяеммого контакта: ").lower().title()
        for line in temporary_1:
            if remove_name in line['Имя']:
                temporary.append(line)
                search +=1
        if search == 0:
            print("Не найден объект для удаления")
            return book_list
    book_list.remove(temporary[0])
    return book_list


def write_txt(book_list, file_name = 'phonebook.txt'):
    with open(file_name,'w',encoding='utf-8') as book_file:
        for i in range(len(book_list)):
            s=''
            for v in book_list[i].values():
                s = s + v + ','
            book_file.write(f'{s[:-1]}')



work_with_phonebook()


























