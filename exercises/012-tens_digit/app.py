#Complete the function to return the tens digit of a given interger
import math
def tens_digit(num):
  str1 = str(num)
  list1 = str1.split()[1:1]
  map_object = map(int, list1)
  listofint = list(map_object)
  return listofint




#Invoke the function with any interger.
print(tens_digit(179))