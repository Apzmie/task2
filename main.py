import json
import os

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, index):
        print(f"\n[문제 {index}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    def load_data(self):
        # 파일이 있으면 불러오고, 없으면 기본값 세팅 (나중에 구현)
        self.set_default_quizzes()

    def set_default_quizzes(self):
        self.quizzes = [
            Quiz("대한민국의 수도는?", ["인천", "광주", "서울", "부산"], 3),
            Quiz("파이썬 창시자는?", ["귀도", "제임스", "빌", "마크"], 1),
            Quiz("태양계에서 가장 큰 행성은?", ["지구", "화성", "목성", "토성"], 3),
            Quiz("CPU의 뜻은?", ["중앙처리장치", "기억장치", "입력장치", "출력장치"], 1),
            Quiz("1+1은?", ["1", "2", "3", "4"], 2)
        ]

    def run(self):
        while True:
            print("\n" + "="*20)
            print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 목록 보기\n4. 점수 확인\n5. 종료")
            print("="*20)
            choice = input("선택: ").strip()

            if choice == "1":
                print("퀴즈 풀기 기능을 곧 구현합니다!")
            elif choice == "5":
                print("게임을 종료합니다.")
                break
            else:
                print("번호를 다시 확인해주세요.")

if __name__ == "__main__":
    game = QuizGame()
    game.run()