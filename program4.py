#Set

#Created a set of IT Companies and finding the length of set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("Length of set is ",len(it_companies))

#Adding / Updating the value to the set
it_companies.add("Twitter")
print("Updated set: ",it_companies)

#Adding / Updating multiple values to the set
it_companies.update(["Cognizant","TCS","Accenture","MindTree"])
print("Updated Set of multiple values: ",it_companies)

#Remove value from the set
it_companies.remove('TCS')
print("Updated Set: ",it_companies)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Joining A and B
C = A.union(B)
print("New Set: ",C)

#finding the intersection of A and B
D = A.intersection(B)
print("new set:",D)


#Is A subset of B?
print("Is A subset of B? ",A.issubset(B))

#Are A and B disjoint sets
print("Are A and B disjoint sets? ",A.isdisjoint(B))

#Join A with B and B with A
print("Joining A with B: ",A.union(B))
print("Joining B with A: ",B.union(A))

#Symmetric difference of 2 sets
print("Symmetric Difference: ",A.symmetric_difference(B))

#Deleted the sets Completely
del A
del B


age = [22, 19, 24, 25, 26, 24, 25, 24]
#Converting the list into set
age_set = set(age)
print("Age : ",age_set)

#Comparing the length of age in set with age in list
print("Length age in list: ",len(age))
print("Length of age in set: ",len(age_set))
if(len(age)>len(age_set)):
    print("List is larger")
else:
    print("Set is larger")

##########################################################################################################################################
#What is the difference between remove and discard?
#The major purpose of remove and discard is to delete an element from the set.
#although both have various functionality

#remove : set.remove() throws an error if there is no specified element in the list 
# num = {"1","2","3","4","5","6"}
# num.remove("1")
# print(num)
# num.remove("7")
# print(num)

#discard :set.discard() removes the specified element and doesnt throw the error message
# num = {"1","2","3","4","5","6"}
# num.discard("1")
# print(num)
# num.discard("7")
# print(num)
#########################################################################################################################################