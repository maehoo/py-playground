# 3. 리스트의 수정과 삭제


# 리스트 값 수정
a = [1,2,3]
a[2] = 4
print(a)        # [1, 2, 4]

# 리스트 요소 삭제하기
a = [1,2,3]
del a[1]
print(a)        # [1, 3]

a = [1,2,3,4,5]
del a[2:]
print(a)        # [1, 2]





# 4. 리스트 관련 함수


# 리스트에 요소 추가하기 - append
a1 = [1,2,3]
a1.append(4)
print(a1)       # [1, 2, 3, 4]
a1.append([5,6])
print(a1)       # [1, 2, 3, 4, [5, 6]] 리스트 자체를 배열요소로 넣음
a1.append(5,6,7)
print(a1)       # 오류 append()는 인자를 하나만 받을 수 있는 함수기 때문

# 리스트 정렬 - sort
a2 = [2,4,3,1]
a2.sort()
print(a2)       # [1, 2, 3, 4]

a2.sort(reverse = True)
print(a2)       # [4, 3, 2, 1]

# 리스트 뒤집기 - reverse
a3 = ['a','c','b']
a3.reverse()
print(a3)       # ['b', 'c', 'a']

# 인덱스 반환 - index
a4 = [1,2,3,4]
result = a4.index(3)
print(result)   # 2  index(x) 함수는 리스트에 'x' 값이 있으면 'x'의 인덱스 값(위칫값)을 반환한다.
print(a4.index(1))# 0
#값이 존재하지 않으면 오류가 발생한다.

# 리스트에 요소 삽입 - insert
a5 = [1,2,3,4]
a5.insert(0,5) #insert(a,b) 리스트의 인덱스a번째 위치에 b를 삽입하는 함수
print(a5)       # [5, 1, 2, 3, 4]
a5.insert(3,6)
print(a5)       # [5, 1, 2, 6, 3, 4]

# 리스트 요소 제거 - remove
a6 = [1,2,3,1,2,3]
a6.remove(3)
print(a6)       # [1, 2, 1, 2, 3] 리스트에서 첫 번째로 나오는 인자를 삭제하는 함수.
a6.remove(3)
print(a6)       # [1, 2, 1, 2]

# 리스트 요소 끄집어 내기 - pop
a7 = [1,2,3]
print(a7.pop()) # 3
print(a7)       # [1, 2]
# pop()은 리스트의 맨 마지막 요소를 반환하고 그 요소는 삭제한다.
a7 = [1,2,3]
print(a7.pop(1))# 2
print(a7)       # [1, 3]

# 리스트에 포함된 요소 x의 개수 세기 - count
a8 = [1,2,3,4,1]
print(a8.count(1)) # 2
#count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 반환한다.

# 리스트 확장 - extend
a9 = [1,2,3]
a.extend([4,5])
print(a9)       # [1, 2, 3, 4, 5] a9.extend([4,5])는 a9 += [4,5] 와 똑같다.
b1 = [6,7]
a9.extend(b1)
print(a9)       # [1, 2, 3, 4, 5, 6, 7]