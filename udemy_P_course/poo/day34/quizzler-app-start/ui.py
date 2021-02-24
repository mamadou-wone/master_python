from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzier")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_txt = self.canvas.create_text(150, 125,
                                                    text="",
                                                    font=FONT,
                                                    fill=THEME_COLOR,
                                                    width=280
                                                    )

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, command=self.got_it)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_image, command=self.error)
        self.false_button.grid(column=1, row=2)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_txt, text="Fin du Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def got_it(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def error(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)
