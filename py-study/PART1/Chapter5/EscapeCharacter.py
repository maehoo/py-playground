#문자열

#문자열 포매팅
print(str(98.6))
print(str(1.0e4))
print(str(True))
#str()을 사용하여 문자열이 아닌 객체를 문자열로 바꿀수 있다.



#줄바꿈 \n

palindrome = 'A man, \n A plan, \n A canal, :\nPanama'
print(palindrome)
"""
>>>A man,
A plan,
A canal, :
 Panama.
"""



#tab \t

print('\tabc')
#>>>    abc

print('a\tbc')
#>>>a   bc

print('ab\tc')
#>>>ab  c



#따옴표 \",\'

testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
print(testimony)
#>>>"I did nothing!" he said. "Or that other thing."

fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'"
print(fact)
#>>> The world's largest rubber duck was 54'2" by 65'7" by 105'



#백슬래시 \\

speech = 'The backslash (\\) bends over backwards to please you'
print(speech)
#>>> The backslash (\) bends over backwards to please you.



#원시 문자열
info = r'Type a \n to get a new line in a normal string'
print(info)