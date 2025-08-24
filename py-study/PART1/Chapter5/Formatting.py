#{}.format()
thing = "woodchuck"
place = "lake"
print("{}".format(thing))
'''>>> woodchuck'''
print('The {} is in the {}'.format(thing,place))
'''>>> The woodchuck is in the lake'''

#위치별로 인수를 지정할 수 있다.
print('The {1} is in the {0}'.format(thing,place))
'''>>> The lake is in the woodchuck'''
#값 0은 첫 번째 인수 thing을 나타내고, 값 1은 두 번째 인수 place를 나타낸다.

#딕셔너리로도 사용 가능하다.
dictt = {'thing' : 'duck', 'place' : 'bathtub'}
print('The {0[thing]} is in the {0[place]}'.format(dictt))
'''>>> The duck is in the bathtub'''



#문자열 정의
'''
1. 맨 처음 콜론(:)이 온다.
2. 채우기 문자(옵션): 문자열이 최소 너비보다 짧은 경우, 이 문자로 채운다(기본값'')
3. 선택적 정렬 문자(옵션): 왼쪽 정렬이 기본값이다. '<'는 왼쪽 정렬, '>'는 오른쪽 정렬. '^'는 가운데 정렬이다.
4. 숫자에 대한 부호 문자(옵션): 기본값으로 음수에만 부호('-')가 붙는다. '-'는 음수에 부호가 붙고, 양수에 공백(' ')을 붙인다.
5. 최소 너비(옵션): 최소 너비 및 최대 문자를 구분한다.
6. 최대 문자(옵션)
7. 변환 타입
'''
thing2 = 'wraith'
place2 = 'window'
print('The {} is at the {}'.format(thing2,place2))
'''>>> The wraith is at the window'''

print('The {:10s} is at the {:10s}'.format(thing2,place2))
'''>>> The wraith     is at the window    '''

print('The {:<10s} is at the {:<10s}'.format(thing2,place2))
'''>>> The wraith     is at the window    '''

print('The {:^10s} is at the {:^10s}'.format(thing2,place2))
'''>>> The   wraith   is at the   window   '''

print('The {:>10s} is at the {:>10s}'.format(thing2,place2))
'''>>> The     wraith is at the     window'''

print('The {:!^10s} is at the {:!^10s}'.format(thing2,place2))
'''>>> The !!wraith!! is at the !!window!!'''




#f-문자열
#첫 인용 부호 앞에 문자 f 또는 F를 입력한다.
#변수 이름이나 식을 중괄호 안에 포함해 값을 문자열로 가져온다.

thing3 = 'wereduck'
place3 = 'werepond'
print(f'The {thing3} is in the {place3}')
'''>>> The wereduck is in the werepond'''

#중괄호 안에 표현식을 사용할 수 있다.
print(f'The {thing3.capitalize()} is in the {place3.rjust(20)}')
'''>>> The Wereduck is in the             werepond'''
#capitalize = 문자열 맨앞의 문자를 대문자로 만든다.
#rjust = 오른쪽 정렬

#format 메서드에서 수행할 수 있는 정의가 사용 가능하다.
print(f'The{thing3:>20} is in the {place3:.^20}')
'''>>> The            wereduck is in the ......werepond......'''

#이름과 값을 '='을 이용해 출력 가능하다.
print(f'{thing3 =}, {place3 =}')
'''>>> thing3 ='wereduck', place3 ='werepond'''

print(f'{thing3 = :>20.5}')
'''>>> thing3 =                wered'''
