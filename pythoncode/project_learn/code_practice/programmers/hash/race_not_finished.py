# 완주하지 못한 선수  완주하지 못한 선수는 1명
def solution(part, com):
    dic = dict()
    for p in part:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    for c in com:
        dic[c] -= 1

    for k,v in dic.items():
        if v > 0:
            return k
