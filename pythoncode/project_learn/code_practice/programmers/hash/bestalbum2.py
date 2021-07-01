# 프로그래머스_해쉬_베스트앨범

# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return

# genre = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]	

#풀이방식_1: 딕셔너리
#defaultdict와 operator를 이용한 정렬
# - 딕셔너리1: 장르 별, 플레이 숫자와 인덱스 위치를 삽입하는 딕셔너리
#     > operator를 이용해 플레이 숫자 기준으로 내림차순 정렬
# - 딕셔너리2: 장르 KEY, 플레이 숫자의 합 VALUE
#     > lambda를 이용해, 플레이 숫자 합 기준으로 내림차순 정렬
# - 딕셔너리2의 키 순서대로, 딕셔너리1의 인덱스 위치를 2개(1개밖에 없다면 1개만)

from collections import defaultdict
import operator

def solution(genres, plays):
    dic = defaultdict(list) # 딕셔너리 1
    genre_dic = {} # 딕셔너리 2

    for i in range(len(genres)):
        dic[genres[i]].append([i, plays[i]])
    for k in dic:
        tmp = 0
        for e in dic[k]:
            tmp += e[-1]
        genre_dic[k] = tmp
        dic[k] = sorted(dic[k], key=operator.itemgetter(1), reverse=True) # 딕셔너리 1 정렬

    genre_dic = {k: v for k, v in sorted(genre_dic.items(), key=lambda item: item[1], reverse=True)} #딕셔너리 2 정렬

    ans = []
    for k in genre_dic.keys(): # 딕셔너리2의 키 순서대로, 
        if len(dic[k]) >= 2:
            for i in range(2): # 딕셔너리1의 인덱스 위치를 2개
                ans.append(dic[k][i][0])
        else: # 1개밖에 없다면 1개만
            ans.append(dic[k][0][0])
    return ans
