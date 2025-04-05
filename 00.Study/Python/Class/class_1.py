# 학생 관리 시스템

# 기능 
# 학생 등록, 선생님 등록, 학생/선생님 정보 출력
# 등록 인원수 확인

class Person:
    # 전체 인원수 카운드
    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count += 1

    def __str__(self):
        return f'{self.name} ({self.age} 세)'
    
    @classmethod
    def get_count(cls):
        return cls.count

class Student(Person):
    def __init__(self, name, age, student_ID):
        super().__init__(name, age)
        self.student_id = student_ID

    def __str__(self):
        return f'학생 - {super().__str__()}, 학번: {self.student_id}'
    

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def __str__(self):
        return f'선생님 - {super().__str__()}, 과목 : {self.subject}'
    

def main():
    student_list = []
    teacher_list = []

    while True:
        print('\n[메뉴]')
        print('1. 학생 등록')
        print('2. 선생님 등록')
        print('3. 전체 인원 출력')
        print('4. 종료')
        
        choice = input('메뉴를 선택해주세요')

        if choice == '1':
            name = input('학생 이름:')
            age = input('나이:')
            sid = input('학번:')
            student_list.append(Student(name,age,sid))
            print('학생 등록완료')
        
        elif choice == '2':
            name = input('선생님 이름:')
            age = input('나이')
            subject = input('과목')
            teacher_list.append(Teacher(name,age,subject))

        elif choice == '3':
            print('\n[학생목록]')

            for s in student_list:
                print(s)
            
            print('\n 선생님 목록')
            for t in teacher_list:
                print(t)

            print(f'\n총 인원수 : {Person.get_count()}명')


        elif choice == '4':
            print('프로그램을 종료합니다.')

            break
        else:
            print('잘못된 입력입니다.')


# 프로그램 실행
if __name__ == '__main__':
    main()        