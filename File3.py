#Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк. 

File = input('File name: ') # Ввод имени файла

Lines = Words = Letters = 0

for i in open(File):
    i = i[0:-1] # Подсчет колличества строк. Перенос на следующую строку не считается.
    Lines += 1
 
    for j in i: # Подсчет колличества символов. Цикл выполняет проверку на пробелы
        if j != ' ':
            Letters += 1
 
    in_out = 0 # Подсчет колличества слов. Счетчик ищет начало и конец слова, если следующим символом является пробел, то это конец слова.
    for j in i:
        if j != ' ' and in_out == 0:
            Words += 1
            in_out = 1
        elif j == ' ':
            in_out = 0
            
print(Lines, 'lines'); print(Words, 'words'); print(Letters, 'letters')
