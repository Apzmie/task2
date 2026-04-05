import json
import os

# 1. Quiz 클래스 정의 (개별 퀴즈 객체용)
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, index):
        """문제를 화면에 출력합니다."""
        print(f"\n----------------------------------------")
        print(f"[문제 {index}]")
        print(f"{self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        """정답 여부를 확인합니다."""
        return self.answer == user_answer

    def to_dict(self):
        """JSON 저장을 위해 딕셔너리로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

# 2. QuizGame 클래스 (게임 전체 관리)
class QuizGame:
    def __init__(self):
        self.file_path = "state.json"
        self.quizzes = [] # 여기에 Quiz 객체들이 담깁니다.
        self.best_score = 0
        self.is_running = True
        
        # 프로그램 시작 시 데이터 로드
        self.load_data()

    def load_data(self):
        """파일이 없거나 손상된 경우를 처리하며 데이터를 불러옵니다."""
        # 기본 퀴즈 데이터 (최소 5개 주제에 맞춰 준비 권장)
        default_quizzes = [
            {"question": "Python의 창시자는?", "choices": ["Guido", "Linus", "Bjarne", "James"], "answer": 1},
            {"question": "JSON의 약자는?", "choices": ["Java Standard Object", "JavaScript Object Notation", "Just Simple Object", "None"], "answer": 2},
            {"question": "리스트에서 마지막 요소를 제거하는 함수는?", "choices": ["remove()", "delete()", "pop()", "clear()"], "answer": 3},
            {"question": "Python에서 사용되는 논리값은?", "choices": ["True/False", "Yes/No", "High/Low", "On/Off"], "answer": 1},
            {"question": "데이터를 저장하는 JSON 인코딩 형식은?", "choices": ["UTF-8", "ASCII", "EUC-KR", "ISO-8859"], "answer": 1}
        ]

        if not os.path.exists(self.file_path):
            print("📂 데이터 파일이 없어 기본 데이터를 사용합니다.")
            self.quizzes = [Quiz(**q) for q in default_quizzes]
            self.best_score = 0
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                raw_quizzes = data.get("quizzes", default_quizzes)
                # 딕셔너리 리스트를 Quiz 객체 리스트로 변환
                self.quizzes = [Quiz(**q) for q in raw_quizzes]
                self.best_score = data.get("best_score", 0)
                print(f"✅ 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score})")
        except (json.JSONDecodeError, IOError, TypeError):
            print("⚠️ 데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self.quizzes = [Quiz(**q) for q in default_quizzes]
            self.best_score = 0

    def save_data(self):
        """현재 상태를 state.json에 저장합니다."""
        try:
            data = {
                # Quiz 객체들을 다시 딕셔너리 형태로 바꿔서 저장
                "quizzes": [q.to_dict() for q in self.quizzes],
                "best_score": self.best_score
            }
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("💾 데이터가 안전하게 저장되었습니다.")
        except Exception as e:
            print(f"❌ 저장 중 오류 발생: {e}")

    def get_valid_input(self, prompt, min_val, max_val):
        """숫자 입력 예외 처리를 전담하는 메서드입니다."""
        while True:
            try:
                user_input = input(prompt).strip()
                if not user_input:
                    print("⚠️ 입력이 비어 있습니다. 숫자를 입력해 주세요.")
                    continue
                
                choice = int(user_input)
                if min_val <= choice <= max_val:
                    return choice
                else:
                    print(f"⚠️ {min_val}~{max_val} 사이의 숫자를 입력하세요.")
            except ValueError:
                print("⚠️ 숫자가 아닙니다. 다시 입력해 주세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n\n⚠️ 중단 신호가 감지되었습니다. 저장 후 종료합니다.")
                self.save_data()
                exit(0)

    def run(self):
        while self.is_running:
            print("\n========================================")
            print("        🎯 나만의 퀴즈 게임 🎯")
            print("========================================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("========================================")
            
            choice = self.get_valid_input("선택: ", 1, 5)

            if choice == 1:
                print("\n📝 퀴즈 풀기를 시작합니다!")
                # TODO: play_game() 구현 예정
            elif choice == 2:
                print("\n📌 퀴즈 추가 기능을 실행합니다.")
                # TODO: add_quiz() 구현 예정
            elif choice == 3:
                print("\n📋 등록된 퀴즈 목록을 출력합니다.")
                # TODO: show_list() 구현 예정
            elif choice == 4:
                print(f"\n🏆 최고 점수: {self.best_score}점")
            elif choice == 5:
                self.save_data()
                print("👋 프로그램을 종료합니다.")
                self.is_running = False

if __name__ == "__main__":
    game = QuizGame()
    game.run()