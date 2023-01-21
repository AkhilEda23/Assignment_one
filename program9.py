
#taking output for number of students
num_of_students = int(input("Enter the student count: "))

weight = [] #creating empty list

#taking input for the n specified students weights in lbs and converting the pounds in kilograms
for i in range(0,num_of_students):
  ele = float(input("enter weights: "))
  kilo_weight = ele / 2.2046
  kilo=round(kilo_weight,2)
  weight.append(kilo)

print("Weights of the students: ",weight)