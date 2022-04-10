'''

Random Password Generator using Python


'''

import secrets 
import string

pasw=secrets.SystemRandom() 
print('\n\n******************Hello, Welcome to Password Generator!******************\n')


length = int(input('\nEnter the length of password: '))                      


lower = string.ascii_lowercase

upper = string.ascii_uppercase

num = string.digits

symbols = string.punctuation


print('Choices are\n')

print('1-Password including only numbers\n')

print('2-Password including lower case\n')

print('3-Password including upper case\n')

print('4-Password including only symbols\n')

print('5-Password including lower case + symbol\n')

print('6-Password including  symbols + upper case\n')

print('7-Password including numbers + symbols\n')

print('8-Password including upper case + numbers\n')

print('9-Password including lower case + numbers\n')

print('10-Password including lower case + upper case\n')

print('11-Password including lower case + upper case + numbers\n')

print('12-Password including lower case + numbers + symbols\n')

print('13-Password including upper case + numbers + symbols\n')

print('14-Password including lower case + upper case + symbols\n')

print('15-Password including lower case + upper case + symbols + numbers\n')

ch=int(input('\nEnter your choice\n'))


if ch==1:
    temp = pasw.sample(num,length)
    print(*temp) 

elif ch==2:
    temp = pasw.sample(lower,length)
    print(temp)

elif ch==3:
    temp = pasw.sample(upper,length)
    print(*temp)

elif ch==4:
    temp = pasw.sample(symbols,length)
    print(*temp)

elif ch==5:
    all = lower+symbols
    temp = pasw.sample(all,length)
    print(*temp)

elif ch==6:
    all = upper+symbols
    temp = pasw.sample(all,length)
    print(*temp)

elif ch==7:
    all = num+symbols
    temp = pasw.sample(all,length)
    print(*temp)

elif ch==8:
    all = upper+num
    temp = pasw.sample(all,length)
    print(*temp)

elif ch==9:
    all = lower+num
    temp = pasw.sample(all,length)
    print(*temp)

elif ch==10:
    all = lower+upper
    temp = pasw.sample(all,length)
    print(*temp)

elif ch==11:
    all = lower+upper+num
    temp = pasw.sample(all,length)
    print(*temp)

elif ch==12:
    all = lower+symbols+num
    temp = pasw.sample(all,length)
    print(*temp)

elif ch==13:
    all = upper+num+symbols
    temp = pasw.sample(all,length)
    print(*temp)

elif ch==14:
    all = lower+upper+symbols
    temp = pasw.sample(all,length)
    print(*temp)

elif ch==15:
    all = lower+upper+num+symbols
    temp =  pasw.sample(all,length)
    print(*temp)

else:
    print('Wrong choice entered')
