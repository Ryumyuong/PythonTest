first, last, addm, count = 0, 0, 0, 0

first = int(input("*** 첫번째 숫자를 입력하세요 : "))
last = int(input("*** 두번째 숫자를 입력하세요 : "))
add = int(input("*** 더할 숫자를 입력하세요 : "))



for i in range(first, last + 1, add) :
    count += i

print(" %d + %d + ... + %d는 %d입니다." % (first, first + add, last, count))