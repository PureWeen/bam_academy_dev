# Python Basics from Unit 1
### Input - Output - Variables

### Output a message
```py
print("Hello World")
```

### Assign a value to a variable
```py
age = 14
lastName = "Bob"
shoeSize=10.5
```

### String concatenation and casting
```py
print("Hi "+lastName+"you are "+str(age))
```

### Storing user input
```py
name = input("What is your name?")
age = int(input("How old are you"))
```

# Unit 2 - In Class: IF statement and Operators

### Overview of Lesson
* Sequence
* Selection
* IF statement - `IF` or `ELSE`
* Comparison vs Assignment
* Indent in python
* `>` vs `>=`

* What are Operators?  - https://www.youtube.com/watch?v=Y6CwThhquQs&t=119s&ab_channel=GoogleStudents

### if/else statement (String)

```python
if lastName=="Bob":
  print("Welcome Bob!")
else:
  print("you are not Bob!")
```

### if/elif/else (int)
```python
if age>14:
  print("Age is above 14")
elif age>10 and age<=14:
  print("Age is between 10 and 14")
else:
  print("Under 14")
```


### Logical Operators

* `==` Equal to, `5==4` -> `False`
* `!=` Not equal to, `5!=4` -> `True`
* `<`  Less than, 2<10 -> `True`
* `<=` Less than or equal to, 2<=10 -> `True`
* `>` Greater than, 9>9 -> `False`
* `>=` Greater than or equal to, 9>=9 -> `True`
* `and` AND, 3>2 and 5==4 -> `False`
* `or` OR, 3>2 or 5==4 -> `True`

examples of logical operators

```
x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y
```

## Helpful resources
* https://docs.python.org/3/reference/expressions.html#expression-lists