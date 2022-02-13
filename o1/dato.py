#input first date
day1 = input("input day")
month1 = input("input month")
#input second date
print("-----------------------------------")
day2 = input("input second day")
month2 = input("input second month")

#check if month1 come first, print Riktig rekkefølge!
if month1 < month2:
    print('Riktig rekkefølge!')
# check if month2 come first, print Feil rekkefølge!
elif month1 > month2:
    print("Feil rekkefølge!")
# check if same day, print same dato
elif month1 ==month2 :
    if day1 < day2 :
        print("Riktig rekkefølge!")
    elif day1 > day2:
        print("Feil rekkefølge!")
    elif day1 == day2:
        print("Samme dato!")