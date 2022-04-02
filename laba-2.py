'''Написать программу, которая читая последовательность чисел из файла,
выводит на экран используемые цифры и их количество'''

quantity = 0                                                        #счетчик количества чисел
buffer = 1                                                          #размер буфера чтения
result_block = [0]*10                                                   #массив для вывода числа
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
                    result_block[int(block)] += 1

                block = file.read(buffer)

        print("Количество цифр 0 - ", result_block[0])
        print("Количество цифр 1 - ", result_block[1])
        print("Количество цифр 2 - ", result_block[2])
        print("Количество цифр 3 - ", result_block[3])
        print("Количество цифр 4 - ", result_block[4])
        print("Количество цифр 5 - ", result_block[5])
        print("Количество цифр 6 - ", result_block[6])
        print("Количество цифр 7 - ", result_block[7])
        print("Количество цифр 8 - ", result_block[8])
        print("Количество цифр 9 - ", result_block[9])
        result_block = []
except FileNotFoundError:                                          #исключаем ошибку 'файл не найден' для понимания ( почему программа не работает)
  print ("\nФайл в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")

