'''Напишите функцию read_last(lines, file),
 которая будет открывать определенный файл file и выводить на печать построчно последние строки в
  количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на
   файле «article.txt» со следующим содержимым:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела'''

def read_last(lines, file):
    if lines > 0:
        with open('article.txt',"r", encoding='utf-8') as text:
            file_lines = text.read().splitlines()[-lines:]
        for line in file_lines:
            print(line.strip())



input_lines = int(input("Введите количество строк: "))
read_last(input_lines,"article.txt")

