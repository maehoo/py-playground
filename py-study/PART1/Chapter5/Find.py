#검색
sentence = "I'm a student a"
word = 'a'
print(sentence.find(word))
'''>>> 4'''
print(sentence.rfind(word))
'''>>> 14'''

print(sentence.index(word))
'''>>> 4'''
print(sentence.rindex(word))
'''>>> 14'''
#find와 index 앞에 r을 붙일경우 오른쪽부터 단어를 찾아 그 부분의 오프셋을 출력한다.
#단어를 찾지 못할 경우 find는 -1을 출력하고 index는 예외가 발생한다.



#count
print(sentence.count(word))
'''>>> 2'''



#isalnum
print(sentence.isalnum())
'''>>> False'''
#알파벳 또는 숫자로 이루어져있는지 확인하는 것이다. 문장에 다른 문장 부호가 잇으므로 False가 출력된다.
sentence2 = "imastudent1234"
print(sentence2.isalnum())
'''>>> True'''