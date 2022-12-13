# 2. Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '2', '3')

a = ( "a", 'b', '2', '3' ,'c')
string =[]
number = []

for i in a:
    if i.isdigit() :
        number.append(i)
    else : string.append(i)

print(number)
print(string)
        