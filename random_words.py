from asyncore import read
from cProfile import label
from distutils import command
from pickle import FALSE, TRUE
import tkinter
from tkinter import CENTER, Button, DoubleVar, Entry, ttk
import random
from tkinter import messagebox
from turtle import left, right
from tkinter import messagebox
import os

from numpy import double
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from tkinter import filedialog

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
    def change_by_enter(event):
        change_COUNT

    def change_COUNT():
        global COUNT, init_lines
        
        num = entry_num.get().strip()
        if num == '':
            messagebox.showinfo(message="다시 입력해주세요")
            return
        COUNT = int(num)
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
    entry_num.bind("<Enter>", change_by_enter)
    entry_num.pack()

    btn_count = tkinter.Button(read_through, text = "확인", command=change_COUNT)
    btn_count.pack()

    read_through.mainloop()
def list_of_words():
    result_of_words = []
    exec_num = 0
    def delete_word():
        nonlocal table, result_of_words, exec_num

        exec_num += 1

        idx = table.focus()
        table.delete(table.item(idx).get('text'))

        result_of_words = []
        for idx in table.get_children():
            table_item = table.item(idx).get('values')
            table_item[3] = str(table_item[3])
            result_of_words.append(table_item)
        
    def event_of_mouse(event):
        if messagebox.askyesno("Delete", "삭제하시겠습니까?"):
            delete_word()

    lists = tkinter.Tk()
    lists.title("단어 목록")
    lists.bind("<BackSpace>", event_of_mouse)
    lists.bind("x", event_of_mouse)

    scrollbar=tkinter.Scrollbar(lists)
    scrollbar.pack(side="right", fill="y")

    table = ttk.Treeview(lists, \
        columns=["단어", "품사", "뜻", "횟수"], \
            displaycolumns=["단어", "품사", "뜻", "횟수"], yscrollcommand=scrollbar.set)
    table.pack()

    table.column("#0", width=50)
    table.column("#1", width=100, anchor="w")
    table.column("#2", width=30)
    table.column("#3", width=70)
    table.column("#4", width=40)

    table.heading("#1", text="단어", anchor="center")
    table.heading("#2", text="품사", anchor="center")
    table.heading("#3", text="뜻", anchor="center")
    table.heading("#4", text="회독수", anchor="center")

    f = open("words.txt", "r")
    words = f.readlines()
    f.close()

    for i, word in enumerate(words):
        table.insert('', 'end', text=(i+1), values=word, iid=str(i+1))
    scrollbar["command"] = table.yview

    for idx in table.get_children():
        table_item = table.item(idx).get('values')
        table_item[3] = str(table_item[3])
        result_of_words.append(table_item)

    lists.mainloop()

    if exec_num > 0:
        lines = []
        for line in result_of_words:
            lines.append((" ").join(line))

        f = open("words.txt", "w")
        f.writelines(("\n").join(lines) + "\n")
        f.close()
def insert_file():
    
    file = tkinter.Tk()
    file.title('단어 파일로 입력하기')
    file.geometry('200x200')

    def open_files():
        filename = filedialog.askopenfilename(initialdir='', title="txt 파일 선택", \
            filetypes=(
                ('txt files', '*.txt'),
                ("all files","*.*")
                )
            )
        print(filename)

        label_file = tkinter.Label(file, text=filename.split('/')[-1])
        label_file.pack()

        p = 0.0
        progress = ttk.Progressbar(file, maximum=100, length=180, variable=p)
        progress.pack()

        progress.start(50000)

        f = open(filename, "r")
        lines = f.readlines()
        len_lines = len(lines)
        f.close()

        f = open("words.txt", "a")
        for i, line in enumerate(lines):
            p = i / double(len_lines) * 100
            progress.update()

            f.write(line.strip() + ' 0\n')
        f.close()

        progress.destroy()
        file.destroy()
        
    btn_open = tkinter.Button(file, text="파일 불러오기", command=open_files)
    btn_open.pack(fill='both')

    file.mainloop()

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