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