print('List and Tuples')
#list
mylist=[23,54,45,'Keerthu','Vikee']
print(mylist)
print(mylist[1])
print(mylist[:])
print(mylist[0:2])
mylist.append('Aadhvik')
print(mylist)
mylist.extend(['Rhea',1,2])
print(mylist)
mylist.insert(0,'Hello')
print(mylist)
# adds to that 2nd position since we ended in 2nd itself.
#doesn't replace any
mylist[2:2]=['hi','gm']
print(mylist)
#this replaces since the start and end poitn differs
mylist[1:2]=['happy','day']
print(mylist)
mylist.reverse()
print(mylist)
#list constructor
#using list() to create a list
#use  (())
num=list((1,2,3,4,5,7))
print(num)

#tuple- cannot be changed 
mytuple=('keerth','vikee','aadhvik','rhea')
print(mytuple)
# to change tuple, make it a list
newtuple=list(mytuple)
print(newtuple)
newtuple.append('hello')
print(newtuple)


