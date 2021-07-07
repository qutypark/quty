---
title: “Programmers_Python_모든문제_오픈채팅방"
date: 2021-07-07
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/42888)


### 프로그래머스_모든문제_오픈채팅방

채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때,<br> 
모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return
<br>
- record 예시
  > Enter : "Enter uid1234 Muzi"<br> 
  > Leave : "Leave uid1234"<br> 
  > Change: "Change uid4567 Ryan"<br> 
<br> 
<details>
  <summary>문제설명</summary>

채팅방에 누군가 들어오면 다음 메시지가 출력된다.<br>
"[닉네임]님이 들어왔습니다."<br>
채팅방에서 누군가 나가면 다음 메시지가 출력된다.<br>
"[닉네임]님이 나갔습니다."<br>
 <br>
채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.<br>
  > 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.<br>
  > 채팅방에서 닉네임을 변경한다.<br>
 <br>
닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.
 <br>
 <br>
- 제한조건 <br>
  채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못 된 입력은 주어지지 않는다.

</details>

### 풀이방법

1. 변경된 닉네임을 갱신하는 딕셔너리
2. Change를 제외한 상태(Enter / Leave) 딕셔너리 생성
3. 각 딕셔너리 값을 이용해 메세지 생성 


#### 코드

```python
def solution(phrase):
    # renew nickname
    nic_dic = {}
    for p in phrase:
        tmp = p.split(" ")
        if tmp[0] != 'Leave':
            nic_dic[tmp[1]] = tmp[-1]

    # status dic
    st_dic = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}

    # message
    mes = []
    for p in phrase:
        spl = p.split(" ")
        if spl[0]!="Change":
            tmp = nic_dic[spl[1]]+"님이 "+st_dic[spl[0]]
            mes.append(tmp)
    return mes
```

