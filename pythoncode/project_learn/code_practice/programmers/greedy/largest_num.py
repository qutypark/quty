# 프로그래머스_탐욕법(Greedy)_큰 수 만들기
# 문자열 형식의 숫자 number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return

# 조합을 이용 -> 시간 효율 떨어지는 답
from itertools import combinations

def solution(num, k):
    comb = list(combinations(list(range(len(num))), k))
    ans = "0"*k
    for e in comb:
        l0 = e[0]
        str0 = num[:l0]
        for i in range(k-1):
            str0 += num[e[i]+1:e[i+1]]
        str0 += num[e[-1]+1:]
        ans = max(ans, str0)
    return ans
  
# 좋은 답안 예시: 
def solution(number, k):
    stack = [number[0]] # stack에 입력값을 순서대로 삽입 
    for num in number[1:]: # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈 
        while len(stack) > 0 and stack[-1] < num and k > 0: 
            k -= 1 # k: -1씩 감소
            stack.pop() # 내부의 값을 제거 
        stack.append(num) # 새로운 값을 삽입
    if k != 0:# 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
        stack = stack[:-k]# 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문 
    return ''.join(stack)
