# set is unordered,unique and mutable
myset={1,2,3,4,6}
print(myset)
myset.add(7)
print(myset)
myset1={7,9,34,65}
#union
print(myset | myset1)
#intersection 
print (myset & myset1)
#difference
print(myset - myset1)
#looping set
for items in myset:
    print("set:",items)
#dictionary
mydict={
    "name" : "keerthu",
    "age" :35,
    "city" :"Plano"
}
print(mydict)
mydict["state"]="TX"
print(mydict)