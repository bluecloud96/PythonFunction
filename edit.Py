import os
import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 운동 부위와 운동 목록
exercises = {
    '하체': ['스티프데드리프트', '힙쓰러스트', '브이스쿼트', '레그프레스', '시티드레그프레스', '힙어브덕션', '레그컬', '링크아웃사이', '원레그힙데드리프트', '리버스하이퍼'],
    '등': ['바벨로우', '덤벨로우', '스탠딩풀업', '랫풀다운', '암풀다운', '티바로우', '케이블로우', '케이블하이로우', '어시스트풀업', '셀렉트로우',' 하이로우', '미들로우' ],
    '가슴': ['벤치프레스', '인클라인벤치프레스', '체스트프레스', '니푸쉬업', '플라이','인클라인머신','디클라인프레스'],
    '어깨': ['셀렉트숄더프레스', '숄더프레스머신', 'iso숄더프레스', '사레레머신', '오버헤드프레스', '사이드레터널레이즈', '페이스풀', '풀오버', 'iso프론트풀다운', '밀리토리프레스', '사레레/프론트레이즈(세트)', '덤벨숄더프레스'],
    '복부/팔': ['케이블컬', '케이블푸쉬다운', '크런치']
}

# 운동 기록 저장 함수
def exercise_memo(exercise_log):
    nowdate = datetime.datetime.now()
    directory = './운동기록/'
    filename = f'운동기록({nowdate.strftime("%Y-%m-%d")}).txt'

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(directory + filename, 'w', encoding='utf-8') as file:
        for log in exercise_log:
            file.write(f"{log}\n")

# 세트 기록 저장 함수
def count_memo(exercise, count, weight, set_num):
    return f'{exercise}: {set_num}세트, {weight}kg, {count}개'

# 운동 수행 함수
def perform_exercise():
    exercise_log = []  # 오늘 수행한 운동 기록
    print("운동 부위를 선택해주세요: 하체, 등, 가슴, 어깨, 복부/팔")
    print("원하는 부위를 선택한 후 운동을 고르세요. '끝'을 입력하면 종료됩니다.\n")

    while True:
        part = input('운동 부위 입력 (또는 "끝" 입력): ')
        if part == '끝':
            break

        if part not in exercises:
            print("잘못된 부위입니다. 다시 입력해주세요.")
            continue

        print(f"{part} 운동 목록: {', '.join(exercises[part])}")
        exercise = input(f"{part}에서 하고 싶은 운동을 입력하세요 (또는 '취소' 입력): ")
        if exercise == '취소':
            continue
        elif exercise not in exercises[part]:
            print("잘못된 운동입니다. 다시 입력해주세요.")
            continue

        print(f"운동 시작: {exercise}")
        exercise_log.append(f"운동: {exercise}")
        for i in range(5):  # 세트는 기본 3회
            set_num = i + 1
            weight = input(f"{set_num}세트 웨이트 무게를 입력해주세요(kg): ")
            count = input(f"{set_num}세트 운동 횟수를 입력해주세요(개): ")
            log = count_memo(exercise, count, weight, set_num)
            exercise_log.append(log)

    exercise_memo(exercise_log)
    return exercise_log

# 메인 실행
def main():
    print("운동 프로그램을 시작합니다.")
    exercise_log = perform_exercise()

    print("\n오늘의 운동 기록:")
    for log in exercise_log:
        print(log)

    print("\n운동이 완료되었습니다! 수고하셨습니다!")

if __name__ == "__main__":
    main()
