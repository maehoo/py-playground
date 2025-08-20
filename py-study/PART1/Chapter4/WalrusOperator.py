#바다코끼리 연산자
#':='가 바다코끼리처럼 생겼다해서 바다코끼리 연산자라고 한다.

"""
tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >=0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))
"""
#>>> A fitting tweet

tweet_limit = 280
tweet_string = "Blah" * 50
if diff := tweet_limit - len(tweet_string) >=0:
    print("A fitting tweet")
else:
    print("Went over by" , abs(diff))
#>>> A fitting tweet

