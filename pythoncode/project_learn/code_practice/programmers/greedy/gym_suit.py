# 프로그래머스_그리디_체육복

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
# 체육수업을 들을 수 있는 학생의 최댓값을 return 

# 제한1. 전체 학생의 수는 2명 이상 30명 이하입니다.
# 제한2. 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 제한3. 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 제한4. 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 제한5. 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

def solution(n, los, res):
  los1 = list(set(los).difference(res))
  res1 = list(set(res).difference(los))

  ans = int(n-len(los1))

  los1.sort()
  res1.sort()

  for r in res1:
      if not los1:
        break
      for lo in los1:
          if lo == r-1 or lo == r+1:
              ans += 1
              los1.remove(lo)

  return ans
