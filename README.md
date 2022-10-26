# data_structure

# 추상자료형
---
복잡한 것을 가리고 필요한 것만 남겨놓는 것
SW = DATA + 명령코드
객체지향 SW = 객체의 집합



#시간 복잡
---
성능표기 -> BIG Oh 표기법
O(n) : 실행 시간 복잡도가 n에 비례

* log n
* n
* n log n
* n^2

## 빅오 표기법
---
example

* f(n) =5 -> O(1) , c= 10 이면 5< 10
* f(n) = 5 * 2^n -> O(2^n), c=10 일 때 5*2^n + 10 * n2 + 100 < 10 * 2^n 이기 때문에.

## 스택
---
탐색 -> 깊이 우선 탐색 (Depth - First Search(DFS))


## queue 원리
---
큐 -> FIFO 순서를 따름 : 들어가는 순서대로 나오는 것을 의미
뒤 (Rear)에서 들어와 앞 (Front)로 데이터가 나오게 됨

Front -> 삭제
Rear -> 삽입

선형 큐의 문제점 : 삭제를 하게 되면 모든 데이터를 이동해주어야한다. -> 원형 큐


큐 응용 : 대기열 시뮬레이션, 버퍼 , 너비 우선 탐색 (Breadth Fisrt Search / BFS)

## Deque (덱)
---
선입선출을 따르던 큐에서 양 옆으로 삽입, 삭제가
  get_num():
  return (rear - front + Size) % Size


## 연결리스트
---
노드 : 데이터와 링크로 구성
node1.data = data1
node1.link = node2 로 구성

노드 삽입 : 중간 연결리스트에 데이터 삽입
* 새 노드 생성 , 데이터 입력
* 새노드의 링크에 n+1 번째 노드 입력
* n-1 노드의  링크를 새 노드로 지정

노드 삭제 : 중간 데이터 삭제
* n-1 데이터 링크를 n+1 노드로 연결
* n번째 노드 삭제

코드 구현
* head : 첫번째 노드
* current : 현재 녿
* pre : 현재 처리중 바로 앞 노드

## 우선순위큐
---
우선순위를 가진 항목들을 저장하는 큐
우선순위가 높은 데이터가 먼저 나가게 됨

최대값 우선 큐 -> Max-heap
최소값 우선 큐 -> Min-heap

우선순위 큐 구현 비교


|표현 방법|삽입|삭제|
|:---:|:---:|:---:|
|순서 없는 배열|O(1)|O(n)|
|순서 없는 연결리스트|O(1)|O(1)|
|정렬된 배열|O(n)|O(1)|
|정렬된 연결 리스트|O(n)|O(1)|
|힙|O(log n)|O(log n)|

### heal (힙)
* 최대힙 - 부모 노드의 키값이 자식 노드키값보다 크거나 같은 완전 이진 트리
* 최소힙 - 부모 노드의 키값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리

( 완전 트리 -> 위에서 아래로 갈 때 좌에서 우로 자식을 설정)

* 힙 각 노드에 번호를 붙임 ( 노드가 없어도 좌에서 우로 가상으로 있다고 생각 한 후 번호 설정) -> 배열의 인덱스로 설정

(시험문제 : 다운힙에서 디큐했을대 )
