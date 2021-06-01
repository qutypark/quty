#스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return
# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

# 조합: (a+1)(b+1)(c+1)-1
# 1은 아무것도 입지 않았을 경우

from collections import Counter

def solution(clothes):
    answer = 1
    c = Counter([x[1] for x in clothes])
    for v in c.values():
        answer *= (v+1)
    answer -= 1
    return answer
