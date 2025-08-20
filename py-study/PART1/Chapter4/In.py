#in을 이용하여 여러 개 비교하기
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')
#>>> o is a vowel

#파이썬 멤버십 연산자
vowels = "aeiou"
print(letter in vowels)
#>>> True

if letter in vowels:
    print(letter, "is a vowel")
#>>> o is a vowel

vowel_set = {'a','e','i','o','u'}
print(letter in vowel_set)
#>>> True

vowel_list = ['a','e','i','o','u']
print(letter in vowel_list)
#>>> True

vowel_tuple = ('a','e','i','o','u')
print(letter in vowel_tuple)
#>>> True

vowel_string = "aeiou"
print(letter in vowel_string)
#>>> True

vowel_dict = {'a' : 'apple', 'e' : 'elephant', 'i' : 'impala', 'o' : 'ocelot' , 'u' : 'unicorn'}
print(letter in vowel_dict)
#>>> True
