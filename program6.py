Striing = "I am a teacher and I love to inspire and teach people"

#Splitting the string using the set to get the unique words
split_strings = set(Striing.split(" "))
print("Unique Words: ",split_strings)

#Finding the count of unique words
print("Number of unique words = ",len(split_strings))
