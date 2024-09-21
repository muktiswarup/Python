#  1.Append to thhe list 
""" fruits=["apple","bananna","orange","pinapple"]
fruits.append("litch")
print(fruits) """
#  2.use slice to extract subset of the element
""" number=[0,1,2,3,4,5,6]
print(number[0:3]) #0,1,2
print(number[0:4]) #0,1,2,3
print(number[1:3]) #1,2
print(number[2:5]) #2,3,4
print(number[1:-2]) """
#  3.remove elemnt from the list
""" number=[1,2,3,4,5,6,7,8,9]
number.remove(9)
print(number)
number.append(9)
print(number)
number.remove(5)
print(number)
number.append(5)
print(number)
del number[8]
print(number)
del number
print(number) """
#  4.sort a list in ascending and descending order 
""" number=[5,3,8,6,7,2,1,4]
number.sort()
print(number) #ascending order
number.sort(reverse=True)
print(number) #descending order """
#  5.reverse a list
""" number=[4,5,6,7,8,9,1,2,3]
number.reverse()
print(number) """
#  6.Find the maximum and minimum value of a list
""" number=[4,56,36,89,78,14]
print(max(number))
print(min(number)) """
#  7.Count occurrence of specific element
""" number=[1,5,5,5,1,4,6,5,5,4,5,4,7,8,4,5,7,4,7,1,5,4,7,8,2,4,4,5,4,7,5,4]
print(number.count(4))
print(number.count(5))
print(number.count(7)) """
#  8.Create a list of square number from 1 to 10
""" squareNumber=[x**2 for x in range(1,11)]
print(f"The square of the first 10 number is {squareNumber}") """
#  9.Create a list of even number from 1 to 41
""" evenNumber=[x for x in range(1,41) if x%2==0]
print(f"The even number of first 40 number is {evenNumber}") """
#  10.Create a list of words from a sentence 
""" sentence= "Hello World"
words=[x for x in sentence.split()]
print(words)
profile="Hi i am raju the dilwala i am a driver from karnataka i want to marraige.But no one is marrying me will you marry"
raju=[raju for raju in profile.split()]
print(raju) """
#  11.Nested list access
""" number=[[1,2,3],[4,5,6]]
print(number[1][2]) """
#  12.Modify elements in a nested list
""" number=[[1,2,3],[4,5,6]]
number[0][2]=10
print(number) """
