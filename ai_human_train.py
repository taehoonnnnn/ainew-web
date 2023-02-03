from tkinter import *
from tkinter import ttk
import tkinter.font
import os
from tkinter import filedialog
from tkinter import messagebox
import subprocess

# 설정
bg = '#2c3e50'
bnbg = '#2f3640'


def train_win(win, mainfont2, k_font, btn2_font, null_font):   # AI_HUMAN TRAIN
    
    newWindow = Toplevel(win)
    newWindow.geometry('1366x768')
    Train_frame = LabelFrame(newWindow, bg=bg, relief='flat')
    Train_frame.pack(fill='both', expand=False)

    Label(Train_frame, text='AI Human Train Tool', bg=bg, fg='white', font=mainfont2).pack() # 타이틀
    Label(Train_frame, bg=bg, text='  ').pack(side='left') # 여백용
    Label(Train_frame, bg=bg, text='  ').pack(side='right')


    # 학습관리
    frame1 = LabelFrame(Train_frame, bg=bg, text='학습관리',fg='white', font=mainfont2)
    frame1.pack(fill='both', expand=True, side='left')

    # 작업과정
    frame2 = LabelFrame(Train_frame, bg=bg, text='작업과정',fg='white', font=mainfont2)
    frame2.pack(fill='both', expand=True, side='right')

    runing_imglab_flie = PhotoImage(file='./image/그래프.png', master=frame2)
    runing_imglab = Label(frame2, image=runing_imglab_flie, relief='flat') # 작업 과정 이미지 라벨
    runing_imglab.image = runing_imglab_flie # 가비지 컬렉션 삭제 방지
    runing_imglab.pack(anchor='center', pady=0) # **** 이미지에 따른 위치 수정 필요( 파일크기 확인하세요 )


    # 학습 프레임
    run_frame = LabelFrame(frame1, bg=bg)
    run_frame.pack(fill='both', expand=True, side='bottom')

    # 학습 텍스트 및 파일첨부 프레임
    text_Frame = LabelFrame(run_frame, bg=bg, relief='flat')
    text_Frame.pack(side='left', expand=False)

    ##### 여백용 #####
    for i in range(0,10):
        for j in range(0, 3):
            Label(text_Frame, text='', bg=bg).grid(row=i, column=j)
    #################

    def min_run_click():
        m_run_yn = m_rv.get() # 선택시 1 / 아니면 0 반환
        print(f'립싱크 선택 확인 : {m_run_yn}')
    m_rv = IntVar()
    btn_m_run_yn = Checkbutton(text_Frame, text='립싱크학습(중간)', bg=bg, variable=m_rv, activebackground=bg, fg='white',
                             activeforeground='white', font=k_font, selectcolor=bg)
    btn_m_run_yn.config(command=min_run_click)
    btn_m_run_yn.grid(row=0, column=0) # 립싱크학습(중간) 유무 선택

    Lab_min_file = Label(text_Frame, text='중간파일 :        ', bg=bg, fg='white', padx=15, anchor='w')
    Lab_min_file.grid(row=1, column=0)

    Lab_min_file_name = Label(text_Frame, text='C\:...\...text.mp4', bg=bg, width=30,
                              relief='ridge', anchor='w', fg='white', padx=13)
    Lab_min_file_name.grid(row=1, column=1)

    btn_min_file = Button(text_Frame, text='...', bg=bnbg, fg='white', relief='flat', padx=30)
    btn_min_file.grid(row=1, column=3)

    def run_click():
        run_yn = rv.get() # 선택시 1 / 아니면 0 반환
        print(f'최종학습 선택 확인 : {run_yn}')
    rv = IntVar()
    btn_run_yn = Checkbutton(text_Frame, text='최종학습           ', bg=bg, variable=rv, activebackground=bg, fg='white',
                             activeforeground='white', font=k_font, selectcolor=bg, anchor='w')
    btn_run_yn.config(command=run_click)
    btn_run_yn.grid(row=3, column=0) # 최종학습 유무 선택

    Lab_last_file = Label(text_Frame, text='결과파일이름 :    ', bg=bg, fg='white', padx=15).grid(row=4, column=0)
    Lab_last_file_name = Entry(text_Frame, bg=bg, width=33, bd=2,
                              relief='ridge', fg='white').grid(row=4, column=1)

    Lab_fake_file = Label(text_Frame, text='립싱크파일 :       ', bg=bg, fg='white', padx=15).grid(row=6, column=0)
    Lab_fake_file_name = Label(text_Frame, text='C\:...\...text.mp4', bg=bg, width=30,
                              relief='ridge', anchor='w', fg='white', padx=13).grid(row=6, column=1)
    btn_fake_file = Button(text_Frame, text='...', bg=bnbg, fg='white', relief='flat', padx=30).grid(row=6, column=3)

    Lab_last_min_file = Label(text_Frame, text='중간파일 :          ', bg=bg, fg='white', padx=15).grid(row=8, column=0)
    Lab_last_min_file_name = Label(text_Frame, text='C\:...\...text.mp4', bg=bg, width=30,
                              relief='ridge', anchor='w', fg='white', padx=13).grid(row=8, column=1)
    btn_min_file = Button(text_Frame, text='...', bg=bnbg, fg='white', relief='flat', padx=30).grid(row=8, column=3)


    # 학습 시작 버튼 프레임
    btn_run_frame = LabelFrame(run_frame, bg=bg, relief='flat', pady=20)
    btn_run_frame.pack(fill='both', expand=False)

    btn_cut_start = Button(btn_run_frame, text='전처리 시작', bg=bnbg, fg='white',
                           relief='flat', padx=50, pady=6, font=btn2_font, anchor='w').pack()
    Label(btn_run_frame, text='', bg=bg, font=null_font).pack()
    btn_cut_start = Button(btn_run_frame, text='일시정지', bg=bnbg, fg='white', 
                           relief='flat', padx=62, pady=6, font=btn2_font).pack()
    Label(btn_run_frame, text='', bg=bg, font=null_font).pack()
    btn_cut_start = Button(btn_run_frame, text='작업게속', bg=bnbg, fg='white', 
                           relief='flat', padx=62, pady=6, font=btn2_font).pack()


    #######################

    # 인물인덱스 프레임
    model_frame = LabelFrame(frame1, bg=bg, relief='flat')
    model_frame.pack(fill='both', expand=True, side='top')

    model_lab = Label(model_frame, text='  인물 인덱스', bg=bg, fg='white', font=k_font).grid(row=0, column=0)
    for i in range(1,5):
        Entry(model_frame, width=8).grid(row=0, column=i, padx=5, pady=3)
    model_ent = Entry(model_frame ,width = 8).grid(row=0, column=1, columnspan=5, sticky='NEWS', padx=5, pady=3) # 인물 인덱스

    # 전처리 프레임
    data_cut_frame = LabelFrame(frame1, bg=bg)
    data_cut_frame.pack(fill='both', expand=False, side='right')

    def data_click():
        cut_yn = cv.get() # 선택시 1 / 아니면 0 반환
        print(f'전처리 선택 확인 : {cut_yn}')
    cv = IntVar()
    for i in range(0,25):
        Label(data_cut_frame, text='  ', bg=bg).grid(row=0, column=i)
    btn_cut_yn = Checkbutton(data_cut_frame, text='전처리', bg=bg, variable=cv, activebackground=bg, fg='white', 
                             activeforeground='white', font=k_font, selectcolor=bg, state='normal')
    btn_cut_yn.config(command=data_click)
    btn_cut_yn.grid(row=0, column=1) # 전처리 유무 선택
    cut_flie = Button(data_cut_frame, text='동영상 경로...', bg=bnbg, fg='white', height=1, widt=25, relief='flat') # 영상 버튼
    cut_flie.grid(row=0, column=2, columnspan=25, sticky='NEWS', padx=5, pady=3)

    cutlab1 = Label(data_cut_frame, text='-파일경로 : '+'C:\asdfasdf\영상경로.mp4', bg=bg, fg='white')
    cutlab1.grid(row=1, column=0, columnspan=10, sticky='W',padx=20, pady=5)
    cutlab2 = Label(data_cut_frame, text='-지원가능한 파일확장자 : MP4,AVI..', bg=bg, fg='white')
    cutlab2.grid(row=2, column=0, columnspan=10, sticky='w',padx=20, pady=5)
    cutlab3 = Label(data_cut_frame, text='-영상길이:000.0프레임(00.0초)', bg=bg, fg='white')
    cutlab3.grid(row=3, column=0, columnspan=10, sticky='w',padx=20, pady=5)
    cutlab4 = Label(data_cut_frame, text='-오디오 : ~~~프레임(0.00분)* 수정', bg=bg, fg='white')
    cutlab4.grid(row=4, column=0, columnspan=10, sticky='w',padx=20, pady=5)

    # 녹음 파일 파동 이미지 프레임
    aud_img_frame = LabelFrame(data_cut_frame, bg=bg)
    aud_img_frame.grid(row=5, column=0, columnspan=25, rowspan=10, sticky='news')

    aud_img_file = PhotoImage(file='./image/음파.png', master=aud_img_frame)
    aud_img = Label(aud_img_frame, image=aud_img_file, relief='flat') # 소리 음파 이미지 라벨
    aud_img.image = aud_img_file # 가비지 컬렉션 삭제 방지
    aud_img.pack(anchor='center', pady=10) # **** 이미지에 따른 위치 수정 필요( 파일크기 확인하세요 )

    # ai 봇 이미지 프레임
    model_img = LabelFrame(frame1, bg=bg)
    model_img.pack(fill='both', expand=True, side='bottom')

    model_img_file = PhotoImage(file='./image/test.png', master=model_img)
    model_imglab = Label(model_img, image=model_img_file, relief='flat') # 아나운서 이미지 라벨
    model_imglab.image = model_img_file # 가비지 컬렉션 삭제 방지
    model_imglab.pack(anchor='center', pady=0) # **** 이미지에 따른 위치 수정 필요( 파일크기 확인하세요 )
    