# task2
Python 클래스와 JSON을 활용해 데이터를 유지하고, Git으로 개발 과정을 기록

주제: 
```bash
상식 - 누구나 쉽게 접근할 수 있게 하기 위함.
```

실행 방법:
```bash
git clone https://github.com/Apzmie/task2.git
cd task2
python main.py
```

기능 목록:
```bash
퀴즈 풀기: 저장된 퀴즈를 풀고 점수를 확인합니다. (최고 점수 갱신 가능)
퀴즈 추가: 사용자가 새로운 문제를 직접 등록합니다.
퀴즈 목록: 현재 등록된 모든 퀴즈의 질문을 확인합니다.
점수 확인: 현재까지의 최고 점수를 확인합니다.
```

파일 구조:
```bash
main.py: 프로그램 실행 메인 코드 (Quiz, QuizGame 클래스 포함)
state.json: 데이터 저장 파일 (UTF-8 인코딩)
quizzes: 퀴즈 데이터 리스트 (질문, 보기, 정답 포함)
best_score: 퀴즈 게임의 최고 점수 기록
```
