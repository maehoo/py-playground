# 4. 문자열 길이 구하기

a = "Life is too short"
b = len(a)
print(b)   #17





# 5. 문자열 인덱싱과 슬라이싱

a = "life is too short, you need python"
b = a[3]
print(b)     #e

#역으로도 가능
a = "life is too short, you need python"
b = a[-1]
print(b)    #n
# 0과 -0은 똑같기 때문에 a[-0]으로 쓰지않고 a[-1]부터 시작

a = "life is too short, you need python"
b = a[0:4]
print(b)
# a[시작 번호: 끝 번호]로 지정되지만 끝 번호에 해당하는 문자는 포함하지 않음
# 0<= a <4 와 똑같은 상황
c = a[19:]
d = a[:17]
e = a[:]
# '시작 번호', '끝 번호' 생략 가능

a = "life is too short, you need python"
b = a[19:-7]
print(b)

#응용
a = "20250512sunny"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year, day, weather)

#문자열 변경
a = "apdle"
a[2] = 'p' #불가능
#!문자열!의 요솟값은 바꿀 수 없음




# 6. 문자열 포매팅

print("I eat %d apples" %3)
print("I eat %s apples" %"five")

number=3, day = "three"
print("I eat %d apples" %number)
print("I ate %d apples. so I was sick for %s days." %(number,day))

#%s
print("I have %s apples" %3)
print("My rate is %s" %4.23232)
# %s 는 정수나 소수를 !문자열로 바꾸어! 대입한다.

print("%d%" %98) # 오류
print("%d%%" %98)
print("%d %" %98) #오류
#문자열 포맷 코드가 앞에 있으면 '%'를 출력하기 위해서는 '%%'형태로 사용하여야 한다.

print("%10s" %"hi")             #'        hi' 전체길이 10을 오른쪽 정렬
print("%-10sapple" %"hi")       #'hi        apple' 전체길이 10을 왼쪽 정렬
print("%.4f" %3.421323123)     #'3.4213' 소수점 4번째 자리까지만 출력
print("%10.4f" %3.421323123)    #'    3.4213'