
import os


def CheckID(lst, book_id):
    for row in lst:
        if row[0] == int(book_id):
            return False
    else:
        return True


def FindPosition(lst, ind, col_pos):
    for pos, row in enumerate(lst):
        if row[col_pos] == ind:
            return pos


def ShowList(lst):
    os.system('clear')
    print("========================================")
    print("              All Books")
    print("========================================")
    print("ID       Author      Name      Year")
    print("\n".join(map(str, lst)))
    input("\n    Press Any Key to continue....     ")


def UpdateRecord():
    os.system("clear")
    print("========================================")
    print("            Update Record")
    print("========================================")

    book_id = input("Type ID to change record: ")
    tmp_lst =[]
    if not book_id:
        MainMenu()
    elif not book_id.isdigit():
        input("Invalid Value")
        UpdateRecord()
    else:
        id_pos = FindPosition(list_books, int(book_id), 0)
        if not id_pos:
            input("Not found")
            MainMenu()

        tmp_lst = list_books.pop(id_pos)
        print(tmp_lst)

    author = input("Author: ")
    if author:
        tmp_lst[1] = author
    name = input("Name: ")
    if name:
        tmp_lst[2] = name
    year = input("Year: ")
    if year.isdigit():
        tmp_lst[3] = int(year)
    else:
        if year:
            print("Invalid Year")

    list_books.insert(id_pos, tmp_lst)
    input("----Done-----")
    MainMenu()


def CorrectingDataType(list_books):
    id_pos = 0
    year_pos = 3
    for row_num, row_data in enumerate(list_books):
        list_books[row_num] = row_data.split(",")
        for col_num, col_data in enumerate(list_books[row_num]):
            list_books[row_num][col_num] = col_data.strip()
        list_books[row_num][id_pos] = int(list_books[row_num][id_pos])
        list_books[row_num][year_pos] = int(list_books[row_num][year_pos])


def MainMenu():
    os.system('clear')
    print("========================================")
    print("          Books Database")
    print("========================================")
    print("  1 - Show Books")
    print("  2 - Search for a book")
    print("  3 - Add book")
    print("  4 - Update record")
    print("  5 - Delete book")
    print("  6 - Save Changes")
    print("  0 - Exit")
    print("========================================")

    inp = input("  Enter a selection: ")
    if inp == "1":
        ShowList(list_books)
        MainMenu()
    elif inp == "2":
        SerchBooksMenu()
        MainMenu()
    elif inp == "3":
        AddRecordMenu()
        MainMenu()
    elif inp == "4":
        UpdateRecord()
        MainMenu()
    elif inp == "5":
        DelRecord()
        MainMenu()
    elif inp == "6":
        SaveToFile()
        MainMenu()

    elif inp == "0":
        os.system("clear")
        exit()
    else:
        MainMenu()


def SerchBooksMenu():
    os.system("clear")
    print("========================================")
    print("    Select a column name to search")
    print("========================================")
    print("  1 - ID")
    print("  2 - Author")
    print("  3 - Name")
    print("  4 - Year")
    print("  0 - Back to Main menu")
    print("========================================")

    inp = input("  Enter a selection: ")
    if inp == "1":
        inp = input("ID: ")
        if not inp.isdigit():
            input("Value Error: integer only")
            SerchBooksMenu()
        lst_tmp = list(filter(lambda serch_rez: serch_rez[0] == int(inp), list_books))
        if not lst_tmp:
            input("Not found")
            SerchBooksMenu()
        else:
            print("\n".join(map(str, lst_tmp)))
            input("\n Press any key to continue..")

    elif inp == "2":
        inp = input("Author: ")
        lst_tmp = list(filter(lambda serch_rez: serch_rez[1] == inp, list_books))
        if not lst_tmp:
            input("Not found")
            SerchBooksMenu()
        else:
            print("\n".join(map(str, lst_tmp)))
            input("\n Press any key to continue..")

    elif inp == "3":
        inp = input("Name: ")
        lst_tmp = list(filter(lambda serch_rez: serch_rez[2] == inp, list_books))
        if not lst_tmp:
            input("Not found")
            SerchBooksMenu()
        else:
            print("\n".join(map(str, lst_tmp)))
            input("\n Press any key to continue..")

    elif inp == "4":
        inp = input("Year: ")
        if not inp.isdigit():
            input("Value Error: integer only")
            SerchBooksMenu()
        lst_tmp = list(filter(lambda serch_rez: serch_rez[3] == int(inp), list_books))
        if not lst_tmp:
            input("Not found")
            SerchBooksMenu()
        else:
            print("\n".join(map(str, lst_tmp)))
            input("\n Press any key to continue..")

    elif inp == "0":
        MainMenu()
    SerchBooksMenu()


def AddRecordMenu():
    os.system("clear")
    print("========================================")
    print("              Add Record ")
    print("========================================")
    lst_tmp = []

    book_id = input("Type Id: ")
    if not book_id:
        MainMenu()
    elif not book_id.isdigit():
        input("Invalid Value")
        AddRecordMenu()
    elif CheckID(list_books, book_id):
        lst_tmp.append(int(book_id))
    else:
        input("ID already exist")
        AddRecordMenu()

    author = input("Type Author: ")
    if not author:
        input("Can't be null value")
        AddRecordMenu()
    else:
        lst_tmp.append(author)

    name = input("Type Name: ")
    if not name:
        input("Can't be null value")
        AddRecordMenu()
    else:
        lst_tmp.append(name)

    year = input("Type Year: ")
    if not year:
        input("Can't be null value")
        AddRecordMenu()
    elif not year.isdigit():
        input("Invalid Value")
        AddRecordMenu()
    else:
        lst_tmp.append(int(year))
        list_books.append(lst_tmp)
        input("----Done----")
        AddRecordMenu()


def DelRecord():
    os.system("clear")
    print("========================================")
    print("            Delete Record ")
    print("========================================")
    book_id = input("Type ID to del: ")
    if not book_id:
        MainMenu()
    elif not book_id.isdigit():
        input("Invalid Value")
        AddRecordMenu()
    elif not CheckID(list_books, book_id):
        del_pos = FindPosition(list_books, int(book_id), 0)
        list_books.pop(int(del_pos))
        input("------Done------")
        DelRecord()
    else:
        input("ID not exist")
        AddRecordMenu()


def SaveToFile():
    with open("books.txt", "w") as my_file:
        for rows in list_books:
            for cols in rows[:-1]:
                my_file.write(str(cols) + ", ")
            else:
                my_file.write(str(rows[-1])+"\n")
    input("----Done... Press any key---------")


try:
    with open("books.txt", "r") as my_file:
        list_books = my_file.readlines()
    CorrectingDataType(list_books)
except FileNotFoundError:
    print("Файл books.txt не найден")
    exit()
except IndexError:
    print("Неверные данные, проверьте корректность данных в файле")
    exit()
except ValueError:
    print("Неверные данные, проверьте корректность данных в файле")
    exit()
MainMenu()
