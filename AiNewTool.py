#!/usr/bin/env python
# coding: utf-8


from tkinter import *
from tkinter import ttk
import tkinter.font
import tts_model as tts
import os
import ai_human
import ai_human_train

# 설정
bg = '#2c3e50'
bnbg = '#2f3640'


# -- 메인 tkinter --
def main():
    win = Tk()
    win.geometry('800x550')
    win.title('Ai Human Integrated Tool_BTF.v1')
    win['bg']=bg

    # -- 폰트 --
    mainfont2 = tkinter.font.Font(family='맑은 고딕', size=15, weight='bold')
    mainfont = tkinter.font.Font(family='Arial', size=25, weight='bold')
    btn_font = tkinter.font.Font(family='Candara', size=25, weight='bold')
    text_font = tkinter.font.Font(family='맑은 고딕', size=13, weight='bold')
    k_font = tkinter.font.Font(family='맑은 고딕', size=9)
    btn2_font = tkinter.font.Font(family='맑은 고딕', size=13)
    null_font = tkinter.font.Font(family='맑은 고딕', size=12)

    # -- 공백용 --
    Label(win, bg=bg, text='     ').pack(side='left') # 사각 패딩
    Label(win, bg=bg, text='     ').pack(side='right')
    Label(win, bg=bg, text='     ').pack(side='top')
    Label(win, bg=bg, text='     ').pack(side='bottom')

    # -- 메인프레임 --
    main_frame = LabelFrame(win, bg=bg, text='AI_Human Integrated Tool', fg='white', font=mainfont)
    main_frame.pack(fill='both', expand=True)

    tt_frame = LabelFrame(main_frame, bg=bg, relief='flat')
    tt_frame.pack(fill='both', side='top', expand=False) # 여백용
    Label(tt_frame, bg=bg, text='     ', height=2).pack(side='top')


    btn_frame = LabelFrame(main_frame, bg=bg,relief='flat') # 버튼 프레임
    btn_frame.pack(fill='both', side='right', expand=True)


    btn_inco = Button(btn_frame, bg=bnbg, text='Start AI_Human', fg='white',
                    width=25, height=2, font=btn_font, relief='flat', command=lambda:ai_human.human_win(win, mainfont2)).pack(pady=12)
    # btn_train = Button(btn_frame, bg=bnbg, text='Start AI_Human Train', fg='white', width=25, height=2, font=btn_font, relief='flat', command=lambda:ai_human_train.train_win(win, mainfont2, k_font, btn2_font, null_font)).pack(pady=12)

    btn_tts_create = Button(btn_frame, bg=bnbg, text='Start TTS Model', fg='white',
                    width=25, height=2, font=btn_font, relief='flat', command=lambda:tts.tts_program(win, mainfont2, mainfont, k_font, text_font)).pack(pady=12)
    btn_train = Button(btn_frame, bg=bnbg, text='준비중', fg='white', 
                    width=25, height=2, font=btn_font, relief='flat').pack(pady=12)

    win.resizable(False, False)
    win.mainloop()



if __name__ == '__main__':
    main()