import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import ImageTk, Image
import random
import json 
import os

DATA_PATH = os.path.join(os.path.abspath(__file__ + '/..'), 'questions.json')
DATA_IMAGE = os.path.join(os.path.abspath(__file__ + '/..'), 'images\\')

if os.path.exists(DATA_PATH):
    with open(DATA_PATH, 'r') as f:
        questions = json.load(f)
else:
    questions = []
print (DATA_IMAGE)
class Millionario(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.BG_COLOR = "#3A2F59"
        self.question_index = 0
        self.prize = 0
        self.title("Хто хоче стати мільйонером?")
        self.resizable(False, False)
        self.geometry("800x450")
        self.logo = PhotoImage(file=f'{DATA_IMAGE}WWTBAM_US_Logo.png')
        self.iconphoto(False, self.logo)
        self.bg_image = ImageTk.PhotoImage(Image.open(f'{DATA_IMAGE}WWTBAM_UA_logo.png'))
        tk.Label(self, image=self.bg_image).place(x=0, y=0, relwidth=1)
        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_frame = tk.Frame(self, bg = self.BG_COLOR)
        self.question_frame.place(x=0, y=270, width=800, height=180)
        self.question_label = tk.Label(self.question_frame ,text="", bg=self.BG_COLOR, fg="white", font=("Arial", 14))
        self.question_label.pack()
        self.prize_label = tk.Label(self ,text=f"Твій виграш:\n{self.prize} грн.", bg=self.BG_COLOR, fg="white", font=("Arial", 14))
        self.prize_label.place(x=60, y=10)

        self.frames = []
        for i in range(4):
            frame = tk.Frame(self, bg=self.BG_COLOR)
            frame.place(x= 0 if i%2==0 else 400, y=350 if i < 2 else 400, width=400, height=50)
            self.frames.append(frame)
    
        self.answer_buttons = []
        for i in range(4):
            btn = tk.Button(self.frames[i], text="", font=("Arial", 14), width=50, fg="white", bg=self.BG_COLOR, activebackground="#fa7e02",  command=lambda i=i: self.check_answer(i))
            btn.pack(side=tk.TOP)
            self.answer_buttons.append(btn)              

        self.help_img_1 = tk.PhotoImage(file=f'{DATA_IMAGE}fifty_fifty.png')
        self.help_btn_1 = tk.Button(self, command=self.fifty_fifty, image=self.help_img_1, width=50, background=self.BG_COLOR, activebackground="#fa7e02")
        self.help_btn_1.place(x=570, y=10)
        self.help_img_2 = tk.PhotoImage(file=f'{DATA_IMAGE}call_friend.png')
        self.help_btn_2 = tk.Button(self, command=self.call_friend, image=self.help_img_2, width=50, background=self.BG_COLOR, activebackground="#fa7e02")
        self.help_btn_2.place(x=630, y=10)        
        self.help_img_3 = tk.PhotoImage(file=f'{DATA_IMAGE}hall_help.png')
        self.help_btn_3 = tk.Button(self, command=self.hall_help, image=self.help_img_3, width=50, background=self.BG_COLOR, activebackground="#fa7e02")
        self.help_btn_3.place(x=690, y=10)
          
    def fifty_fifty(self):
        self.help_btn_1['state']=tk.DISABLED
        self.help_btn_1['background']="red"
        correct_answer = questions[self.question_index]["answer"]
        incorrect_options = [option for option in questions[self.question_index]["options"] if option != correct_answer]
        two_to_hide = random.sample(incorrect_options, 2)
        for btn in self.answer_buttons:
            if btn.cget("text") in two_to_hide:
                btn.config(state=tk.DISABLED)
    
    def call_friend(self):
        self.help_btn_2['state']=tk.DISABLED
        self.help_btn_2['background']="red"    
        correct_answer = questions[self.question_index]["answer"]
        friend_advice = random.choice([correct_answer, random.choice(questions[self.question_index]["options"])])
        messagebox.showinfo("Дзвінок другу", f"Друг думає, що правильна відповідь: {friend_advice}")
                
    def hall_help(self):
        self.help_btn_3['state']=tk.DISABLED
        self.help_btn_3['background']="red"
        correct_answer = questions[self.question_index]["answer"]
        votes = [0, 0, 0, 0]

        correct_index = questions[self.question_index]["options"].index(correct_answer)
        votes[correct_index] = random.randint(45, 90)

        remaining_percent = 100 - votes[correct_index]
        incorrect_indices = [i for i in range(4) if i != correct_index]
        cnt = 0
        for i in incorrect_indices:
            cnt += 1
            if cnt == 3:
                votes[i] = remaining_percent
            else:   
                votes[i] = random.randint(0, remaining_percent // 2)
                remaining_percent -= votes[i]

        vote_message = "\n".join([f"{questions[self.question_index]['options'][i]}: {votes[i]}%" for i in range(4)])
        messagebox.showinfo("Допомога залу", f"Результати голосування:\n\n{vote_message}")

    def display_question(self):
        if self.question_index < len(questions):
            q = questions[self.question_index]
            self.question_label.config(text=f'{q["question"]}\nВиграш: {q["prize"]} грн.')
            for i, option in enumerate(q["options"]):
                self.answer_buttons[i].config(text=option, state=tk.NORMAL, bg=self.BG_COLOR)
        else:
            self.end_game()
    
    def check_answer(self, i):
        selected_option = self.answer_buttons[i].cget("text")
        correct_answer = questions[self.question_index]["answer"]
        prize = questions[self.question_index]["prize"]
        if selected_option == correct_answer:
            self.answer_buttons[i]['background']="green"
            self.prize += prize
            self.prize_label.config(text=f"Твій виграш:\n{self.prize} грн.")
            messagebox.showinfo("Відповідь", f"Правильно!\nТи виграв {prize} грн.")           
        else:
            self.answer_buttons[i]['background']="#fa7e02"
            for btn in self.answer_buttons:
                if btn.cget("text") == correct_answer:
                    btn['background']="green"
            messagebox.showinfo("Відповідь", f"Невірно!\nПравильна відповідь {correct_answer}")                    
        self.question_index += 1
        self.display_question()

    def end_game(self):
        messagebox.showinfo("Гра закінчена", "Дякую за гру!")
        self.quit()

    
if __name__ == "__main__":
    app = Millionario()
    app.mainloop()
