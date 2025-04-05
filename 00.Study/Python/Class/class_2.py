# 도서관 시스템

# 책 등록
# 책 목록 보기
# 책 대출/ 반남

class Book :
    
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'{self.title} 대출 완료')

        else:
            print(f'{self.title} 은 이미 대출중입니다.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'{self.title} 반납완료')

        else:
            print(f'{self.title}은 대출되지않습니다.')

    
    def __str__(self):
        status = '대출중' if self.is_borrowed else '대출가능'
        return f'{self.title} = {status}'

def main():

    library_list = []

    while True:
        print('\n 1. 책등록  | 2. 전체 책 보기 | 3. 책 대출 | 4. 책반납 | 5. 종료')
        choice = input('메뉴 선택')
        
        if choice == '1':
            title = input('책 제목 입력')
            library_list.append(Book(title))
            print('책등록 완료')

        elif choice == '2':
            if not library_list:
                    print('등록된 책이 없습니다.')
            for i, book in enumerate(library_list):
                print(f'{i+1}.{book}')

        elif choice == '3':
            idx = int(input('대출할 책 번호 :'))-1

            if 0 <= idx < len(library_list):
                library_list[idx].borrow()
        elif choice == "4":
            idx = int(input("반납할 책 번호: ")) - 1
            if 0 <= idx < len(library_list):
                library_list[idx].return_book()
        elif choice == "5":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == '__main__':
    main()