date_to_prove = ['15.4.2023','0.5.2022', '12.0.2022', '12.5.-2022', '29.2.2020', '12.5.2022', '28.2.2021', '31.12.9999', \
'32.5.2022', '12.13.2022', '29.2.2021', '30.2.2020']



def date_func(date_to_prove):
    date_list = list(map(lambda x: int(x), date_to_prove.split(".")))
    if date_list[0] not in range(1, 32) or date_list[1] not in range(1,13) or date_list[2] < 0:
        return False
    elif date_list[1] % 2 != 0 and date_list[0] not in (range(1, 32)):
        return False
    elif date_list[2] % 4 == 0 and date_list[1] == 2 and date_list[0] not in (range(1, 30)):
        return False
    elif date_list[2] % 4 != 0 and date_list[1] == 2 and date_list[0] not in (range(1, 29)):
        return False
    elif date_list[1] % 2 == 0 and date_list[0] not in (range(1, 32)):
        return False
    else:
        return True
i =0
for el in date_to_prove:
    i +=1
    print(i, date_func(el))