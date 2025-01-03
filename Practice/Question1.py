import math
def paint_calculation(height,weight,cover):
    area= height*weight
    no_of_cans=math.ceil(area/cover)
    return no_of_cans
h=int(input("The no of height you want to put: "))
w=int(input("The no opf weight you want to put: "))
coverage=7
print (f"The no of paint required for the wall is {paint_calculation(h,w,coverage)}")