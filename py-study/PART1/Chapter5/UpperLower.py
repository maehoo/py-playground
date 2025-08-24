#대소 문자
sentence = "aaaa duck goes into a bar"

#첫 번째 문자를 대문자로 만든다.
print(sentence.capitalize())
'''>>> Aaaa duck goes into a bar'''
#모든 단어의 첫 번째 문자를 대문자로 만든다.
print(sentence.title())
'''>>> Aaaa Duck Goes Into A Bar'''
#모든 글자를 대문자로 만든다.
print(sentence.upper())
'''>>> AAAA DUCK GOES INTO A BAR'''

sentence2 = "AAAA DUCK GOES INTO A BAR"
#모든 글자를 소문자로 만든다.
print(sentence2.lower())
'''>>> aaaa duck goes into a bar'''

sentence3 = "aaaa duck GOES INTO A BAR"
#대문자는 소문자로, 소문자는 대문자로 만든다.
print(sentence3.swapcase())
'''>>> AAAA DUCK goes into a bar'''
