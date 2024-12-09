---
title: Python Object Oriented Programming
date: 2024-07-08
categories: python-basic
tags: ["programming/python", "programming/basics", "programming/oop"]
---
이 포스트는 [이 사이트](https://www.boostcourse.org/ai100/lecture/739171?isDesc=false)의 동영상 강의를 바탕으로 작성되었습니다. 더 자세한 내용은 해당 강의를 참고하시기 바랍니다.

## 클래스와 객체

- 객체 지향 언어의 이해

### 예시로 생각해보기

> 수강신청 프로그램을 작성한다. 어떻게 해야할까?
>
> 1. 절차적 프로그래밍
>
> - 수강신청이 시작부터 끝까지 순서대로 작성
>
> 2. 객체 지향 프로그래밍
>
> - 수강신청 관련 **주체**(교수, 학생, 관리자)의 **행동**(수강신청, 과목 입력)과 **데이터**(수강과목, 강의 과목)들을 중심으로 프로그램 작성 후 연결

### 객체지향 프로그래밍 개요

- Object-Oriented Programming, OOP
- 객체 : 실생활에서 일종의 물건 속성(Attribute)와 행동(Action)을 가짐
- OOP는 이러한 객체 개념을 프로그램으로 표현
- 속성은 변수(variable), 행동은 함수(method)로 표현
- class : 설계도
- instance : 실제 구현체

### 축구 선수 정보를 Class로 구현하기

1. Attribute(속성) 추가는 **init**, self와 함께!

- **init**은 객체 초기화 예약 함수

```python
class SoccerPlayer(object):

  def __init__(self, name, position, back_number):
      self.name = name
      self.position = position
      self.back_number = back_number
```

> 파이썬에서 \_\_의 의미
>
> - **는 특수한 예약 함수나 변수 그리고 함수명 변경(맨글링)으로 사용
>   ex) **main**, **add**, **str**, **eq\_\_
>   class SoccerPlayer(object):

```python
def __str__(self):
    return "Hello, My name is %s. I play in %s in center" % (self.name, self.position)
jinhyun = Soccerplayer("Jinhyun", "MF", 10)
print(jinhyun)
```

2. method 구현하기

- method(Action) 추가느 ㄴ기존 함수와 같으나, 반드시 self를 추가해야만 class 함수로 인정됨

```python
class SoccerPlayer(object):
    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다: From %d to %d"% (self.back_number, new_number))
        self.back_number = new_number
```

3. Object(instance) 사용하기

- Object 이름 선언과 함께 초기값 입력 하기

```python
jinhyun = SoccerPlayer("Junhyun", "MF", 10)
```

> self : **생성된 인스턴스 자신**을 의미함

## OOP Implementation Example

> 1. Note를 정리하는 프로그램
> 2. 사용자는 Note에 뭔가를 적을 수 있다.
> 3. Note에는 Content가 있고, 내용을 제거할 수 있다.
> 4. 두 개의 노트북을 합쳐 하나로 만들 수 있다.
> 5. Note는 Notebook에 삽입된다.
> 6. Notebook은 Note가 삽입 될 때 페이지를 생성하며, 최고 300 페이지까지 저장 가능하다.
> 7. 300 페이지가 넘으면 더 이상 노트를 삽입하지 못한다.

1. Notebook
   1. method
      1. add_note
      2. remove_note
      3. get_number_of_pages
   2. variable
      1. title
      2. page_number
      3. notes
2. Note
   1. method
      1. write_content
      2. remove_all
   2. variable
      1. content

## 객체 지향 언어의 특징

- 실제 세상을 모델링
- 필요한 것들
  - Inheritance(상속)
  - Polymorphism(다형성)
  - Visibility(히든 클래스)

### Inheritance(상속)

- 부모클래스로부터 속성과 method를 물려받는 자식 클래스를 생성 하는 것

```python
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

class Korean(Person):
   pass
first_korean = Korean("Sungchul", 35)
print(first_korean.name)
# "Sungchul"
```

```python
class Person: # 초기 상속은 (object)를 적어주지 않아도 됨
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print("저의 이름은", self.name,"이구요.제 나이는", str(self.age),"살 입니다.")

    def __str__(self):
        return "저의 이름은", self.name,"이구요.제 나이는", str(self.age),"살 입니다."
class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

    def do_work(self):
        print("열심히 일을 합니다.")

    def about_me(self):
        super().about_me()
        print("제 급여는", self.salary,"원 이구요, 제 입사일은", self.hire_date, "입니다.")

my_person = Person("John", 34, "Male")
my_employee = Employee("Chunsic", 45, "Male", 1000, "1989/12/19")

my_employee.about_me()
# 저의 이름은 Chunsic 이구요.제 나이는 45 살 입니다. 제 급여는 1000 원 이구요, 제 입사일은 1989/12/19 입니다.

```

### Polymorphism(다형성)

- 같은 이름 메소드의 내부 로직을 다르게 작성
- Dynamic Typing 특성으로 인해 파이썬에서는 같은 부모클래스의 상속에서 주로 발생함
- 개념적으로는 같은 일 세부적인 구현이 다를 때

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def __str__(self):
        return f"{self.name}: {self.talk()}"
class Cat(Animal):
    def talk(self):
        return "Meow!"
class Dog(Animal):
    def talk(self):
        return "Woaf! Woaf!"

animals = [Cat("John"), Cat("Chunsic"), Dog("Lassie")]

for animal in animals:
    print(animal)

# John: Meow!
# Chunsic: Meow!
# Lassie: Woaf! Woaf!
```

### Visibility(가시성)

- 객체의 정보를 볼 수 있는 레벨을 조절하는 것
- 누구나 객체 안에 모든 변수를 볼 필요가 없음
  1. 객체를 사용하는 사용자가 임의로 정보 수정
  2. 필요 없는 정보에는 접근할 필요가 없음
  3. 만약 제품으로 판매한다면? 소스의 보호

#### Encapsulation

- 캡슐화 또는 정보 은닉(Information Hiding)
- Class를 설계할 때, 클래스 간 간섭/정보공유의 최소화
  - 심판 클래스가 축구선수 클래스 가족 정보를 알아야 하나?
- 캡슐을 던지듯, 인터페이스만 알아서 써야함

- 가시성을 통해 객체 내부의 변수와 메서드를 외부에서 볼 수 있는 범위를 제한합니다.
  - public: 모든 곳에서 접근 가능
  - protected: 같은 패키지나 서브클래스에서만 접근 가능
  - private: 같은 클래스에서만 접근 가능
- 캡슐화를 통해 객체의 상태를 보호하고, 객체의 동작을 제어합니다.
  - 내부적으로 사용되는 변수는 private으로 설정하고, 필요한 경우 getter와 setter 메서드를 통해 접근을 허용합니다.

#### Visibility Example 1

- Product 객체를 Inventory 객체에 추가
- Inventory에는 오직 Product 객체만 들어감
- Inventory에 Product가 몇 개인지 확인이 필요
- Inventory에 Product items는 직접 접근이 불가

```python
class Product(object):
   pass
class Inventory(object):
   def __init__(self):
      self.__items = [] # Private(__) 변수로 선언, 타객체가 접근 못함
      self.test = "abc"

   def add_new_item(self, product):
      if type(product) == Product:
         self.__items.append(product)
      else:
         raise ValueError("Invalid Item")

   def get_number_of_items(self):
      return len(self.__items)
my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
my_inventory.__items # 접근 불가

# 접근 허용 방법(property decorator)
   @property
   def items(self):
      return self.__items
```

## decorator

- first-class objects(일급 객체)
- inner function
- decorator

1. First-class objects

- 일등 함수, 일급 객체
- 변수나 데이터 구조에 할당이 가능한 객체
- **parameter**로 전달이 가능 + **리턴 값**으로 사용
  - 파이썬의 함수는 일급함수

```python
def square(x):
   return x*x
f = square
f(5)
# 25
def cube(x):
   return x*x*x
def formula(method, argument_list):
   return [method(value) for value in argument_list]
```

2. Inner function

- 함수 내에 또 다른 함수가 존재

```python
def print_msg(msg):
   def printer():
      print(msg)
   printer()

print_msg("Hello, Python")
```

- closures : Inner function을 return값으로 반환

```python
def print_msg(msg):
   def printer():
      print(msg)
   return printer()

another = print_msg("Hello, Python")
another()
```

```python
def tag_func(tag, text):
   text = text
   tag = tag

   def inner_func():
      return '<{0}>{1}</{0}>'.format(tag, text)

   return inner_func

h1_func = tag_func('title', "This is Python Class")
p_func = tag_func('p', "Data Academy")

print(h1_func())
print(p_func())
# <title>This is Python Class</title>
# <p>Data Academy</p>
```

3. Decorator function

- 복잡한 클로져 함수를 간단하게 표현

```python
def star(func):
   def inner(*args, **kwargs):
      print(arg[1],"*"*30)
      func(*args, **kwargs)
      print(arg[1],"*"*30)
   return inner

@star
def printer(msg):
   print(msg)
printer("Hello","Python")
```

```python
def generate_power(exponent):
   def wapper(f):
      def inner(*args):
         result = f(*args)
         return exponent ** result
      return inner
   return wrapper

@generate_power(2)
def raise_two(n):
   return n**2

print(raise_two(3))
# 512
```
