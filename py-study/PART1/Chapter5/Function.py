#문자열 길이 : len()
letters = 'abcdefghijklmnopqrstuvwxyz'
print(len(letters))
'''>>> 26'''
empty = ''
print(len(empty))
'''>>> 0'''



#문자열 나누기 : split()
#문자열 이름을 입력하고 .을 입력한 후 함수 이름과 인수를 입력한다. 
#어떤 구분자를 기준으로 하나의 문자열을 작은 문자열들의 리스트로 나누기 위해서는 문자열 내장 함수 split()을 사용한다.
tasks = 'get gloves, get mask, give cat vitamins, call ambulance'
print(tasks.split(','))
'''>>> ['get gloves', ' get mask', ' give cat vitamins', ' call ambulance']'''
#구분자를 지정하지 않으면 split()는 문자열에 등장하는 공백 문자(줄바꿈, 스페이스, 탭)를 구분자로 사용한다.
print(tasks.split())
'''>>> ['get', 'gloves,', 'get', 'mask,', 'give', 'cat', 'vitamins,', 'call', 'ambulance']'''



#문자열 결합하기 : join()
#join() 메서드는 split() 메서드와 반대로 문자열 리스트를 하나의 문자열로 결합한다.
#결합할 문자열을 지정한 다음에 문자열 리스트를 결합한다.
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
crypto_string2 = ' and '.join(crypto_list)
print(crypto_string)
'''>>> Yeti, Bigfoot, Loch Ness Monster'''
print(crypto_string2)
'''>>> Yeti and Bigfoot and Loch Ness Monster'''



#문자열 대체하기: replace()
setup = 'a duck goes into a bar..'
print(setup.replace('.', ',,'))
'''>>> a duck goes into a bar,,,,'''
#뒤에 숫자 인수를 추가하면 바꿀 문자열에 대한 횟수를 설정할 수 있다.
print(setup.replace('.',',,',1))
'''>>> a duck goes into a bar,,.'''
#주의 단어 중간에 있는 문자도 바뀔 수 있다는 점을 주의해야 한다.
print(setup.replace('o', 'blah'))
'''>>> a duck gblahes intblah a bar..'''



#문자열 스트립: strip()
#문자열 맨 앞 또는 맨 뒤에서 '패딩'문자(여백 또는 공백 문자)를 제거하는 함수이다.
#인수가 엇다면 공백 문자(' ','\t', '\n')
#앞쪽만 제거하고 싶다면 lstrip()를 뒤쪽만 제거하고 싶다면 rstrip()을 사용한다.
world = " earth "
print(world.strip())
print(world.strip(' '))
'''>>> "earth"'''
print(world.lstrip())
'''>>> "earth "'''
print(world.rstrip())
'''>>> " earth"'''

#문자열에서 strip()메서드에 해당하는 인수가 없다면 아무 일도 일어나지 않는다.
print(world.strip('!'))
'''>>> " earth "'''

#단일 문자 또는 여러 문자의 이수를 취해서 해당 문자열을 제거할 수 있다.
blurt = "what the ..!..!?"
print(blurt.strip('?.!'))
'''>>> what the'''