---
title: "ToDo-Hadoop-Map-Reduce"
date: 2021-04-12
categories: Hadoop
---

## ToDo-Hadoop; Map-Reduce 맵리듀스

#### 전반적인 내용은 아래의 강좌를 참고
Overview of Hadoop Ecosystem<br>
*Udemy의 [The Ultimate Hands-On Hadoop: Tame your Big Data!](https://www.udemy.com/course/the-ultimate-hands-on-hadoop-tame-your-big-data/) 

### Map-Reduce 맵리듀스 개요 <br>

- 맵리듀스란 무엇인가 <br>
: HDFS에서 작동하는 데이터 분산 프레임워크 [*관련내용; HDFS](https://tododata101.github.io/hadoop/todo-Hadoop1/)


- 왜 맵리듀스인가 <br>
*전제: 모든 일을 한번에 처리하는 것보다 각 라인에서 전문적으로 일을 처리하는 것이 생산적
 > 1. 클러스터 별로 대규모의 데이터 처리작업 분산 <br>
      (각 노드는 다른 노드에 대해 알 필요가 없으므로 병력적 작업에 용이해짐)<br>
 > 2. 데이터를 각 파티션으로 구분하여 <br>
      Key-Value 페어 집합으로의 출력 및 집계 가능<br>
 > 3. 실패에 대한 복원력이 강하다<br>
     (어플리케이션 매스터가 각 파티션의 매퍼와 리듀서를 모니터하기 때문)

- Key-Value 페이 집합이 이용되는 이유<br>
 > 1. 많은 실제 세상의 테스크가 표현 가능해지므로<br>
 > 2. 병렬 혹은 분산시스템에 대한 경험과 지식이 적어도 이용이 가능<br>
      (병렬화, 내결함성, 지역성 최적화 및 로드 밸런싱의 디테일이 숨겨있음)<br>
 > 3. 대용량 클러스터 소스를 효율적으로 사용 가능하므로<br>

### Map-Reduce 의 처리내용 <br>

#### Mapper 매퍼 <br>
- 주 역할: HDFS의 Raw source를 Key/Value 페어로 변환<br>
- 이점  : input data를 각각의 파티션으로 나누어 각 노드에 지정<br>
        -> 각 노드는 다른 노드에 대해 알 필요가 없으므로 병렬적 작업에 용이해짐

#### Shuffle & Sort <br>
- 주 역할: 같은 키를 가진 값을 묶어주는 역할<br>
  -> 이를 Reducer에 전송

#### Reducer 리듀서 <br>
- 주 역할: 각 키에 대한 밸류의 수를 집계 


### Map-Reduce 의 처리 예시 <br>

0. Input Data

|UserId|MovieId|
|------|---|
|196|242|
|186|302|
|196|377|
|186|548|

1. Mapper

1.1 각각의 파티션으로 나누어 각 노드에 지정

노드1 <br>
|UserId|MovieId|
|------|---|
|196|242|
|186|302|

노드2 <br>
|UserId|MovieId|
|------|---|
|196|377|
|186|548|

1.2 Key/Value 페어로 변환

노드1 <br>         
196:242<br>      
186:302<br>      

노드2 <br>
196:377<br>
186:548<br>

2. Shuffle & Sort

186: 301, 548<br>
196: 242, 377

3. Reducer

186: 2<br>
196: 2 

4. Back to Client Node



### 참고<br>
[1](https://data-flair.training/forums/topic/why-hadoop-mapreduce-uses-key-value-pair-to-process-the-data/)<br>
[2](https://kdata.or.kr/info/info_04_view.html?field=&keyword=&type=techreport&page=74&dbnum=153319&mode=detail&type=techreport)


