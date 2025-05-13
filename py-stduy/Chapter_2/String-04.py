# 9. 문자열 관련 함수들

# 문자 개수 세기 - count
s = "hobby"
loc = s.count('b')
print(loc)   # 출력값 2

# 위치 알려 주기 - find
a1 = "python is the best choice"
loc = a1.find('b')      # 출력값 14   인덱스 값을 반환해서 15가 아닌 14가 반환
loc2 = a1.find('k')     # 출력값 -1   존재하지 않으면 -1

# 위치 알려 주기 2 - index
a2 = "life is too short"
loc = a2.index('t')     # 출력값 8
loc2 = a2.index('k')    # 출력 오류!
# find와 차이점은 index는 존재하지 않으면 오류가 발생한다.

# 문자열 삽입 - join
a3 = ",".join('abcdsa')
print(a3)   # 출력값 a,b,c,d,s,a
a3 = ",".join(['a','b','c','d'])
print(a3)   # 출력값 a,b,c,d

# 소문자를 대문자로 바꾸기 - upper
a4 = 'hi'
result = a4.upper()
print(result)   # HI

# 대문자를 소문자로 바꾸기 - lower
a4 = 'HI'
result = a4.lower()
print(result)   # hi

# 왼쪽 공백 지우기 - lstrip
a5 = "  d  hi  d  "
result = a5.lstrip()
print(result)   # "d  hi  d  " 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다.

# 오른쪽 공백 지우기 - rstrip
result = a5.rstrip()
print(result)   # "  d  hi  d" 가장 오른쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다.

# 문자열 바꾸기 - replace
a6 = "life is too short"
result = a6.replace("life", "your leg")
print(result)   # your leg is too short

# 문자열 나누기 - split
a7 = "life is too short"
result = a7.split()
print(result)   # ['life', 'is', 'too', 'short'] 
b = "a:b:c:d"
result = b.split(":")
print(result)   # ['a', 'b', 'c', 'd']
# split()의 괄호 안에 아무 값도 넣지 않으면 공백(space, tab, enter)을 기준으로 문자열을 나눈다.
# 괄호 안에 ":" 처럼 특정 값이 있으면 그 값을 구분자로 해서 문자열을 나눈다.
# 나눈 값은 !!리스트!!에 하나씩 들어간다.

# 문자열이 알파벳으로만 구성되어 있는지 확인하기 - isalpha
a8 = "python"
result = a8.isalpha()   
print(result)           # True
a8 = "python3"
result = a8.isalpha()   
print(result)           # False
a8 = "hi hello"
result = a8.isalpha()
print(result)           # False
#문자열이 알파벳 문자로만 이루어져 있는지 검사한다. 숫자나 공백, 특수 문자가 포함되어 있으면 False를 반환한다.

# 문자열이 숫자로만 구성되어 있는지 확인하기 - isdigit
a9 = "12345"
result = a9.isdigit()
print(result)           # True
a9 = "1234a"
result = a9.isdigit()
print(result)           # False
a9 = "12 34"
result = a9.isdigit()
print(result)           # False

#문자열이 특정 문자(열)로 시작하는지 확인하기 - startwith
a10 = "life is too short"
result = a10.startswith("life") 
print(result)                       # True
result = a10.startswith("short") 
print(result)                       # False
result = a10.startswith("li")
print(result)                       # True

#문자열이 특정 문자(열)로 끝나는지 확인하기 - endswith
a11 = "life is too short"
result = a11.endswith("short")  
print(result)                       # True
result = a11.endswith("too")
print(result)                       # False
result = a11.endswith("rt")
print(result)                       # True