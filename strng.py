name = 'motlokwe'

# string operation 
print(name.capitalize())
print(name.upper())


new_name = 'Femi Edmund'
print(new_name.startswith('Zem'))
print(new_name.endswith('nd'))
#
student_number = '1234567'
print(student_number.isnumeric())



# 
school = 'UJ UJ UJ UJ UJ UJ'
new_school = school.replace('UJ', 'UP' , -1)
print(new_school)

introduction = 'Mky name is motlokwe and I am 24 years old'
print(introduction.rfind('24'))
print(introduction[28])

print(introduction.title)
