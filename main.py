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
        # [미션] 본인이 선택한 주제의 퀴즈 5개 직접 작성
        default_quizzes = [
            {
                "question": "세계에서 가장 큰 섬은 어디일까요?",
                "choices": ["마다가스카르", "그린란드", "보르네오", "뉴기니"],
                "answer": 2
            },
            {
                "question": "대한민국의 국보 1호는 무엇일까요?",
                "choices": ["다보탑", "석굴암", "숭례문", "경복궁"],
                "answer": 3
            },
            {
                "question": "영화 '기생충'의 감독은 누구일까요?",
                "choices": ["박찬욱", "봉준호", "이창동", "홍상수"],
                "answer": 2
            },
            {
                "question": "태양계에서 가장 큰 행성은 무엇일까요?",
                "choices": ["지구", "화성", "목성", "토성"],
                "answer": 3
            },
            {
                "question": "컴퓨터의 뇌 역할을 하는 부품은?",
                "choices": ["RAM", "SSD", "GPU", "CPU"],
                "answer": 4
            }
        ]

        if not os.path.exists(self.file_path):
            print("📂 데이터 파일이 없어 기본 데이터를 사용합니다.")
            # [미션] Quiz 클래스의 인스턴스로 퀴즈 생성
            # 아래 한 줄이 딕셔너리 데이터를 Quiz 객체 5개로 만드는 마법입니다.
            self.quizzes = [Quiz(q["question"], q["choices"], q["answer"]) for q in default_quizzes]
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

    def play_game(self):
        """1. 퀴즈 풀기 기능을 수행합니다."""
        # [요구사항] 퀴즈가 없는 경우 처리
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요.")
            return

        score = 0
        total = len(self.quizzes)
        print(f"\n🚀 퀴즈를 시작합니다! 총 {total}문제가 준비되어 있습니다.")

        # [요구사항] 저장된 퀴즈를 하나씩 출제
        for i, quiz in enumerate(self.quizzes, 1):
            quiz.display(i)  # Quiz 클래스의 출력 기능 활용
            
            # [요구사항] 사용자가 정답 입력 (보디가드 메서드 활용)
            user_answer = self.get_valid_input("정답 입력 (1-4): ", 1, 4)

            # [요구사항] 정답/오답 여부 확인
            if quiz.check_answer(user_answer):
                print("✨ 정답입니다!")
                score += 1
            else:
                print(f"❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")

        # [요구사항] 모든 문제를 풀면 결과 표시
        final_percentage = int((score / total) * 100)
        print("\n" + "="*40)
        print(f"🏁 퀴즈 종료!")
        print(f"📊 맞힌 개수: {score} / {total}")
        print(f"🏆 최종 점수: {final_percentage}점")
        print("="*40)

        # 최고 점수 갱신 및 저장
        if final_percentage > self.best_score:
            print("🎊 축하합니다! 최고 점수를 경신했습니다!")
            self.best_score = final_percentage
            self.save_data() # 점수 업데이트 후 자동 저장

    def add_quiz(self):
        """2. 새로운 퀴즈를 등록합니다."""
        print("\n" + "="*40)
        print("📌 새로운 퀴즈를 추가합니다.")
        print("="*40)

        # 1. 문제 입력 (빈 칸 방지)
        while True:
            question = input("문제를 입력하세요: ").strip()
            if question:
                break
            print("⚠️ 문제는 비워둘 수 없습니다.")

        # 2. 선택지 4개 입력
        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}: ").strip()
                if choice:
                    choices.append(choice)
                    break
                print(f"⚠️ 선택지 {i}을(를) 입력해 주세요.")

        # 3. 정답 번호 입력 (우리가 만든 보디가드 메서드 활용!)
        answer = self.get_valid_input("정답 번호 (1-4): ", 1, 4)

        # 4. Quiz 객체 생성 및 리스트 추가
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        # 5. 파일에 즉시 저장 (데이터 영속성)
        self.save_data()
        
        print("\n✅ 퀴즈가 성공적으로 추가되었습니다!")

    def show_list(self):
        """3. 저장된 퀴즈 목록을 확인합니다."""
        print("\n" + "="*40)
        # [요구사항] 퀴즈가 없는 경우 처리
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요.")
            print("="*40)
            return

        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        
        # [요구사항] 저장된 퀴즈 목록 출력
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"[{i}] {quiz.question}")
        
        print("="*40)

    def show_best_score(self):
        """4. 최고 점수를 확인합니다."""
        print("\n" + "="*40)
        # [요구사항] 아직 퀴즈를 풀지 않은 경우 (최고 점수가 0인 경우) 처리
        if self.best_score == 0:
            print("📜 아직 기록된 점수가 없습니다.")
            print("   첫 번째 퀴즈를 풀어 최고 기록을 세워보세요!")
        else:
            print(f"🏆 현재 최고 점수: {self.best_score}점")
        print("="*40)

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
                self.play_game()
                # TODO: play_game() 구현 예정
            elif choice == 2:
                self.add_quiz()
                # TODO: add_quiz() 구현 예정
            elif choice == 3:
                self.show_list()
                # TODO: show_list() 구현 예정
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                self.save_data()
                print("👋 프로그램을 종료합니다.")
                self.is_running = False

if __name__ == "__main__":
    game = QuizGame()
    game.run()