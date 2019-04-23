import csv

file = open("Base_Annual_Employee_Salaries.csv", "r")
reader = csv.reader(file)
yearsExp = []
salary = []
for line in reader:
    if(line[4][0:4].isnumeric()):
        yearsExp.append(2019 - int(line[4][0:4]))
        salary.append(line[3])

with open('benignData.csv','w') as f:
        for i in range(0,len(salary)):
                f.write(str(yearsExp[i]) + ',' + str(salary[i]) + '\n')