


var1 = input('Invoer 1: ')
var2 = input('Invoer 2: ')

print('')
print(f'{var1} == {var2}:', var1 == var2) 
print(f'{var1} != {var2}:', var1 != var2) 

print('')
print(f'{var1} > {var2}:', var1 > var2)
print(f'{var1} >= {var2}:', var1 >= var2)

print('')
print(f'{var1} <= {var2}:', var1 <= var2)
print(f'{var1} < {var2}:', var1 < var2)

# we lossen misschien wat problemen op
import random

favoriteColor = input('En wat is je favoriete kleur?') 
trueOrFalse = bool(random.randint(0,1))
if trueOrFalse == True:
 print('Ik vind dat ook een mooie kleur!')
elif trueOrFalse == False:
 print(f'{favoriteColor}? wat een kak kleur.')



# We bekijken de volgende foute code en lossen de problemen op
# en maken het netter
# favoriteColor = input('En wat is je favoriete kleur? ') 
# trueOrFalse = str(random.randint(0,1))
# if trueOrFalse = True:
# print('Ik vind dat ook een mooie kleur!')
# elif trueOrFalse = False:
# print('TBH, ik hou niet zo van {}...'.format(favoritecolor))