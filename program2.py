#Dictionaries

#created dog dictionary having certain keys and values
dog = {
    "name" : "Miller",
     "color":"white",
     "breed" :"shinzu",
     "legs":4,
     "age":2
}
print("My Dog :",dog)

#created student dictionaries with certain keys and values.
student = {
    "first_name" : "John",
    "last_name" :"Snow",
    "gender" :"male",
    "age":25,
    "marital_status" :"married",
    "skills" :["C programming","node","python"],
    "country":"USA",
    "city":"Overland Park",
    "address":"9008 w 124thst"
}
print("Sudent Details: ",student)


#finding the length of student dictionary
print("Length of student dictionary: ",len(student))

#acessing the skills value and checking the data type
print(student["skills"])
print("Type is:",type(student['skills']))

#updated the skills by adding another skills to the list
student["skills"].append("R programming")
print("Updated skills: ",student["skills"])

#Get dictionary keys as list
keys = student.keys()
print("Dictionary Keys are: ",keys)

#Get dictionary values as list
values = student.values()
print("Dictionary Values are: ",values)