#다음은 모두 False로 간주된다.
"""
null            none
정수 0           0
부동소수점 0      0.0
빈 문자열         ' '
빈 리스트         [ ]
빈 튜플          ()
빈 딕셔너리       {}
빈 셋           set()
"""
#이 외에 다른 것들은 True로 간주된다.

some_list = []
if some_list:
    print("There's something in here")
else:
    print("It's a empty!")
#>>> It's a empty!
