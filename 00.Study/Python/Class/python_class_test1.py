
# 객체 지향 프로그래밍

'''클래스 (Class)
객체의 구성요소를 담는 개념
여러개 의 속성과 메소드 를 포함하는 개념
- 객체를 정희하는 틀 또는 설계도
- 인스턴스는 메모리에 할당된 객체를 의미

class Name(object):
   
    # class : 클래스 정의
    # Name : 클래스 이름
    # object : 상속 받는 객체명

'''

# class Book(object):
#     autorh =''
#     titel =''
#     publisher =''
#     data =''

# book = Book()
# book.autorh = 'Suan'
# # book 클래스 메소드 정의
# book.titel = 'Python Programming'
# print(book.autorh)
# print(book.titel)

# Book 클래스 메소드 정의
# 메소드 
'''
    책정보 출력 : pring_info(self)
    self 가 있어야만 실제로 인스턴스가 사용할수 있는 메소드로 선언
    print_info(self) 에서 self 는 실제로 b1 인스턴스를 의미
    메소드 안세서 속성값을 사용하지 않을 경우에는 self 생략가능
'''
class Book(object):
    autorh =''
    titel =''
    publisher =''
    data =''

    def print_info(self):
        print('Author :', self.autorh)
        print('Title :', self.titel)
        print('Publiser:',self.publisher)
        print('Date:',self.data)

book = Book()
book.print_info()

book.autorh = 'Suam'
book.titel = 'Python Programming'
book.publisher = 'Colab'
book.data = '2020'
book.print_info()

        

# 인스턴스 속성
# -인스턴스 속성은 객체로 부터 인스턴스가 생성된 후에 인스턴스에 활용하는 속성


# Class 속성 
# __init__() 메소드를 이용하여 클래스의 속성들을 초기화

# 클래스
class Person: 
    # 생성자
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def great(self):
        print(f"Hi~ Im {self.name} and I'm {self.age}years old ")

# 객체생성

p1 = Person('Alice',25)
p1.great()


# 클래스 변수

class Dog:
    species = 'Canine'

    def __init__(self, name):
        self.name = name

d1 = Dog('Rex')
d2 = Dog('Buddy')

print(d1.species)
print(d1.name)


# 클래스 매서드 & 정적 매서드
# 인스턴스 메서드
# 가장 흔히 쓰이는 것으로 인스턴스 변수에 엑세스 할수 있도록 첫번째 인자에 항상 객체 자신을
# 의미하는 self 파라미터를 갖는다.
# 해당 클래스 안에서 
# self.메서드
# 클래스 밖에서는 객체.메서드명

# 정적 메서드 static 메서드 
# 객체와 독립적이지만, 로직상 클래스 내에 포함되는 메서드
# self 파라미터를 가지고 있지않다. 따라서 인스턴스 변수에 엑세스가 불가능
# 그러나, 정적 메서드 내부에서 클래스 변수(속성) 에는 클래스명,클래스 속성명으로 엑세스 가능
# 정적 메서드는 메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수함수(pure function)
# 순수 함수란 부수효과 가 없고, 입력값이 같으면 언제나 같은 출력값을 반환
# 즉, 인스턴스 상태를 변화시키지않는 메서드
# @staticmethod라는 데코레이터를 붙여서 해당 메서드가 정적 메서드임을 표시한다.
# 호출 방법 ; 클래스명.정적메서드명 또는 객체명.정적메서드명 둘 다 호출 가능하지만, 전자를 주로 사용한다.

class MyClass:
    # 클래스 변수 (클래스 속성)
    count = 0

    @classmethod
    def increase_count(cls):
        cls.count += 1

    @staticmethod
    def say_hello():
        print("Hello!")

MyClass.increase_count()
MyClass.say_hello()

# 상속

class Animal:
    def speak(self):
        print('Animal speaks')


class Dog(Animal):
    def speak(self):
        print('Dog barks')

    
d = Dog()
d.speak()

# 다중 상속
class A:
    def hello(self):
        print("Hello from A")

class B:
    def hello(self):
        print("Hello from B")
    def hello2(self):
        print('hello_2_b')

class C(A, B):
    pass

c = C()
c.hello()

# 계산기


class Calculator :
    def __init__(self):
        self.result = 0

    def add(self,n):
        self.result += n
        return self.result
    
    def subtract(self,n):
        self.result -= n

        return self.result

calc = Calculator()
print(calc.add(10))
print(calc.subtract(3))


class Dog :
    # 클래스 변수 (모든 강아지가 공유함)
    species = 'Canis Familiris'

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f'{self.name}은 {self.age} 살이며, 좋은 {self.species}입니다')

dog1 = Dog('초코',3)
dog2 = Dog('바둑이',5)

dog1.info()
dog2.info()


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"안녕하세요, 저는 {self.name}입니다.")

if __name__ == "__main__":
    p = Person("루카스")
    p.say_hello()