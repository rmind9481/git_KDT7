# 영화 추가
# 예매 가능 좌석 확인
# 좌석 예매



class Movie :
    def __init__(self, title, seats=10):
        self.title = title
        self.seats = [False] * seats

    def reserve(self, seat_num):
        if 0 <= seat_num < len(self.seats):
            if not self.seats[seat_num]:
                self.seats[seat_num] = True
                print(f'{seat_num+1} 번 좌석입니다.')

            else:
                print('이미 예약된 자석입니다.')
        
        else:
            print('유효 하지않은 좌석 입니다.')

    
    def show_seats(self):
        for i, seat in enumerate(self.seats):
            print(f"{i+1}:{'O' if seat else 'X'}", end=" ")
        print('\n')


def main():
    movies = []

    while True:
        print("\n1. 영화 등록 | 2. 좌석 보기 | 3. 좌석 예매 | 4. 종료")
        choice = input("선택: ")

        if choice == "1":
            title = input("영화 제목: ")
            movies.append(Movie(title))
            print("영화 등록 완료!")

        elif choice == "2":
            for i, m in enumerate(movies):
                print(f"{i+1}. {m.title}")
                m.show_seats()

        elif choice == "3":
            for i, m in enumerate(movies):
                print(f"{i+1}. {m.title}")
            m_idx = int(input("영화 번호 선택: ")) - 1
            seat = int(input("예약할 좌석 번호: ")) - 1
            if 0 <= m_idx < len(movies):
                movies[m_idx].reserve(seat)

        elif choice == "4":
            break

if __name__ == "__main__":
    main()