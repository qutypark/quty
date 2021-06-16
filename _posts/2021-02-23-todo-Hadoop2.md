---
title: "ToDo-HadoopEcosystem_2"
date: 2021-02-23
categories: Hadoop
---

## ToDo-HadoopEcosystem_2 

Overview of Hadoop Ecosystem<br>
*Udemy의 [The Ultimate Hands-On Hadoop: Tame your Big Data!](https://www.udemy.com/course/the-ultimate-hands-on-hadoop-tame-your-big-data/) 강좌 참고 내용*


{% include adsense.html %}


### Major Component of Hadoop<br>
*주의: 각 시스템 별로 복잡한 관계가 존재하고, 획일화된 이해방식이 존재하지 않음*<br>

이하의 내용 중 이번 포스팅에서는 <br>
Core Hadoop Ecosystem 에 대해 집중적으로 다뤄보도록 하겠습니다.<br>
>> **Ⅰ　Core Hadoop Ecosystem** <br>
>> Ⅱ　External Data Storage<br>
>> Ⅲ Query Engines<br>


#### Ⅰ Core Hadoop Ecosystem<br>
- 하둡에서 생성된 시스템과,(표시: *Hadoop Itself*)<br>
- 특정 문제를 해결하기 위해 Add-on된 시스템으로 나뉨(표시: *Add-on*)

#### 1. Hadoop Itself

##### 1.1 HDFS (Hadoop Distributed File System) <br>
Data Storage part of Hadoop <br>

주요기능: 빅데이터의 용량을 컴퓨터의 클러스터 간 분배시켜, <br>
클러스터의 모든 하드 드라이브를 하나의 거대 파일 시스템처럼 보이게 함<br>
그리고 데이터의 복사본을 보유하여 컴퓨터가 손실되었을 때 백업복사로부터 회복가능<br>
이가 자동으로 이루어진다는 것이 핵심 기능<br>


##### 1.2 YARN (Yet Another Resource Negotiator) <br>
Data Process part of Hadoop <br>
(on top of HDFS) <br>

주요기능: 컴퓨터 클러스터의 리소스를 관리하는 resource negotiator <br>
어떤 노드가 가능하고 불가능한지에 따라 어떤 태스크를 실행시킬 지 결정하는 기능<br>
클러스터가 기능하게 하는 **heartbeat** 같은 존재<br>


##### 1.3 MapReduce <br>
programming metaphor or programming model that allows you to process your data across entire cluster
(on top of YARN) <br>

주요기능: 전체 클러스터 간 데이터를 효과적으로 처리하게 하는 프로그래밍 모델<br>
>> - Mappers: 전체 클러스터 간 데이터를 병렬로 변형시킴<br>
>> - Reducers: 데이터를 집합시킴<br>

#### 2. Add-on 

##### 2.1 Pig <br>
programming api allows you write simple scripts look like SQL quries <br>
(on top of MapReduce) <br>

주요기능: Python 혹은 Java 코드 작성 없이도 쿼리 수행 및 MapReduce 수행이 가능해짐<br>
이는 YARN과 HDFS를 통해 필요한 데이터를 얻고 처리할 수 있음<br>

##### 2.2 HIVE <br>
data warehouse software project
(on top of MapReduce or TEZ) <br>

주요기능: SQL데이터베이스와 비슷하며 그 기능을 목적으로 함<br>
실제로 hadoop cluster 저장 데이터에 대해 SQL쿼리를 실행<br>
(실제 관계형 데이터베이스는 아님)

##### 2.3 Ambari <br>
system administrator <br> 
(on top of everything) <br>

주요기능: 이용 중인 하둡 시스템을 관리하는 역할<br>
각 클러스터 및 리소스 상황 감시 가능 및 어떤 클러스터 및 시스템이 실행 중인지 가시화 가능<br>
실제 hive 및 pig 쿼리 실행이 가능하며 hiveDB에 데이터 import 가능<br>

##### 2.4 Mesos <br>
open-source project to manage computer clusters<br>
(on top of HDFS) <br>
YARN과 같은 resource negotiator역할을 수행하며 그 대안이 될 수도 있음<br>

##### 2.5 Spark <br>
open-source unified analytics engine for large-scale data processing<br>
(on top of YARN and Mesos) = same level of MapReduce <br>

주요기능: MapReduce처럼 클러스터 간 데이터 처리를 담당함<br>
SQL뿐만 아니라 머신러닝 및 실시간 스트리밍 데이터 처리도 가능<br>

##### 2.6 TEZ <br>
Data Processing pipline<br>
(on top of YARN and Mesos) = same level of MapReduce <br>

주요기능: Spark와 같은 기능을 하고<br>
유향 비순회 그래프(DAG;Directed Acyclic Graph)처리로 유명<br>
Hive의 쿼리 수행시 더 최적화된 플랜으로 MapReduce보다 더 빠를 수 있음<br>

##### 2.7 HBase <br>
open-source non-relational distributed database<br>
= NoSQL database<br>
(sit off to the side)<br>

주요기능: 많은 처리량을 상대로 하는 빠른 속도의 데이터베이스 <br>
클러스터에 저장되어 있고 spark 혹은 MapReduce로 처리된 데이터를 <br>
상당히 빠른 속도로 다른 시스템들에게 노출시킴<br>

##### 2.8 Apache Storm <br>
distributed stream processing computation framework<br>
(sit off to the side)<br>
= Spark streaming (but in a different way)

주요기능: 실시간 스트리밍 데이터를 빠르게 처리하는 프레임워크 <br>
배치 파일을 가질 필요가 없으며 <br>
machinge learning모델이나 데이터가 업데이트 될 때마다 DB로의 처리 가능<br>

##### 2.9 Oozie <br>
Scheduling josbs on cluster<br>
(sit off to the side)<br>

주요기능: 다른 시스템 별 다른 단계와 다른 태스크 등의 복잡한 Operation을 스케줄링함 <br>
예를 들어 hive로 데이터를 로딩하고, 그 데이터를 pig로 결합하고, <br>
Spark로 쿼리를 수행하여, 최종적으로 결과를 HBase로 변경하는 Operation에 대해 <br>
Oozie를 통해 신뢰성있게 스케줄 관리가 가능<br>

##### 2.10 Zookeeper <br>
Coordinating everything on cluster<br>
(sit off to the side)<br>

주요기능: 클러스터 안의 많은 어플에 대한 코디네이팅을 수행 <br>
어떤 노드가 업 혹은 다운되어있는지와 더불어, <br> 
다른 앱들이 사용하는 클러스터의 공유된 상황에 대해 추적<br>
위에서 언급된 어플 및 시스템들은 클러스터간 신뢰적이고 일정한 성능을 유지하기 위해, <br>
Zookeeper에 의존함 (각 노드가 무작위로 다운될지라도)<br>

##### 2.11 Data Ingestion <br>
(sit off to the side)<br>
외부 리소스로부터 클러스터와 HDFS로의 데이터를 수집  

###### 2.11.1 Sqoop <br>
Hadoop과 외부DB간 커넥터 역할을 수행 <br>

###### 2.11.2 Flume <br>
웹 서버로부터 클러스터로의 웹 로그의 수집과 변형을 실시간으로 수행하는 역할<br>
많은 양의 웹 로그들이 신뢰적으로 수신됨<br>
수집 및 변형된 웹 로그들은 storm 혹은 spark streaming에 의해 실시간으로 처리됨<br>

###### 2.11.2 Kafka <br>
Flume과 비슷한 역할을 수행하지만 보다 일반적인 목적으로 사용됨


이하에 대해서는 다음 포스팅으로 넘어가도록 하겠습니다. <br>
>> Ⅱ　External Data Storage<br>
>> Ⅲ Query Engines<br>
