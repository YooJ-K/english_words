from cProfile import label
from distutils import command
from pickle import FALSE, TRUE
import tkinter
from tkinter import BOTTOM, CENTER, Entry, ttk
import random
from tkinter import messagebox
from turtle import left, right
from tkinter import messagebox
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

COUNT = 3

def insert():
    file_name = "words.txt"
    f = open(file_name, "a")

    var = ''
    def set_variable():
        global var

        speech = combo_part_of_speech.get()
        print(speech)
        if word.get() == '' or mean.get() == '' or speech == '품사 선택':
            messagebox.showinfo(message="입력해주세요")
            return

        s = ''
        if speech == '명사':
            s = 'n'
        elif speech == '동사':
            s = 'v'
        elif speech == '형용사':
            s = 'a'
        elif speech == '부사':
            s = 'ad'
        elif speech == '전치사':
            s = 'p'
        elif speech == '접속사':
            s = 'c'

        var = word.get() + ' ' + s + ' ' + mean.get() + ' 0\n'

        f.write(var)
        f.close()
        words.destroy()
        
        
    words = tkinter.Tk()
    words.title("단어")

    words.geometry('200x200')

    label_word = tkinter.Label(words, text="단어")
    label_word.grid(row=0, column=0)

    word = tkinter.Entry(words, width=10)
    word.grid(row=0, column=1)

    

    label_mean = tkinter.Label(words, text="뜻")
    label_mean.grid(row=1, column=0)

    mean = tkinter.Entry(words, width=10)
    mean.grid(row=1, column=1)

    label_part_of_speech = tkinter.Label(words, text="품사")
    label_part_of_speech.grid(row=2, column=0)

    combo_part_of_speech = ttk.Combobox(words, width=10, values=[
        "명사", "동사", "형용사", "부사", "전치사", "접속사", "기타"
    ])
    combo_part_of_speech.set("품사 선택")
    combo_part_of_speech.grid(row=2, column=1)

    btn_submit = tkinter.Button(words, text="제출", command=set_variable)
    btn_submit.grid(row=3, column=1)

    words.mainloop()
def test():
    idx = 0
    label_mean, btn_know, btn_no = '', '', ''

    def change_word():
        nonlocal idx, btn_mean
        s = ""
        idx += 1
        label_mean.destroy()
        if idx >= len(freq):
            s = "Finish!"
            btn_mean.destroy()

            btn = tkinter.Button(test, text="Q", command=test.destroy)
            btn.pack(side='bottom')

        else:
            s = freq[idx].split(' ')[1]
            
            btn_mean = tkinter.Button(test, text="🧐", command=show)
            btn_mean.pack()
        btn_know.destroy()
        btn_no.destroy()
        label_word.config(text=s)
    
    def know():
        nonlocal freq

        num_of_count = int(freq[idx].split(' ')[4]) 
        freq[idx] = (" ").join(freq[idx].split(' ')[0:4]) + ' ' + str(num_of_count + 1)
        change_word()

    def completeCheck():
        nonlocal words
        complete_word_idx = []
        for i, w in enumerate(words):
            if int(w.strip().split(' ')[3]) >= COUNT:
                complete_word_idx.append(i)
        complete_word_idx.sort(reverse=True)
        for i in complete_word_idx:
            words.pop(i)
    
    def show():
        nonlocal label_mean, btn_know, btn_no, btn_mean
        btn_mean.destroy()

        label_mean = tkinter.Label(test, text=freq[idx].split(' ')[3], height=0)
        label_mean.pack()

        btn_know = tkinter.Button(test, text="O", command=know)
        btn_know.pack(side='left')

        btn_no = tkinter.Button(test, text="X", command=change_word)
        btn_no.pack(side='right')

        
    f = open("words.txt", "r")
    words = f.readlines()
    f.close()
    freq = [str(i) + ' ' + w.strip() for i, w in enumerate(words)]

    random.shuffle(freq)

    test = tkinter.Tk()
    test.title("테스트")
    test.geometry('200x200')

    label_word = tkinter.Label(test, text=freq[idx].split(' ')[1], height=8)
    label_word.pack()

    btn_mean = tkinter.Button(test, text="🧐", command=show)
    btn_mean.pack()

    

    test.mainloop()

    for f in freq:
        f_line = f.split(' ')
        i = int(f_line[0])
        f_line.pop(0)

        words[i] = (" ").join(f_line)

    completeCheck()
    
    f = open("words.txt", "w")
    f.writelines(("\n").join(words))
    f.close()
def reading():
    def change_COUNT():
        global COUNT, init_lines
        
        num = entry_num.get().strip()
        if num == '':
            messagebox.showinfo(message="다시 입력해주세요")
            return
        COUNT = int()
        read_through.destroy()

        init_lines[0] = "COUNT = " + str(COUNT)

        f = open("init", "w")
        f.writelines(("\n").join(init_lines))
        f.close()

    read_through = tkinter.Tk()
    read_through.title("단어 회독 횟수")
    read_through.geometry('200x200')

    string = "단어를 몇번 회독하시겠습니까? \n현재 " + str(COUNT) + "회로 설정되어 있습니다."
    label_read_through = tkinter.Label(read_through, text=string)
    label_read_through.pack()

    entry_num = Entry(read_through)
    entry_num.pack()

    btn_count = tkinter.Button(read_through, text = "확인", command=change_COUNT)
    btn_count.pack(side="bottom")

    read_through.mainloop()
def list_of_words():
    return
def insert_file():
    return

init = open("init", 'r')
init_lines = list(init.readlines())
init.close()

for line in init_lines:
    exec(line.strip())

menu = tkinter.Tk()
menu.title("TOEIC words")
menu.geometry('200x200')

menubar = tkinter.Menu(menu)
number = tkinter.Menu(menubar)
number.add_command(label="단어 회독 횟수", command=reading)
menubar.add_cascade(label="설정", menu=number)
menu.config(menu=menubar)

btn_insert = tkinter.Button(menu, text="단어 하나 입력", command=insert)
btn_insert.pack()

btn_insert_file = tkinter.Button(menu, text="단어 파일로 입력", command=insert_file)
btn_insert_file.pack()

btn_test = tkinter.Button(menu, text="테스트 시작", command=test)
btn_test.pack()

btn_list = tkinter.Button(menu, text="단어 리스트", command=list_of_words)
btn_list.pack()

menu.mainloop()