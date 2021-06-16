---
title: "ToDo-HadoopEcosystem_1"
date: 2021-04-12 갱신
categories: Hadoop
---

## ToDo-HadoopEcosystem_1 

Overview of Hadoop Ecosystem<br>
*Udemy의 [The Ultimate Hands-On Hadoop: Tame your Big Data!](https://www.udemy.com/course/the-ultimate-hands-on-hadoop-tame-your-big-data/) 강좌 참고 내용*


{% include adsense.html %}


### HDFS(Hadoop Distributed File System)

Big Files -> Break Them into Blocks -> Stored across serveral Commodity Computers<br>
대용량 파일을 -> 블록으로 쪼개어 -> 각 블록은 복수 PC에 분산 저장

#### HDFS Architecture

- **Name Node**: "Edit Log"를 유지하여, 각 블록들의 생성,수정 등을 추적 및 파악<br>
- **Data Node**: 실제 블록들이 저장되는 노드<br>
             Client PC(Node)와 대화<br>
             다른 Data Node와 서로 대화하여 블록 복사본을 유지 
             
- **Name Node의 복원력**
>> 1. Backup Metadata: Name Nodes는 로컬 디스크와 NFS에 작성<br>
>> 2. Secondary NameNode: "Edit Log"의 복사본을 유지<br>
>> 3. HDFS Federation: 각 Name Node는 특정 Name Node의 볼륨만을 관리<br>
      * 대용랑 파일에 유용하지만 신뢰성을 의미하는 것은 아님<br>
>> 4. High Availability <br>
>>> 4.1 공유된 "Edit Log"을 이용하여 Hot Standby상태를 유지<br>
>>> 4.2 ZooKeeper 를 통해 활성화된 Name Node를 추적<br>
>>> 4.3 한 번에 한 개의 Name Node 만 사용 가능<br>
             
- **동작**<br>

**1. Reading a File**<br>
>1.1 Client Node -> Name Node<br>
>: xxx file이 필요해<br>

>1.2 Name Node ->  Client Node<br>
>: okay, Data Node 1,3으로 가면 돼<br>

>1.3 Nane Node -> Data Node 1,3<br>
>: retrieve blocks<br>

**2. Writing a File**<br>
>2.1 Client Node -> Name Node<br>
>: 새로운 파일 생성 요청<br>

>2.2 Name Node ->  Client Node<br>
>: okay, will create new entry<br>

>2.3 Client Node -> Data Node1<br>
>: 새로운 데이터, 파일 제공

>2.4 Data Node 1 -> 2 -> 3<br>
>: 서로 대화하여, 복제 및 저장<br>

>2.5 DataNode1 -> Client Node<br>
>: okay, Everything is fine<br>

>2.6 Client Node -> Name Node<br>
>: 새 데이터가 복제 저장 완료 통지



