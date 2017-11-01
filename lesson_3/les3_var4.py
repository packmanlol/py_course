
try:
    with open("books.txt", "r") as my_file:
        list_books = my_file.readlines()
except FileNotFoundError:
    print("Файл books.txt не найден")
    exit()

#Убираем пробелы и разделители в начале и конце элеметов списка
#Приводим типы данных
PRICE_POS = 3
YEAR_POS = 2

try:
    for row_num, row_data in enumerate(list_books):
        list_books[row_num] = row_data.split(",")
        for col_num, col_data in enumerate(list_books[row_num]):
            list_books[row_num][col_num] = col_data.strip()
        list_books[row_num][PRICE_POS] = int(list_books[row_num][PRICE_POS])
except IndexError:
    print("Неверные данные, проверьте корректность данных в файле")
    exit()
except ValueError:
    print("Неверные данные, проверьте корректность данных в файле")
    exit()

#Поиск книг по году изданияи и сортировка результата по алфавиту
year = input("Введите год издания книг: ")
lst = list(filter(lambda serch_rez: serch_rez[YEAR_POS] == year, list_books))
lst.sort(key=lambda num_str: num_str[YEAR_POS])

if not lst:
    print("Книг не найдено")
else:
    print("Найдено ", len(lst), '\n',
          '\n'.join(map(str, lst)))

#сортировка по возрастанию цены
list_books.sort(key = lambda num_: num_[PRICE_POS])

#Запись в файл с сортировкой по возрасатнию цены
with open("books_out.txt", "w") as my_file:
    for rows in list_books:
        for cols in rows:
            my_file.write(str(cols)+", ")
        else:
            my_file.write("\n")
