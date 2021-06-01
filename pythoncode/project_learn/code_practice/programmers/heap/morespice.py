# 프로그래머스_힙_더 맵게
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 계산식으로 섞어 새로운 음식을 만듭니다.
# 계산식: 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

# 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
# 불가능하면  -1 return

# heapq를 이용

import heapq 
def solution(sco,k):
    cnt=0
    h=[]
    for e in sco:
        heapq.heappush(h,e)
    while h[0]<k:
        try:
            heapq.heappush(h,(heapq.heappop(h)+heapq.heappop(h)*2))
        except:
            return -1
        cnt+=1
    return cnt
