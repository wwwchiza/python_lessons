month_num = int(input("введите номер месяца"))

if month_num==1 or month_num==2 or month_num==12:
    print("winter")
elif month_num==3 or month_num==4 or month_num==5:
    print('spring')
elif month_num==6 or month_num==7 or month_num==8:
    print("summer")
else:
    print('autumn')