# sset = {"a", "b", "c", "d"}
# print(sset)
# for i in sset:
#     print(i)

sset = {1,2,3,4,5,6,7,8,9,10}
print(sset)
sset.remove(2)
print("After removing 2: ", sset)
sset.pop()
print("after using the pop method", sset)

sset.clear()
print("After using the clear method", sset)