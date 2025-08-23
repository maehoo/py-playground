#문자 추출: []
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
'''>>>a'''
print(letters[1])
'''>>>b'''
print(letters[-1])
'''>>>z'''
print(letters[-2])
'''>>>y'''


#슬라이스
name = 'Henny'
#name[0] = 'P'  (X)
#문자열은 불변하기 때문에 특정 인덱스에 문자를 삽입하거나 변경할 수 없다. 

print(name.replace('H','P'))
'''>>>Penny'''
print('P' + name[1:])
'''>>>Penny'''
print(name)
'''>>>Henny'''
#name의 문자열을 바꾸는 것이 아닌 출력과정에서만 바꿔서 출력하는 것 뿐이다.

#슬라이스를 사용하여 한 문자열에서 문자열 일부를 추출할 수 잇다.
"""
[:] : 처음부터 끝가지 전체 시퀀스를 추출한다.
[start:] : start 오프셋부터 끝까지 시퀀스를 추출한다.
[:end] : 처음부터 (end - 1) 오프셋까지 시퀀스를 추출한다.
[start:end] : start 오프셋부터 (end - 1) 오프셋부터 시퀀스를 추출한다.
[start:end:step] : step만큼 문자를 건너뛰면서, start 오프셋부터 (end - 1)오프셋까지 시퀀스를 추출한다.
"""

print(letters[:])
'''>>>abcdefghijklmnopqrstuvwxyz'''
print(letters[20:])
'''>>>uvwxyz'''
print(letters[10:])
'''>>>klmnopqrstuvwxyz'''
print(letters[12:15])
'''>>>mno'''
print(letters[-3:])
'''>>>xyz'''
print(letters[18:-3])
'''>>>stuvw'''
#앞의 예제처럼 시작 오프셋에 -3을 지정하면 x가 되지만, 끝 오프셋에 -3을 지정하면 -4번째 문자인 w가 된다.
print(letters[-6:-2])
'''>>>uvwx'''
print(letters[::7])
'''>>>ahov'''
print(letters[4:20:3])
'''>>>ehknqt'''
print(letters[19::4])
'''>>>tx'''
print(letters[:21:5])
'''>>>afkpu'''

#스텝을 음수로 지정하면 역순으로 출력도 가능하다.
print(letters[-1::-1])
print(letters[::-1])
'''>>>zyxwvutsrqponmlkjihgfedcba'''

#슬라이스는 첫 번째 문자열 이전의 슬라이스오프셋은 0으로 간주하고, 마지막 다음 오프셋은 -1로 간주한다.
print(letters[-50:])
print(letters[:70])
'''>>>abcdefghijklmnopqrstuvwxyz'''