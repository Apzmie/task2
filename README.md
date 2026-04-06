# task2
Python과 Git을 활용하여 데이터 영속성을 구현한 터미널 기반 퀴즈 게임 프로젝트입니다.

1. 프로젝트 개요

설명: 사용자가 퀴즈를 풀고, 직접 새로운 퀴즈를 등록하며 최고 점수를 관리할 수 있는 콘솔 프로그램입니다.

2. 퀴즈 주제 및 선정 이유

주제: 일반 상식 (General Knowledge)

선정 이유:

특정 분야에 치우치지 않아 누구나 쉽게 게임에 참여하고 흥미를 느낄 수 있습니다.

정답이 명확한 데이터(상식)를 사용함으로써 프로그램의 로직(입력/출력/검증)을 테스트하기에 가장 적합한 주제라고 판단했습니다.

3. 실행 방법

```Bash
# 저장소 복제
git clone https://github.com/Apzmie/task2.git

# 디렉토리 이동
cd task2

# 프로그램 실행
python main.py
```

4. 기능 목록

퀴즈 풀기: 저장된 문제를 풀고 점수를 계산하며, 최고 점수 달성 시 기록을 갱신합니다.

![play](./screenshots/play.png)

퀴즈 추가: 사용자가 직접 문제, 보기(4개), 정답 번호를 입력하여 새 퀴즈를 등록합니다.

![add_quiz](./screenshots/add_quiz.png)

퀴즈 목록: 현재 등록된 모든 퀴즈의 질문 리스트를 확인합니다.

![quiz_list](./screenshots/quiz_list.png)

점수 확인: 역대 최고 점수(최고 정답률)를 확인합니다.

![score](./screenshots/score.png)

데이터 자동 저장: 프로그램 종료나 중단 시 모든 데이터는 state.json에 안전하게 기록됩니다.

5. 파일 구조

main.py: 프로그램의 메인 로직이 담긴 파일 (Quiz, QuizGame 클래스 포함)

state.json: 퀴즈 데이터와 점수가 기록되는 JSON 데이터 파일

.gitignore: Git 관리에서 제외할 파일 설정

README.md: 프로젝트 설명 문서

6. 데이터 파일 설명 (state.json)

데이터는 UTF-8 인코딩으로 저장되며, 아래와 같은 JSON 스키마를 가집니다.

quizzes 	List (Array)

best_score	Integer	기록된 최고 점수


git_log
![git_log](./screenshots/git_log.png)




---
*이 문구는 Git 실습 중에 추가되었습니다.*
