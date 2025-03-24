dict1 = {
    1 : "Red", 
    2 : "Blue",
    3 : "Orange",
    4 : "violet", 
    5 : "yellow", 
    6 : "Maroon"
}
# for i,j in dict1.items():
#     print(i, j)


dict1.pop(5)
print("After poping out the 5th elements" ,dict1)

dict1.clear()
print("Removing all the elements from the  dictionary" , dict1)