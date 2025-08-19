#부동소수점 숫자
print(5.) #숫자 뒤에 '.'만 붙여도 부동소수점 숫자로 표현된다.

#부동소수점 숫자는 문자e와 정수인 지수를 포함할 수 있다.
print(5e0)
print(5e1)
print(5.0e1)

#소수점 뒷자리에도 '_'를 붙일 수 있다.
print(1.0_0_1)

print(float(True))  #1.0
print(float(False)) #0.0

#유효한 부동소수점 수(숫자, 지수, 기호, 소수점)가 있는 문자열을 부동소수점 수로 변활할 수 있다.
print(float('98.6'))
print(float('-1.5'))
print(float('1.0e4'))