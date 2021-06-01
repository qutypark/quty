# 프로그래머스_완전탐색_소수 찾기

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 
# numbers = "17"

from itertools import permutations

def solution(num):
    # 1. 만들 수 있는 모든 수의 조합
    lis = []
    for i in range(1, len(num)+1):
        a = list(permutations(num, i))
        for e in a:
            t = int(''.join(e))
            if t not in lis:
                lis.append(t)

    # 2. 소수의 리스트를 만듦: (에라토스테네스의 체)를 통해
    n = int(max(lis))
    a = [False,False] + [True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    # 최종. 만들 수 있는 모든 수 조합 중 소수 리스트에 해당되는 카운트
    cnt = 0
    for e in lis:
        if e in primes:
            cnt += 1
    return cnt
  
  
