"""
## Lesson 3: Activity 1
Peter wants to write an algorithm that goes through the list of temperatures and calculate the following:
* the average temperature
* the highest temperature
* the lowest temperature
"""

# Inputs
temps = [5, 6, 6, 9, 10]
total = 0
high = 0
low = 100

# start your loop here
for temp in temps:
  if (temp > high):
    high = temp

  if (temp < low):
    low = temp

print(high)
print(low)

#############################
# Solve Activity 1.1 first before moving on to 1.2
#############################
"""
----
## Activity 1.2 

Peter now wants to be able to input temperatures for a new week. You should ask for each dayawef "Please enter temperature for Monday" etc. 

The algorithm should then calculate the average, lowest and higest temperature for the week, just like before. 
"""

days = ['mon', 'tue', 'wed', 'thu', 'fri']
