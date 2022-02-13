#creat dictionary
dict = {"melk":"14.90", "brød":"24.90","yoghurt":"12.90","pizza":"39.90"}
print(dict)
#get input from user twice
def new_product():
    product_name = input("input product name")
    prodcut_price =input("input product price")
    dict[product_name]= prodcut_price


new_product()
print(dict)
