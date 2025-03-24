dict1 = {
    1 : "Red", 
    2 : "Blue",
    3 : "Orange",
    4 : "violet", 
    5 : "yellow", 
    6 : "Maroon"
}
# for i in dict1:
#     print(i, dict1[i])


# print(any(dict1.values()))
print(dict1.popitem())
# print(all(dict1.values()))
print("after popping")



dict2 = dict1.copy()
for i in dict2:
    print(i, dict2[i])