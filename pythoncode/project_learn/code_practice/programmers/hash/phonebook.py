# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return

# pb = ["97674223", "119", "1195524421"]

# startswith 함수 이용
def solution(pb):
    # 1. 정렬
    pb = sorted(pb)
    # 2. 전 요소가 그 후 요소의 접두어가 되는지를 확인
    for p1, p2 in zip(pb, pb[1:]):
        if p2.startswith(p1):
            return False
    return True

