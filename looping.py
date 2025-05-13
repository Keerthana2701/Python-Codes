#looping
#while-repeat until condition is true.
#used when we do not know how long it will repeat
i=10
while i<20:
    print(i)
    i+=1

#to manually break a loop
#even if condition is true
#use break
i=190
while i<200:
    print(i)
    if i==210:
        break
    i+=1
#if correct password is entered, break
correct_password="Keerthu"
while True:
    enter_password=input("enter the password")
    if enter_password==correct_password:
        print("correct password")
        break
    else:
        print("wrong password")

#continue: that code is not executed for that iteration
i=10
while i<20:
    i+=1
    if i==14:
     continue
    print(i)


#for loop
#used to loop over list, tuple, string, set,
#dict, range of numbers
for i in range(1,10):
    print(i)


for i in range(1,10):
    if i==3:
        continue
    print(i)
  




