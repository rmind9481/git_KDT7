# -------------------------------------------------------------
#   dict 자료형의 전용 함수 즉, 메서드
#   
# -------------------------------------------------------------


data ={'name':'홍길동', 'age':20, 'gender':'남', 'job':'의적'}


# [1] dict 에서 키만 추출 해주는 메서드 => keys()

keys=data.keys()
print(type(keys), keys)



# dict_keys 타입 => list 타입 형변환

keys = list(keys)
print(type(keys), keys)
print(type(keys), keys, keys[0], keys[-1])


# [2] dict에서 값만 추출 해주는 메서드 => values()
values=data.values()
print(type(values), values)


# dict_values 타입 => list 타입 형변환
values = list(values)
print(type(values), values, values[0], values[-1])


# [3] dict 에서 키와 값을 튜플로 묶어서 추출 해주는 메서드 => items()
items = data.items()
print(type(items), items)

# - dict_items 타입 => list 타입 형변환

items=list(items)
print(type(items), items, items[0], items[-1])



#[4] dict에서 키로 값 추출 해주는 메서드 => get(key , default_value)
print(data['name'],data.get('name'))

# 존재하지않는 키 => keyERROR
# print(data['phone'])

print(data.get('phone','존재하지 않습니다.'))
print(data.get('phone',0))
print(data.get('phone',-1))



#[5] 멤버 연산자 in/not in => 기준 key
# data ={'name':'홍길동', 'age':20, 'gender':'남', 'job':'의적'}
# => key 
print(f"'name' in data => {'name' in data}")
print(f"'job' in data => {'job' in data}")


# => value
print(f"'남' in data => {'남' in data}") # => key 값을 반환
print(f"'남' in data => {'남' in data.values()}") # => values 값을 체크

