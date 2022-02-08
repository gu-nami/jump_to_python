# 파이썬 자료형 - 문자형 자료형
# 문자열 : 문자, 단어 등으로 구성된 문자들의 집합

# 문자열 만들기
# 1. 큰따옴표로 양쪽 둘러싸기
"a"
"123"
# 2. 여러 줄인 문자열을 변수에 대입하고 싶을 때는 작은(큰) 따옴표 3개를 사용한다
multiline = '''
Life is too short
You need python
'''
print(multiline)

#문자열 연산하기
#1. 문자열 더하기 = 연결하기
head = "Python"
tail = "is fun!"
head + tail

#2. 문자열 곱하기 = 반복하기
a = "python"
a * 2

#4. 문자열 길이 구하기
a = "Life is too short"
len(a)

b = "You need python"
len(b)

# 문자열 인덱싱 = 문자열 안의 특정한 값 뽑아내기
a = "Life is too short, You need python"
a[0] #파이썬은 0부터 숫자를 셈!
a[1]
a[-1] #뒤에서 부터 첫번째 문자

# 문자열 슬라이싱 = 한 문자 뿐만 아니라 단어 뽑아내기
a = "Life is too short, You need python " #에서 Life 뽑아내기
a[0:4] # 슬라이싱 기법은 끝번호에 해당하는 것은 포함하지 않는다 !

a = "20010331Rainy"
year = a[:4]
year
month = a[4:6]
month
day = a[6:8]
day
weather = a[8:]
weather

#pithon을 python으로 바꿔보자
a = "pithon"
a[0] + "y" + a[2:] #a[1] = y는 오류 발생, 문자열의 요솟값은 바꿀 수 없기 때문

# 문자열 포매팅 : 문자열 안의 특정한 값을 바꾸어야 할 때
# %s를 사용하면 자동으로 %뒤에 있는 값을 어떤 형태의 값이든 문자열로 바꿔준다.
# 숫자 대입
"I eat %s apples" % 3
# 문자열 대입
"I eat %s apples" % "five"
# 변수 대입
number = 4
"I eat %s apples" % number
#두 개 이상의 값 넣기
number = 10
day = 'three'
"I ate %s apples. so I was sick for %s days." % (number, day)

#포맷 함수를 사용해서 포매팅하기
"I eat {0} apples" .format(3)
"I eat {0} apples" .format("five")

number = 6
"I eat {0} apples" .format(number)

number = 10 
day = "three"
"I ate {0} apples. so I was sick for {1} days." .format(number, day)

"I ate {number} apples. so I was sick for {day} days." . format(number = 10, day = "five")

"I ate {0} apples. so I was sick for {day} days" .format(10, day = "three")

# f 문자열 포매팅
age = 30
f'나는 내년이면 {age+1}살이 된다' # f 문자열 포매팅은 표현식을 지원한다.

# 문자열 관련 함수
# 문자열 개수 세기
a = "hobby"
a.count('b') #b의 개수를 세준다.

# 위치 알려주기
a = "Life is too short"
a. index('t') # t가 처음 나온 위치를 알려준다.

a. index('k') # 문자열에 k가 없으면 오류발생

# 문자열 바꾸기
a = "Life is too short"
a.replace("Life", "Your leg")

#문자열 나누기
a = "Life is too short"
a.split() #공백을 기준으로 문자열 나누기

b = "a:b:c:d"
b.split(':') # :기호를 기준으로 문자열 나누기
