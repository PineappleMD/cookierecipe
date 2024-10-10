number_of_cookies = int(input('\nHow many cookies would you like to make: ')) #25, 80


COOKIES = 48
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75

totalSugar  = (SUGAR * number_of_cookies) / COOKIES
totalButter = (BUTTER * number_of_cookies) / COOKIES
totalFlour  = (FLOUR * number_of_cookies) / COOKIES


print('\nNumber of cookies =', number_of_cookies, end='\n\n')
print('Total sugar =', format(totalSugar, ',.2f'))
print('Total butter =', format(totalButter, ',.2f'))
print('Total flour =', format(totalFlour, ',.2f'), end='\n\n') 
#25 cookies: Sugar - 0.78; Butter - 0.52; Flour - 1.43;
#80 cookies: Sugar - 2.5; Butter - 1.67; Flour - 4.58;
