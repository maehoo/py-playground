#if
disaster = \
    True                # 문장 끝에 '\'를 붙이면 다음 줄로 이어서 명령어를 입력할 수 있다.
if disaster:
    print("woe!")
else:
    print("uu")
# >>>woe!


#else
furry = True
large = True
if furry:
    if large:
        print("It's a yeti!")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat!")
# >>> It's a yeti!


#elif
color = "mauve"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color",color)
# >>> I've never heard of the color mauve