# 딕셔너리 자료형 : key와 value를 한 쌍으로 갖는 자료형. key를 통해 value를 얻는다.
# 딕셔너리 만들기    
dic = {'name':'pey', 'phone':'01119993323','birth':'1118'} #key : name, phone, birth
                                                           #value : pey, 0119993323, 1118
a = {'a':'hi'} #value로 문자열 사용 가능
a = {'a':[1,2,3]} #value로 리스트 사용 가능

# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b' # {2:'b'}쌍 추가
a

a['name'] = 'pey' # {'name':'pey'}쌍 추가
a

#딕셔너리 요소 삭제하기
del a[1] #key가 1인 쌍이 삭제 되었다. 
a
del a['name'] #key가 name인 쌍이 삭제 되었다. 
a

#key를 사용해 value 얻기
grade = {'pey': 10, 'julliet':99}
grade['pey'] #'pey'에 해당하는 value인 10 반환
grade['julliet'] #'julliet'에 해당하는 value인 99 반환

a = {1:'a', 2:'b'}
a[1] # key가 1인 요소의 value를 반환

## 딕셔너리 주의 사항
# 1. key는 고유한 값이므로 중복되는 key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시됨
a = {1:'a', 1:'b'}
a # 1이라는 key 값이 중복으롷 사용되면 1:'a' 쌍이 무시된다. 

#2. key에는 변하지 않는 값만 사용 가능 (튜플 O, 딕셔너리 X)

# 딕셔너리 관련 함수
# key 리스트 만들기
a = {'name':'pey', 'phone':'01119993323','birth':'1118'}
a.keys() # 딕셔너리 a의 key만을 모아서 dict_keys개체를 반환
list(a.keys()) #dict_keys를 리스트로 변환

# value 리스트 만들기
a.values() # 딕셔너리 a의 value만을 모아서 dict_values 객체를 반환

# key, value 쌍 얻기
a.items() # key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 반환

# key : value 쌍 모두 지우기
a.clear()
a

#key로 value 얻기
a = {'name':'pey', 'phone':'01119993323','birth':'1118'}
a.get('name') #a['name']을 사용했을 때와 동일
a.get('phone')

# 해당 key가 딕셔너리 안에 있는지 조사하기
a = {'name':'pey', 'phone':'01119993323','birth':'1118'}
'name' in a
'email' in a

## 연습
a = {'name':'홍길동', 'birth':'1128', 'age':30}
a