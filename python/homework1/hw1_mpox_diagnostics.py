#
# COP 5008 Homework #1 - Mpox Diagnostics
#
# Eric Dixon
#
# Open data file

# Ask Questions

# Display result of questionaire
infile = open("HW #1 Data.txt")
name = 0 
sum = 0 
questionOne = "Have you been having headaches?"
questionTwo = "Have you been having severe headaches?"
questionThree = "Have you had a fever?" 
questionFour = "Do you have swollen lymph nodes?"
questionFive = "Do you feel exhausted?"
questionSix = "Do you have a backache?"
questionSeven = "Are you experiencing chills?"
questionEight = "Do you have a rash?"
questionNine = "Do you have a rash in / on your genitals?"
questionTen = "Do you have muscle pains?"
numOne = "No"
numTwo = "No"
numThree = "No"
numFour = "No"
numFive = "No"
numSix = "No"
numSeven = "No"
numEight = "No"
numNine = "No"
numTen = "No"
order = 1


def questions():
  sum = 0
  line = infile.readline()
  numOne = line.rstrip()
  while (line != ""):
    if numOne == "Yes":
      print("{0} {1}".format(questionOne,numOne))
      sum += 1
      line = infile.readline()
      numTwo = line.rstrip()
      if numTwo == "Yes":
        sum += 2
        print("{0} {1}".format(questionTwo,numTwo))
      if numTwo == "No":
        print("{0} {1}".format(questionTwo,numTwo))
    if numOne == "No":
      print("{0} {1}".format(questionOne,numOne))
      numTwo = "No"
      print("{0} {1}".format(questionTwo,numTwo))
    #Get answer to Question 3
    line = infile.readline()
    numThree = line.rstrip()
    if numThree == "Yes":
      sum += 3
      print("{0} {1}".format(questionThree,numThree))
    if numThree == "No":
     print("{0} {1}".format(questionThree,numThree))
    line = infile.readline()
    numFour = line.rstrip()
    if numFour == "Yes":
     sum += 3
     print("{0} {1}".format(questionFour,numFour))
    if numFour == "No":
     print("{0} {1}".format(questionFour,numFour))
    line = infile.readline()
    numFive = line.rstrip()
    if numFive == "Yes":
     sum += 2
     print("{0} {1}".format(questionFive,numFive))
    if numFive == "No":
     print("{0} {1}".format(questionFive,numFive))
    line = infile.readline()
    numSix = line.rstrip()
    if numSix == "Yes":
     sum += 2
     print("{0} {1}".format(questionSix,numSix))
    if numSix == "No":
     print("{0} {1}".format(questionSix,numSix))
    line = infile.readline()
    numSeven = line.rstrip()
    if numSeven == "Yes":
     sum += 3
     print("{0} {1}".format(questionSeven,numSeven))
    if numSeven == "No":
     print("{0} {1}".format(questionSeven,numSeven))
    line = infile.readline()
    numEight = line.rstrip()
    if numEight == "Yes":
     print("{0} {1}".format(questionEight,numEight))
     sum += 3
     line = infile.readline()
     numNine = line.rstrip()
     if numNine == "Yes":
       sum += 4
       print("{0} {1}".format(questionNine,numNine))
     if numNine == "No":
       print("{0} {1}".format(questionNine,numNine))
    if numEight == "No":
     print("{0} {1}".format(questionEight,numEight))
     numNine = "No"
     print("{0} {1}".format(questionNine,numNine))
    line = infile.readline()
    numTen = line.rstrip()
    if numTen == "Yes":
     sum += 2
     print("{0} {1}".format(questionTen,numTen))
    if numTen == "No":
     print("{0} {1}".format(questionTen,numTen))
    if sum >= 15:  
      print("==> You may have mxpox, please see a doctor.")
    else:
      print("==> You probably do not have mpox.")
    line = infile.readline()
    if (line == '\n'):
      break
    line = infile.readline()
    if (line == ''):
      break

patients = 10

for i in range(patients):
  line = infile.readline()
    #Get first name in the list
  name = line.strip()
  print("Patient name: ",name)
  questions()
  print()



infile.close()
