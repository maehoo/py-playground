# 7. format함수, f문자열 포매팅


print("I eat {0} apples".format(3))  #{0} 여기서'0'은 format의 몇 번째 값을 쓰겠냐는 의미, 그래서 3은 인덱스 0에 있는 값이어서 3을 불러옴.
print("I eat {0} apples".format("five"))
number = 3
print("I eat {0} apples".format(number))
day = "three"
print("{0} apples. {1} days".format(number,day))
print("{0} apples. {0} days".format(number))

#정렬
print("{0:>10}".format("five")) # 10칸의 자릿수를 가지고 오른쪽 정렬 
print("{0:<10}".format("five")) # 10칸의 자릿수를 가지고 왼쪽 정렬 
print("{0:^10}".format("hi"))   # 10칸의 자릿수를 가지고 가운데 정렬
print("{0:-^10}".format("hi"))  # 출력값 ----hi----
#<,>,^ 앞에 지정한 문자를 넣으면 빈 공간을 지정한 문자로 채운다.

#소수점 표현하기
y = 3.141592
print("{0:0.4f}".format(y))
print("{0:10.04f}".format(y)) # "3.1416" 자릿수 10, 소수점 4자리까지 표현

print("{{and}}".format()) # "{and}" {}를 문자 그대로 사용하고 싶은 경우에는 {{}}처럼 2개를 연속으로 사용하면 된다.





# 8. f문자열 포매팅


name = "홍길동"
age = 30
print(f"나의 이름은 {name}. 나이는 {age}입니다")
print(f"{age +1}")

d = {'name' : '홍길동', 'age' : 100}
print(f"나의 이름은{d['name']}.나이 {d['age']}")

print(f"{'hi':<10}")
x = 3.141592
print(f"{x:10.4f}")
print(f"{{and}}")

# ','삽입
print(f"{1500000000:,}")