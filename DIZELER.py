# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:22:31 2024

@author: merca
"""

 #           DIZELER 
 
'''course='Python for Begginers'
print(course[0:3])
print(course[0:])
print(course[2:])
print(course[:5])
print(course[3:-2])'''

'''name='Jennifer'
print(name[1:-1])'''

first='John'
last='Smith'
'''message= first +'[' +last+ '] is a coder'
print(messsage)'''

'''msg=f'{first +} [{last}] is a coder'
print(msg)'''

course='Python for Beginners'
print(len(course)) #len function to count the number of characters in a string
print(course.upper()) #for converting a string into uppercase
print(course.lower()) #lowercase
print(course.find('P')) #find method which returns the index
print(course.find('Beginners')) #Bosluklari da saydigindan 11. indexi verir.
print(course.replace('Beginners','Absolute Beginners')) #replace method for replacing 
#characters and words in a string
print('Python' in course)
print('python' in course)
