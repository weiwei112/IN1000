#Gitt følgende kode, hvorfor blir False printet ut? Svar som en kommentar i filen.
#fruktliste = [“eple”, “eple”, “banan”, “banan”, “banan”]
#fruktmengde = {“eple”, “eple”, “banan”, “banan”, “banan”}
#print(len(fruktliste) == len(fruktmengde))
#dictionary should have key and value, here only has key


# make a dict for frukt
frukt_dict = {'eple':2,'banan':3}
print(frukt_dict)

#get input from user, name&volume
def new_frukt():
    frukt_name = input("input a new fruit")
    frukt_volume= int(input("input the volume"))
    #check if volume is negative
    if frukt_volume < 0:
        print("Ugyldig input!")
    # if the frukt is not in the dict, add it with volume
    elif frukt_name not in frukt_dict.keys():
        frukt_dict[frukt_name] = frukt_volume
    # if the frukt is in the dict, update the volume
    elif frukt_name in frukt_dict.keys():
        frukt_dict.update({frukt_name:frukt_volume})
    # print new frukt dict
    print(frukt_dict)
# call function
new_frukt()
