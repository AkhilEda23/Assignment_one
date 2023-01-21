import statistics

#sorted the list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("ages :",ages)

#minimum age among the list
minimum = min(ages)
print("Minimum age :",minimum)

#maaximum age among the list
maximum  = max(ages)
print("Maximum age:",maximum)

#adding maximum and minimum  age to the list
ages.append(maximum)
ages.append(minimum)

#finding the median of ages
medain_value = statistics.median(ages)
print("Median of the ages:",medain_value)

#finding the average of ages
mean_value = statistics.mean(ages)
print("Average of the age:",mean_value)

#Range of the ages
range_value  = max(ages) - min(ages)
print("Range of ages:",range_value)
