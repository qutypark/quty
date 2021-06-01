# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구함
# ex) array = [1, 5, 2, 6, 3, 7, 4] /  i = 2, j = 5, k = 3 
# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]
# 2에서 나온 배열의 3번째 숫자는 5

def solution(array, commands):
    ans = []
    for c in commands:
        temp = array[c[0]-1:c[1]]
        temp.sort()
        r = c[-1]-1
        ans.append(temp[r])
    return ans
