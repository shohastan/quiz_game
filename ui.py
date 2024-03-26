import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Create window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        # Create Canvas
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # Create a canvas item
        self.quiz_text = self.canvas.create_text(150, 125, text="", font=("Arial", 20, "italic"), width=280)
        # Score Label
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        # Buttons
        check_photo = PhotoImage(file="Images/true.png")
        x_photo = PhotoImage(file="Images/false.png")
        self.check_button = Button(image=check_photo, highlightthickness=0, command=self.correct_answer)
        self.check_button.grid(column=0, row=2)
        self.x_button = Button(image=x_photo, highlightthickness=0, command=self.false_answer)
        self.x_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="There are no more questions")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def correct_answer(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def false_answer(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
