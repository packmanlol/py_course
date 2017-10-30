
def search_for_records(lst, data, col_num):
    search_rezults=[]
    for row_num, record in enumerate(lst):
        if record[col_num] == data:
            search_rezults.append(record)
    return search_rezults

try:
    with open("books.txt", "r") as my_file:
        list_books = my_file.readlines()
except FileNotFoundError:
    print("Файл books.txt не найден")
    exit()

#Убираем пробелы и разделители в начале и конце элеметов списка
#Приводим типы данных
price_pos = 3
try:
    for row_num, row_data in enumerate(list_books):
        list_books[row_num] = row_data.split(",")
        for col_num, col_data in enumerate(list_books[row_num]):
            list_books[row_num][col_num] = col_data.strip()
        list_books[row_num][price_pos] = int(list_books[row_num][price_pos])
except IndexError:
    print("Неверные данные, проверьте корректность данных в файле")
    exit()
except ValueError:
    print("Неверные данные, проверьте корректность данных в файле")
    exit()

#Поиск книг по году изданияи и сортировка результата по алфавиту
year = input("Введите год издания книг: ")
lst = search_for_records(list_books, year, 2)
lst.sort(key=lambda num_str: num_str[1])

if not lst:
    print("Книг не найдено")
else:
    print("Найдено ", len(lst), "\n", lst)

#сортировка по возрастанию цены
list_books.sort(key = lambda num_: num_[3])

#Запись в файл с сортировкой по возрасатнию цены
with open("books_out.txt", "w") as my_file:
    for rows in list_books:
        for cols in rows:
            my_file.write(str(cols)+", ")
        else:
           my_file.write("\n")
