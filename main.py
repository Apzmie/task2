class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question   # 문제 내용
        self.choices = choices     # 보기 4개 (리스트)
        self.answer = answer       # 정답 번호 (1~4)

    def display(self, index):
        """문제를 화면에 출력하는 기능"""
        print(f"\n[문제 {index}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        """정답 확인 기능"""
        return self.answer == user_answer

# --- 여기서부터 실제 게임 데이터와 실행 로직입니다 ---

def run_game():
    # 1. 퀴즈 문제 5개 생성
    quiz_list = [
        Quiz("대한민국의 수도는 어디인가요?", ["인천", "광주", "서울", "부산"], 3),
        Quiz("파이썬(Python)을 만든 사람은?", ["귀도 반 로섬", "제임스 고슬링", "빌 게이츠", "마크 저커버그"], 1),
        Quiz("태양계에서 가장 큰 행성은?", ["지구", "화성", "목성", "토성"], 3),
        Quiz("컴퓨터의 '뇌' 역할을 하는 부품은?", ["RAM", "HDD", "CPU", "GPU"], 3),
        Quiz("MBTI 중 '성인군자형'으로 불리는 유형은?", ["ISFJ", "ENFP", "ISTP", "ENTJ"], 1)
    ]

    score = 0
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃      🔥 초간단 퀴즈 게임 🔥      ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    # 2. 문제 하나씩 출제
    for i, q in enumerate(quiz_list, 1):
        q.display(i)
        
        try:
            # 사용자로부터 정답 번호 입력받기
            user_input = int(input("정답 번호를 입력하세요 (1~4): "))
            
            if q.is_correct(user_input):
                print("정답입니다! ✨")
                score += 1
            else:
                print(f"아쉽네요. 정답은 {q.answer}번입니다. 😢")
        except ValueError:
            print("❌ 숫자만 입력해주세요! 이번 문제는 틀린 것으로 처리됩니다.")

    # 3. 최종 결과 발표
    print("\n" + "="*30)
    print(f"게임 종료! 당신의 점수는 {score} / {len(quiz_list)}점 입니다.")
    print("="*30)

if __name__ == "__main__":
    run_game()