# 1. ' 와 " 사용하는 방법


a = "python's favorite food is perl" #성립 작은 따옴표를 쓰고 싶으면 큰 따옴표로 둘러싸면 된다.

b = 'python's favorite food is perl' #오류 발생 'python'이 문자열로 인식되어 오류가 발생함.

c = '"python is very easy." he says.' #성립 큰 따옴표를 쓰고 싶으면 작은 따옴표로 둘러싸면 된다.

# 참조 \' , \"도 가능 C언어와 똑같음





# 2. \n (이스케이프 코드)


a = "Hello\nWorld!"  #읽기가 불편함.
b = """
Hello
world
"""                 # """, '''로 해결 가능






# 3. 문자열 연산하기

#합
head = "python"
tail = " is fun!"
head + tail
---> python is fun    # 성립

#곱
a = 'python'
a * 2
---> pythonpython     # 성립

#곱 응용
print("=" *10)
---> ==========

