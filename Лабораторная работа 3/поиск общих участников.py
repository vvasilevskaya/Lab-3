def find_common_participants(str1,str2, n = ','):
    number1 = list(str1.split(n))
    number2 = list(str2.split(n))
    z = list(set(number1).intersection(number2))
    z.sort()
    return z

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))

# TODO Провеьте работу функции с разделителем отличным от запятой
