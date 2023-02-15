#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import tkinter.font
import tts_model as tts
import ai_human, ai_human_train

# 설정
bg = '#2c3e50'
bnbg = '#2f3640'


# -- 메인 tkinter --
def tk_ainewtool():
    ainewtool_window = Tk()
    ainewtool_window.geometry('800x550')
    ainewtool_window.title('Ai Human Integrated Tool_BTF.v1')
    ainewtool_window['bg']=bg

    # -- 폰트 --
    mainfont2 = tkinter.font.Font(family='맑은 고딕', size=15, weight='bold')
    mainfont = tkinter.font.Font(family='Arial', size=25, weight='bold')
    btn_font = tkinter.font.Font(family='Candara', size=25, weight='bold')
    text_font = tkinter.font.Font(family='맑은 고딕', size=13, weight='bold')
    k_font = tkinter.font.Font(family='맑은 고딕', size=9)
    btn2_font = tkinter.font.Font(family='맑은 고딕', size=13)
    null_font = tkinter.font.Font(family='맑은 고딕', size=12)

    # -- 공백용 --
    Label(ainewtool_window, bg=bg, text='     ').pack(side='left')
    Label(ainewtool_window, bg=bg, text='     ').pack(side='right')
    Label(ainewtool_window, bg=bg, text='     ').pack(side='top')
    Label(ainewtool_window, bg=bg, text='     ').pack(side='bottom')

    # -- 메인프레임 --
    ainewtool_main_labelframe = LabelFrame(ainewtool_window, bg=bg, text='AI_Human Integrated Tool', fg='white', font=mainfont)
    ainewtool_main_labelframe.pack(fill='both', expand=True)

    ainewtool_gap_labelframe = LabelFrame(ainewtool_main_labelframe, bg=bg, relief='flat')
    ainewtool_gap_labelframe.pack(fill='both', side='top', expand=False) # 여백용
    Label(ainewtool_gap_labelframe, bg=bg, text='     ', height=2).pack(side='top')

    select_btn_labelframe = LabelFrame(ainewtool_main_labelframe, bg=bg,relief='flat') # 버튼 프레임
    select_btn_labelframe.pack(fill='both', side='right', expand=True)

    load_ai_human_btn = Button(select_btn_labelframe, bg=bnbg, text='Start AI_Human', fg='white',
                    width=25, height=2, font=btn_font, relief='flat', command=lambda:ai_human.tk_ai_human(ainewtool_window, mainfont2)).pack(pady=12)
    load_tts_model_btn = Button(select_btn_labelframe, bg=bnbg, text='Start TTS Model', fg='white',
                    width=25, height=2, font=btn_font, relief='flat', command=lambda:tts.tk_tts_program(ainewtool_window, mainfont2, mainfont, k_font, text_font)).pack(pady=12)
    load_ai_human_train_btn = Button(select_btn_labelframe, bg=bnbg, text='준비중', fg='white', 
                    width=25, height=2, font=btn_font, relief='flat').pack(pady=12)
    # btn_train = Button(btn_frame, bg=bnbg, text='Start AI_Human Train', fg='white', width=25, height=2, font=btn_font, relief='flat', command=lambda:ai_human_train.train_win(win, mainfont2, k_font, btn2_font, null_font)).pack(pady=12)

    ainewtool_window.resizable(False, False)
    ainewtool_window.mainloop()



if __name__ == '__main__':
    tk_ainewtool()