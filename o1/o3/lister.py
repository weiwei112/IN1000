#create list
list = [2,4,6]
#add new number 8
list.append(8)
#print first and last number
print("first number is ",list[0])
print("last number is ",list[-1])

#creat new empty list
name_list=[]
#get input from user
def getname():
    name_input = input("write a name")
    name_list.append(name_input)
#ask 4 names from user
getname()
getname()
getname()
getname()
# check name wei in list or not
myname= "wei"
def check_name():
    if myname in name_list :
        print("Du husket meg!”")
    else:
        print("Glemte du meg?")
check_name()
#print name list
print(name_list)

#sum of list numbers
listsum= sum(list)
print(listsum)
#multiply list
def multipy(list):
    result = 1
    for x in list:
        result = result*x
    return result
print(multipy(list))