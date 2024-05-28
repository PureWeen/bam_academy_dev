#before you can use a library have to import it

import random
num = random.randint(1, 9)
print(num)

#if statement
if num > 9:
  print("greater than 9")
elif num>2 and num<=7:
  print("between 2 and 7")
else:
 print("neither")

#get an input using a variable called one
one = input("First input: ")
print ("First: ", one)


## Lists
#Below is an example where we declares three variables, `name1`, `name2`, and `name3`, and assigns them the values "Bob", "Jo", and "Ash", respectively. Then, it prints out the value of `name3`.

name1 = "Bob"
name2 = "Jo"
name3 = "Ash"
name4 = "James"
name5 = "Cat"

names = [name1, name2, name3, name4, name5]
i = 0

#can also use len(names) to get size of the list
#you can't add a number to a string, without converting it to a string, using str() function
#print("Len: " + str(len(names)))
#while i < 5:
 # print(names[i])
 # i = i + 1

for name in names:
  print("START")
  print(name)
  print("END")
  
#can also define the list this way
#use an index to refer to a specific member of the list
#
#name = ["Bob", "Jo", "Ash"]
#print(name)
#print(name[1])
#name[1] = "Joey"
#print(name)
#name = ["Bob", "Joe", "Ash", name1, name2, 15444]
#print(name)
#
#
#print("Student1")
#print("Student2")
#print("Student3")
#print("Student4")
#print("Student5")

#name = ["Bob", "Joe", "Ash", name1, name2, 15444]

#for i in name:
# print(i)

#
#for i in range(len(name)):
#  print(i)
#  print("Student"+str(i+1))
#  print(name[i])


# lists declaration and assignment
#names = ["Bob", "Jo", "Ash"]
#print(names[2])
#names[1] = "Mo"
#print(names[1])
#print(names)
