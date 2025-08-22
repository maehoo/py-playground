#결합하기: +

# + 연산자를 사용하여 리터럴 문자열 또는 문자열 변수를 결합할 수 있다.
sentence = 'Release the kraken!' + ' No, wait'
print(sentence)
'''>>> Release the kraken! No, wait'''

#괄호로 묶어서 여러 줄에 걸쳐 문자열을 출력할 수 있다.
vowel = ('a'
         "e"
         '''i'''
         'o'
         """u""")
print(vowel)
'''>>> aeiou'''


#print()는 각 인수 사이에 공백을 붙인다. 마지막에는 줄바꿈 문자를 붙인다.
a = 'Duck.'
b = a
c = 'Grey Duck!'
print(a+b+c)
'''>>> Duck.Duck.Grey Duck'''
print(a,b,c)
'''>>> Duck. Duck. Grey Duck!
'''