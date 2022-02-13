# dictionary , key = name, value = meal
# add 3 person in dict
matplan_dict = {'Kari':['brød til frokost','egg til lunsj,middag','pølser til middag.'],'Ole':['brød til frokost','egg til lunsj,middag','pølser til middag.'],'Peder':['brød til frokost','egg til lunsj,middag','pølser til middag.']}

#get name from user
def getname():
    #convert the first letter to uppercase by using capitalize
    name = input("write your name").capitalize()
    #if the name is not on the dict, print out feedback
    if name not in matplan_dict:
        print("You are not on the list")
    #if the name is on the dict, print out 3 meals
    elif name in matplan_dict:
        print(matplan_dict[name])
#call getname()
getname()

#a. Brukernavn på alle IN1000 studentene  ----- list
#b. Brukernavn og antall poeng på innlevering 3 for alle studentene på IN1000 --- dictionary
#c. Alle vinnere i Lotto siste år (kun navn) ---list
#d. All mat noen gjester i et selskap er allergisk mot (for å planlegge menyen) --- set
