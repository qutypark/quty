# 프로그래머스_완전탐색_카펫
# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return
# 제한1. 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수
# 제한2. 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수
# 제한3. 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 길다.

# 노랑벽돌과 갈색벽돌의 관계식을 찾아서 구현
def solution(br, ye):
    res = []
    ve, ho = 1, 1
    while ho >= ve:
        if ye % ve == 0:
            ho = int(ye/ve)
            temp = 2*(ho + 2) + 2*ve
            if temp == br:
                res = [ho+2, ve+2]
                break
            else:
                ve += 1
        else:
            ve += 1
    return res
