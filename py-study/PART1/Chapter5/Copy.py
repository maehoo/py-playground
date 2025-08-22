#복제하기: *
start = 'Na ' * 4 + '\n'
middle = 'Hey ' *3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)
""">>>
Na Na Na Na
Na Na Na Na
Hey Hey Hey
Goodbye.
"""
#*연산자는 + 연산자보다 우선순위가 높으므로 줄바꿈이 시작되기 전에 문자열이 결합된다.
