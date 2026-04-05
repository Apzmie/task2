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
        self.file_path = "state.json"
        self.load_data()

    def load_data(self):
        """파일에서 데이터 불러오기 (없으면 기본값)"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.best_score = data.get("best_score", 0)
                    self.quizzes = [Quiz(q['question'], q['choices'], q['answer']) for q in data.get("quizzes", [])]
                print(f"📂 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")
            except:
                print("⚠️ 파일이 손상되어 초기화합니다.")
                self.set_default_quizzes()
        else:
            self.set_default_quizzes()

    def save_data(self):
        """현재 데이터를 state.json에 저장"""
        data = {
            "best_score": self.best_score,
            "quizzes": [q.__dict__ for q in self.quizzes]
        }
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def set_default_quizzes(self):
        self.quizzes = [
            Quiz("대한민국의 수도는?", ["인천", "광주", "서울", "부산"], 3),
            Quiz("파이썬 창시자는?", ["귀도", "제임스", "빌", "마크"], 1),
            Quiz("태양계에서 가장 큰 행성은?", ["지구", "화성", "목성", "토성"], 3),
            Quiz("CPU의 뜻은?", ["중앙처리장치", "기억장치", "입력장치", "출력장치"], 1),
            Quiz("1+1은?", ["1", "2", "3", "4"], 2)
        ]
        self.save_data()

    def play(self):
        print("\n📝 퀴즈를 시작합니다!")
        score = 0
        for i, q in enumerate(self.quizzes, 1):
            q.display(i)
            while True:
                ans = input("정답(1-4): ").strip()
                if ans.isdigit() and 1 <= int(ans) <= 4:
                    if int(ans) == q.answer:
                        print("✅ 정답!"); score += 1
                    else:
                        print(f"❌ 오답! 정답은 {q.answer}번")
                    break
                print("⚠️ 1-4 사이 숫자만 입력하세요.")
        
        print(f"\n🏆 점수: {score}/{len(self.quizzes)}")
        if score > self.best_score:
            self.best_score = score
            print("🎉 최고 점수 경신!")
            self.save_data()

    def add_quiz(self):
        print("\n📌 새 퀴즈 추가")
        q_text = input("문제 내용: ").strip()
        choices = [input(f"보기 {i}: ").strip() for i in range(1, 5)]
        while True:
            ans = input("정답 번호(1-4): ").strip()
            if ans.isdigit() and 1 <= int(ans) <= 4:
                self.quizzes.append(Quiz(q_text, choices, int(ans)))
                self.save_data()
                print("✅ 추가 완료!")
                break
            print("⚠️ 숫자를 확인하세요.")

    def show_list(self):
        print(f"\n📋 등록된 퀴즈 목록 ({len(self.quizzes)}개)")
        for i, q in enumerate(self.quizzes, 1):
            print(f"[{i}] {q.question}")

    def run(self):
        while True:
            print("\n1.풀기 2.추가 3.목록 4.최고점수 5.종료")
            menu = input("선택: ").strip()
            if menu == "1": self.play()
            elif menu == "2": self.add_quiz()
            elif menu == "3": self.show_list()
            elif menu == "4": print(f"\n🏆 최고 점수: {self.best_score}점")
            elif menu == "5": print("종료합니다."); break

if __name__ == "__main__":
    QuizGame().run()