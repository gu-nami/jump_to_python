
# 제어문
## 02. while문
* ##### 반복해서 문장을 수행해야 할 경우 while문 사용

>* ##### while문의 기본 구조
>
> ---
>##### while 조건문:
>
>##### &nbsp;&nbsp;&nbsp;&nbsp; 수행할 문장1
>##### &nbsp;&nbsp;&nbsp;&nbsp; 수행할 문장2
>##### &nbsp;&nbsp;&nbsp;&nbsp; 수행할 문장3
>##### &nbsp;&nbsp;&nbsp;&nbsp;   ...
> ---
> ##### 조건문이 참인 동안에 while문 아래의 문장이 반복해서 수행된다.
>  ##### ex) '열 번 찍어 안 넘어가는 나무 없다'는 속담을 파이썬으로 나타내기
>```python
> >>> treeHit = 0 # 나무를 찍은 횟수
> >>> while treeHit < 10: #나무를 찍은 횟수가 10보다 작은 동안 아래의 문장이 반복해서 수행됨
> ...    treeHit = treeHit + 1 # 나무를 찍은 횟수가 1씩 증가
> ...    print("나무를 %d번 찍었습니다." % treeHit)
> ...    if treeHit == 10: # 나무를 찍은 횟수가 10이 되면 아래의 문장 수행
>...        print("나무 넘어갑니다.")
>나무를 1번 찍었습니다.
>나무를 2번 찍었습니다.
>나무를 3번 찍었습니다.
>나무를 4번 찍었습니다.
>나무를 5번 찍었습니다.
>나무를 6번 찍었습니다.
>나무를 7번 찍었습니다.
>나무를 8번 찍었습니다.
>나무를 9번 찍었습니다.
>나무를 10번 찍었습니다.
>나무 넘어갑니다.
>```
>ex)
>&nbsp;
>```python
>prompt = """
>1. Add
>2. Del
>3. List
>4. Quit
>
>Enter number : """
>
>number = 0
>while number != 4:
>    print(prompt)
>    number = int(input())
> ```

>+ ##### while문 강제로 빠져 나가기
>
>##### `break`문을 이용하여 while문을 강제로 멈추게 할 수 있다. 
>
>##### ex) 커피 자판기
>```python
>coffee = 10
>while True:
>    money = int(input("돈을 넣어 주세요: "))
>    if money == 300:
>         print("커피를 줍니다.")
>         coffee = coffee - 1
>    elif money > 300:
>         print("거스름돈 %d를 주고 커피를 줍니다."%(money-300))
>         coffee = coffee -1
>    else:
>         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
>         print("남은 커피의 양은 %d개입니다." % coffee)
>     if coffee == 0:
>         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
>         break
>
>돈을 넣어 주세요 : 500
>거스름돈 200를 주고 커피를 줍니다.
>
>돈을 넣어 주세요 : 300
>커피를 줍니다.
>
>돈을넣어주세요 : 100
>돈을 다시 돌려주고 커피를 주지 않습니다. 
>남은 커피의 양은 8개입니다.
>돈을 넣어주세요
>```

>+ ##### while문의 맨 처음으로 돌아가기
>
>##### while문을 빠져나가지 않고 while문의 맨 처음 조건문으로 다시 돌아가게 만들고 싶은 경우 -> `continue` 사용
> ##### ex) 1부터 10까찌의 숫자 중 홀수만 출력하기
> ```python
> >>> a = 0
> >>> while a < 10:
>     a = a + 1
>     if a % 2 == 0: continue #a를 2로 나누었을 때 나머지가 0이면 맨처음 조건문으로 돌아감.
>     print(a)
>```
>###### a가 짝수이면 print(a)는 시행되지 않음
> ##### ex) 1부터 10까찌의 숫자 중 홀수만 출력하기
> ```python
> >>> a = 0
> >>> while a < 10:
>     a = a + 1
>     if a % 2 == 0: continue #a를 2로 나누었을 때 나머지가 0이면 맨처음 조건문으로 돌아감.
>     print(a)
>```
>&nbsp;
>##### ex) 1부터 10까지의 숫자 중에서 3의 배수를 뺀 나머지 값을 출력해보기.
> ```python
>a = 0
> while a < 10:
>    a = a + 1
>    if a % 3 == 0: continue
>    print(a)
> ```

> * 무한 루프
> ##### while문의 조건문이 True이므로 항상 참이됨. 따라서 while문 안에 있는 문장들은 무한하게 수행됨
>##### ex)
>```python
> >>> while True:
> ...    print("Ctrl+c를 눌러야 while문을 빠져나갈 수 있습니다.")
> ...
> Ctrl+c를 눌러야 while문을 빠져나갈 수 있습니다.
> Ctrl+c를 눌러야 while문을 빠져나갈 수 있습니다.
> Ctrl+c를 눌러야 while문을 빠져나갈 수 있습니다.
> .
> .
> .
>```
