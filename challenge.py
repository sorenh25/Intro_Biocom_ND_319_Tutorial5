import pandas

wages = pandas.read_csv("wages.csv")

genderYears = pandas.DataFrame(wages,columns=['gender','yearsExperience'])
genderYears.drop_duplicates(['gender','yearsExperience'], keep='first', inplace=True)
genderYears.sort_values(['gender','yearsExperience'], ascending=[True, True], inplace=True)
genderYears.to_csv('uniqueGenderYears.txt', sep=' ')

