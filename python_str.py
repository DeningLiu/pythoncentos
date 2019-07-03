#/usr/bin/python3.6
# -*- coding=utf-8 -*-
# write by Darin

A = "fsfwefsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdsfdfadadfsdfasdf\
sdasdfadfadf"

print(A)

myjob = 'hacker'

for X in myjob:
    print(X)

department1 = 'Security'
department2 = 'Python'
depart1 = 'cqbomb'
depart2 = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_PYTHON = 1234.3456

line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f'%(department1,depart1,COURSE_FEES_SEC) + ' The End!'
line2 = 'Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f'%(department2,depart2,COURSE_FEES_PYTHON) + ' The End!'

#line1 =
#line2 =

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)


department1 = 'Security'
department2 = 'Python'
depart1 = 'cqbomb'
depart2 = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_PYTHON = 1234.3456


line1 = 'Department1 name:{0:10} Manager:{1:10} COURSE FEES:{2:<10.2f} The End!'.format('Security','cqbomb',\
                                                                                       456789.123456)
line2 = 'Department2 name:{0:10} Manager:{1:10} COURSE FEES:{2:<10.2f} The End!'.format('Python','qinke',1234.3456)

#line1 =
#line2 =

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)



if __name__ == '__main__':
    pass