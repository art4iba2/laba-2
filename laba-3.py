'''Написать программу, которая читая последовательность чисел из файла,
выводит на экран используемые цифры и их количество'''
import time

quantity = 0                                                        #счетчик количества чисел
buffer = 1                                                          #размер буфера чтения
result_block = []                                                   #массив для вывода числа
try:
    with open("nums1.txt", "r") as file:                            #открывается файл
        block = file.read(buffer)                                   #читается первый блок

        if not block:
            print("Файл пустой, измените его или добавьте другой файл")

        while block:                                                #пока файл не пустой ищем цифры

            while (block < '0' or block > '9' ) and block:
                block = file.read(buffer)                           #читатся очередной блок


            while (block >= '0' and block <= '9' or block == '.' or block == ',' ) and block: #обрабатываются цифры

                if block.isnumeric() == True :                      #если символ число, то кол-во не увеличиваем и заносим в массив для вывода
                    quantity += 0
                    result_block.append(block)

                block = file.read(buffer)
                if block.isnumeric() == False and block != '.' and block != ',': #если символ не цифра и не '.' ',' то кол-во чисел увеличивваем на 1
                  quantity += 1
            support_block = result_block
            print(result_block)                                     #выводится прочтенное число
            result_block = []                                       #очищается массив для следующего числа
        if quantity == 0 :
            print("Файл не содержит цифр, добавьте или измените файл")


        print('Количество чисел в последовательности: ',quantity)  #выводится кол-во чисел
except FileNotFoundError:                                          #исключаем ошибку 'файл не найден' для понимания ( почему программа не работает)
  print ("\nФайл в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
print("Время работы программы:  ", time.process_time(), "seconds") #выводится время работы программы
