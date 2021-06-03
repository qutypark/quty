# 프로그래머스_탐욕법(그리디)_조이스틱

# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return

# 반례 존재
def solution(name):
    ini = string.ascii_uppercase.index(name[0])
    end = string.ascii_uppercase.index("Z")
    ans = min(ini, end-ini+1)
    if name[1] == 'A':
        ans += 1
        for i in range(len(name)-1, 1, -1):
            idx = string.ascii_uppercase.index(name[i])
            m = min(idx, (end-idx+1))
            ans += m
            if i > 2:
                ans += 1
    else:
        for i in range(1, len(name)):
            idx = string.ascii_uppercase.index(name[i])
            m = min(idx, (end-idx+1))
            ans += m+1
    return ans
