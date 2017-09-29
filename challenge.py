import pandas

wages = pandas.read_csv("wages.csv")

genderYears = pandas.DataFrame(wages,columns=['gender','yearsExperience'])
genderYears.drop_duplicates(['gender','yearsExperience'], keep='first', inplace=True)
genderYears.sort_values(['gender','yearsExperience'], ascending=[True, True], inplace=True)
genderYears.to_csv('uniqueGenderYears.txt', sep=' ')

print("Highest earner:")
print(wages.loc[wages['wage'].argmax(), ['gender', 'yearsExperience', 'wage']])

print("Lowest earner:")
print(wages.loc[wages['wage'].argmin(), ['gender', 'yearsExperience', 'wage']])

collegeSalery = 0;
highSchoolSalery = 0;
collegeCount = 0;
highSchoolCount = 0;

for index in range(0, 3294 ,1):
    if wages.loc[index, 'yearsSchool'] >= 16:
        collegeCount += 1
        collegeSalery += wages.loc[index, 'wage']
    if wages.loc[index, 'yearsSchool'] <= 12:
        highSchoolCount += 1
        highSchoolSalery += wages.loc[index, 'wage']

