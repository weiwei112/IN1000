#create meny with allergi source
meny = {'gluten':['burger','noodle'],'fish':['seafood soup','seafood BBQ'],'soya':['soya milk']}

#check allergi
def allergi():
    # get allergi source from user
    source = input("write your allergi")
    # check the input source is on the list or not
    if source in meny.keys():
        #if ont the list, print related food
        print("You can eat : ",meny[source])
    # if not on the list, print safe message
    else:
        print("The meny is safe")

#call allergi
allergi()