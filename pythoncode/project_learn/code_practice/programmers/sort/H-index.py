#프로그래머스_정렬_H-index

# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 

# lis = [3, 0, 6, 1, 5]
def solution(lis):
    ans = 0
    # 기준을 0부터 하나씩 늘려나감
    cnt = 0
    lis.sort()
    while cnt <= len(lis):
        tem = 0
        for e in lis:
            if e >= cnt:
                tem += 1
        if cnt <= tem:
            # h의 최댓값을 위해
            ans = max(ans, cnt)
            cnt += 1
        else:
            cnt += 1
    return ans
  
