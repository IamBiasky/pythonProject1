# print('multiplication table from 1 to 10.')

print(f'{" ":>1}  {"1":>4} {"2":>4} {"3":>4} {"4":>4} {"5":>4} {"6":>4} {"7":>4} {"8":>4} {"9":>4} {"10":>4} {"11":>4}\
 {"12":>4}')

for number in range(1, 12):
    print(f'{number:>2} {number*1:>4} {number*2:>4} {number*3:>4} {number*4:>4} {number*5:>4} {number*6:>4}\
 {number*7:>4} {number*8:>4} {number*9:>4} {number*10:>4} {number*11:>4} {number*12:>4}')
