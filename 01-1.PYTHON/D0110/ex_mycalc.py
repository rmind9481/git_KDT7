# ---------------------------------------------------------
#   나의 계산기 프로그램
# ---------------------------------------------------------

# 개발 범위 : 4칙 연산 수행

# UI 형식 : 명령어 기반 CUI/TUI
# UI 메뉴 : 연산 데이터 입력, 덧셈, 뺄셈, 곱셈, 나눗셈, 결과, 설정, 종료
# 기능 구현 : 각 메뉴 선택에 따라서 연산 수행
# -----------------------------------------------------------

# 5번 수행 가능한 계산기

while True:
    # 메뉴 출력
    print("*"* 30)
    print("1. 숫자 입력")
    print("2. 덧  셈")
    print("3. 뺄  셈")
    print("4. 곱  셈")
    print("5. 나눗셈")
    print("0. 종  료")
    print("*"* 30)

# 메뉴 선택
    choice= input("메뉴 선택:")

    if choice == '0' :
        print(f"프로그램을 종료합니다.")
        break;
    
    if choice == '1':
        nums = input("숫자 2개 입력(예:3,5)").strip().split(",")
        nums[0] = int(nums[0])
        nums[1] = int(nums[1])

        # nums= [int(num) for num in nums]

    elif choice == '2' :
        print(f"{nums[0]}+{nums[1]} = {nums[0]+nums[1]}")
    elif choice == '3' :
        print(f"{nums[0]}-{nums[1]} = {nums[0]-nums[1]}")
    elif choice == '4' :
        print(f"{nums[0]}*{nums[1]} = {nums[0]*nums[1]}")
    elif choice == '5' :
        if nums[1]:
            print(f"{nums[0]}/{nums[1]} = {nums[0]/nums[1]}")
    else:
        print("존재하지 않는 메뉴 입니다.")
