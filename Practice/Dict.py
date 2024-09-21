#Dict is a dictionary that used to store the key and value in python.The key value must b unique and dict is a mutable.

#1. Write a dict example
person={
    "name":"Rahul Bose",
    "age":25,
    "subject":"Mca"
}
""" print(person) """
#2.Access the key value in dict 
""" print(person["name"])
print(person["age"]) """
#3.Adding or updating the value
""" person["name"]="Gandi mara bhakata"
print(person)
person["age"]=24
print(person)
person["character"]="bad"
print(person) """
#4deleting a key valyue pair
""" del person["subject"]
print(person) """
#5.itereting over dict
""" for key in  person:
    print(key)
for value in person.values():
    print(value)
for key,value in person.items():
    print(f"{key}:{value}") """


""" 6.Create a dictionary that stores student names and their marks.
Retrieve the mark of a specific student from the dictionary.
Update a student’s mark in the dictionary.
Add a new student to the dictionary.
Remove a student from the dictionary. """
""" student={
    "Sehwag":0,
    "Gambhir":97,
    "Virat":35,
    "Mahi":91
}
print(student["Sehwag"])
student["Virat"]=36
student["Yuvraj"]=19
print(student)
del student["Sehwag"]
print(student) """

#write a function that a key is presence or not in the dictionary
def check_key(d,key):
    return key in d
student={"alice":54}
print(check_key(student,"alic"))