class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.is_running = True

    def display_menu(self):
        print("\n========================================")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def run(self):
        while self.is_running:
            self.display_menu()
            user_input = input("선택: ").strip() # 앞뒤 공백 제거

            # 1. 빈 입력 처리
            if not user_input:
                print("⚠️ 입력이 비어 있습니다. 숫자를 입력해 주세요.")
                continue

            try:
                # 2. 숫자 변환 및 메뉴 로직
                choice = int(user_input)

                if choice == 1:
                    print("\n📝 퀴즈 풀기 기능을 실행합니다...")
                elif choice == 2:
                    print("\n📌 퀴즈 추가 기능을 실행합니다...")
                elif choice == 3:
                    print("\n📋 퀴즈 목록을 출력합니다...")
                elif choice == 4:
                    print("\n🏆 최고 점수를 확인합니다...")
                elif choice == 5:
                    print("\n👋 프로그램을 종료합니다.")
                    self.is_running = False
                else:
                    # 3. 범위를 벗어난 숫자 처리
                    print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")

            except ValueError:
                # 4. 숫자가 아닌 문자 입력 처리
                print("⚠️ 숫자로만 입력해 주세요. (예: 1, 2, 3)")
            except (KeyboardInterrupt, EOFError):
                # 5. Ctrl+C 등 비정상 종료 처리
                print("\n\n⚠️ 사용자에 의해 프로그램이 중단되었습니다. 안전하게 종료합니다.")
                self.is_running = False

# 실행부
if __name__ == "__main__":
    game = QuizGame()
    game.run()