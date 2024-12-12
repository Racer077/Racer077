#№1#
def read_last(lines, file):
    f = open(file, 'r', encoding='utf-8')
    s = f.readlines()
    if len(s) >= n and n > 0:
        for i in s[len(s) - lines:]:
            print(i)
n = int(input())
read_last(n, r'C:\Users\Елизавета\Desktop\article.txt')
#№2#
import os
def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog} [0] содержит:')
        print(f'Директории: {", ".join([f for f in catalog])}')
        print(f'Файлы: {", ".join([file for file in catalog])}')
        print('-' * 40)
print_docs('C:\Users\Елизавета\Desktop\polyteh.py\Racer077')
#№3#
def longest_words(file):
    f = open(file, 'r', encoding='utf-8')
    s = f.readlines()
    d = set()
    for i in s:
        n = i.split()
        d.add(max(n, key=len))
    if len(d) > 0: return max(d, key=len)
print(longest_words('C:\Users\Елизавета\Desktop\article.txt'))
#№4#
def redactor():
    file = open(f'{input('Введите название файла: ')}.txt', 'w+', encoding='utf-8')
    text = 'Напишите содержимое файла'
    print(text)
    while text != '':
        text = input()
        file.write(f'{text} \n')
    file.close()
redactor()