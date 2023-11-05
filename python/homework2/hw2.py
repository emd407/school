# COP 5008 – Homework #2: Almost A Problem
# Eric Dixon
#Open data file for reading
infile =open("CGS 2060 - Homework #2 - Almost A Problem - Data.txt","r")
#Read file in and set as variable "data" (I realize now I could have used realine and split from there.)
data = infile.read()
#Create a list from the data in the file 
myList = list(data)
#Remove new line characters and split list up into individual items
list = data.replace('\n', ' ').split()
#Question 1: percentage of men vs women that have mxpox 
posMale = 0
posFemale = 0
#Get number of positive males
for i in range(len(list)):
    if list[i] == 'M' and i + 13 < len(list):
      if list[i + 13] == '1':
        posMale += 1
#Get number of positive females
for i in range(len(list)):
    if list[i] == 'F' and i + 13 < len(list):
      if list[i + 13] == '1':
        posFemale += 1
totalPos = posMale+posFemale
pctMale = (posMale/totalPos) * 100
pctFemale = (posFemale/totalPos) * 100
print("1. What is the percentage of men vs. women who have mpox?")
print()
#Print answer to Question 1: 
print("Of the people who have Mpox, {0:.2f}% of them are male.".format(pctMale))
print("Of the people who have Mpox, {0:.2f}% of them are female.".format(pctFemale))
print()
#Question 2 Demographic of mpox and over age 65
#Create individual lists for gender, age, infected status
genders = []
ages = []
infected = []
weight = []
for i in range(0, len(list), 14):
    genders.append(list[i])
    ages.append(int(list[i + 1]))
    infected.append(int(list[i + 13]))
    weight.append(int(list[i + 2]))

#function to remove all the non positive males, females, ages at index 1,12,11
def removeNonPos(field):
  (field).pop(1)
  (field).pop(12)
  (field).pop(11)
removeNonPos(genders)
removeNonPos(ages)
removeNonPos(infected)
removeNonPos(weight)

#create a combined list of the needed data: gender, age, infected status  
combined_list = genders + ages 
#Get number of people over age 65 with MPOX 
age65 = 0
for a in range(len(ages)):
  if ages[a] > 65:
    age65 +=1
#Get number of Males and number of Females over 65 with MPOX:
countM65=0
countF65=0
for i in range(len(combined_list)):
    if combined_list[i] == 'M' and i + 13 < len(combined_list):
      if combined_list[i + 11] > 65:
        countM65 +=1
    elif combined_list[i] == 'F' and i + 13 < len(combined_list):
      if combined_list[i + 11] > 65:
        countF65 += 1
        
print("2. Question #2:")
print("      a. How many people over 65 have mpox?   Answer:",age65)
print("      a. How many men over 65 have mpox?   Answer: ",countM65)
print("      a. How many women over 65 have mpox?   Answer:",countF65)
print()
print()
#Answer Question 3: How many under the age of 18 have mpox?
age18 =0
for a in range(len(ages)):
  if ages[a] < 18:
    age18 +=1
print("3. How many people under the age of 18 have mpox?")
print()
print("Of the people that have mpox", age18, "are under 18")
combined_list2 = genders + weight 
countM210=0
countF180=0
for i in range(len(combined_list2)):
    if combined_list2[i] == 'M' and i + 13 < len(combined_list2):
      if combined_list2[i + 11] > 210:
        countM210 += 1
    elif combined_list2[i] == 'F' and i + 13 < len(combined_list2):
      if combined_list2[i + 11] > 180:
        countF180 += 1
print()
print()
print("4. How many men who are overweight by at least 20 pounds have mpox?  Answer:",countM210)
print()
print("5. How many women who are overweight by at least 20 pounds have mpox?  Answer:",countF180)    
