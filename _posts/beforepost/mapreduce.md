---
title: "ToDo-Hadoop; Map-Reduce"
date: 2021-04-12
categories: Hadoop
---

## ToDo-Hadoop; Map-Reduce 맵리듀스

#### 전반적인 내용은 아래의 강좌를 참고
Overview of Hadoop Ecosystem<br>
*Udemy의 [The Ultimate Hands-On Hadoop: Tame your Big Data!](https://www.udemy.com/course/the-ultimate-hands-on-hadoop-tame-your-big-data/) 

### Map-Reduce 맵리듀스 개요 <br>

> 맵리듀스란 무엇인가 <br>
>> HDFS에서 작동하는 데이터 분산 프레임워크

> HDFS란 무엇인가 <br> *[관련내용]()


> 왜 맵리듀스인가 <br>
*전제: 모든 일을 한번에 처리하는 것보다 각 라인에서 전문적으로 일을 처리하는 것이 생산적
>> 1. 클러스터 별로 대규모의 데이터 처리작업을 분산시킬 수 있다.
>> 2. 데이터를 각 파티션으로 구분하여 매핑(Transform), 리듀싱(Aggregate)시킬 수 있다.
>> 3. 실패에 대한 복원력이 강하다 (어플리케이션 매스터가 각 파티션의 매퍼와 리듀서를 모니터하기 때문)

### Map-Reduce 의 처리내용 <br>

#### Mapper 매퍼 <br>

- 주 역할: HDFS의 Raw source를 Key/Value 페어로 변환<br>
- 이점  : input data를 각각의 파티션으로 나누어 각 노드에 지정<br>
        -> 각 노드는 다른 노드에 대해 알 필요가 없으므로 병렬적 작업에 용이해짐

#### 






