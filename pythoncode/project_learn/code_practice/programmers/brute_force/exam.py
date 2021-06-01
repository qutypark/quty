# 프로그래머스_완전탐색_모의고사

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 
# 조건 :시험은 최대 10,000 문제로 구성

# answers = [1,2,3,4,5]
# ver1. 완전탐색
def solution(array):
    ans = []
    p1 = [1, 2, 3, 4, 5] * 2000
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * (int(10000 / 8))
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    n = len(array)
    a1, a2, a3= 0, 0, 0
    for i, e in enumerate(array):
        if e == p1[i]:
            a1 += 1
        if e == p2[i]:
            a2 += 1
        if e == p3[i]:
            a3 += 1
    m = max(a1, a2, a3)
    if m == a1:
        ans.append(1)
    if m == a2:
        ans.append(2)
    if m == a3:
        ans.append(3)
    ans.sort(reverse=False)
    return ans

# ver2. 순환 주기를 이용
def solution(answers):
    # 1번 2번 3번 수포자의 규칙을 정리
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            # 해당 답 인덱스를 수포자의 규칙 길이로 나눈 나머지는 '순환 주기'로 활용됨
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
  
