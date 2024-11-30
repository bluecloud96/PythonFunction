import numpy as np
import os
import datetime
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

#운동부위 두가지 선택
part1, part2 = input('오늘 운동하실 두가지 부위를 입력해주세요: ').split(',')
if part1 == part2:
    print('다시 입력해주세요: ')
    part1, part2 = input('오늘 운동하실 두가지 부위를 입력해주세요: ').split(',')
    
    
def body_part(part1,part2):
    lower_body = ['스티프데드리프트', '힙쓰러스트', '브이스쿼트', '레그프레스', '시티드레그프레스', '힙어브덕션', '레그컬', '링크아웃사이', '원레그힙데드리프트', '리버스하이퍼']
    big_three = ['바벨스쿼트', '루마니안데드리프트', '컨벤셔널데드리프트']
    back = ['바벨로우', '덤벨로우', '스탠딩풀업', '랫풀다운', '암풀다운', '티바로우', '케이블로우', '케이블하이로우', '어시스트풀업', '셀렉트로우']
    shoulder = ['셀렉트숄더프레스', '숄더프레스머신', 'iso숄더프레스', '사레레머신', '오버헤드프레스', '사이드레터널레이즈', '페이스풀', '풀오버', 'iso프론트풀다운', '밀리토리프레스', '사레레/프론트레이즈(세트)', '덤벨숄더프레스']
    chest = ['벤치프레스', '인클라인벤치프레스', '체스트프레스', '니푸쉬업', '플라이']
    abdomen_arm = ['케이블컬', '케이블푸쉬다운', '크런치']
    
    routine = []
    routine1 = []
    routine2 = []
    #루틴만들기

    if part1 == '하체':
        routine1 = list(np.random.choice(lower_body, 2, replace = False)) +list(np.random.choice(big_three, 1, replace = False))
        
    elif part1 == '등':
        routine1 = list(np.random.choice(back, 2, replace = False))

    elif part1 == '가슴':
        routine1 = list(np.random.choice(chest, 2, replace = False))
    
    elif part1 == '어깨':
        routine1 = list(np.random.choice(shoulder, 2, replace = False))

    if part2 == '하체':
        routine2 = list(np.random.choice(lower_body, 2, replace = False)) +list(np.random.choice(big_three, 1, replace = False))
        

    elif part2 == '등':
        routine2 = list(np.random.choice(back, 2, replace = False))

    elif part2 == '가슴':
        routine2 = list(np.random.choice(chest, 2, replace = False))
        
    elif part2 == '어깨':
        routine2 = list(np.random.choice(shoulder, 2, replace = False))
    
    
    routine = routine1 + routine2


    if len(routine) == 4:
        plus_exercise = list(np.random.choice(abdomen_arm, 1, replace = False))
        routine.append(plus_exercise[0])
        

    return routine


def exercise_memo(exercise):
    nowdate = datetime.datetime.now()
    
    if not os.path.isfile('./운동기록/운동기록('+nowdate.strftime("%Y-%m-%d")+').txt'):
        with open('./운동기록/운동기록('+nowdate.strftime("%Y-%m-%d")+').txt','w',encoding = 'utf-8') as file:
            file.write(f'{exercise}\n')
        
    else:    
        with open('./운동기록/운동기록('+nowdate.strftime("%Y-%m-%d")+').txt','a',encoding = 'utf-8') as file:
            file.write(f'{exercise}\n')

            
def count_memo(exercise, count, weight, set):
    nowdate = datetime.datetime.now()
    with open('./운동기록/운동기록('+nowdate.strftime("%Y-%m-%d")+').txt','a',encoding = 'utf-8') as file:
            file.write(f'{set}세트 {weight}kg {count}개\n')
            


def break_time(routine,breaktime,set):
    for exercise in routine:
        print(exercise)
        exercise_memo(exercise)
        for i in range(set):
            set = i + 1
            weight = input('웨이트 무게를 입력해주세요(kg): ')
            count = input('운동 횟수를 입력해주세요(개): ')
            time.sleep(breaktime)
            count_memo(exercise,count,weight,set)

body_part(part1, part2)
routine = body_part(part1,part2)
break_time(routine,1,2)#테스트로 운동세트 2회, 1초 breaktime
print('운동완료하셨습니다! 수고하셨습니다!😆😊😄😁')