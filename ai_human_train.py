from tkinter import *

# 설정
bg = '#2c3e50'
bnbg = '#2f3640'


def tk_ai_human_train(win, mainfont2, k_font, btn2_font, null_font):   # AI_HUMAN TRAIN
    
    program_window = Toplevel(win)
    program_window.geometry('1366x768')
    main_Frame = LabelFrame(program_window, bg=bg, relief='flat')
    main_Frame.pack(fill='both', expand=False)

    # 타이틀
    Label(main_Frame, text='AI Human Train Tool', bg=bg, fg='white', font=mainfont2).pack() 
    Label(main_Frame, bg=bg, text='  ').pack(side='left') # 여백용
    Label(main_Frame, bg=bg, text='  ').pack(side='right')


    # 학습관리
    learning_management_frame = LabelFrame(main_Frame, bg=bg, text='학습관리',fg='white', font=mainfont2)
    learning_management_frame.pack(fill='both', expand=True, side='left')

    # 작업과정
    work_process_frame = LabelFrame(main_Frame, bg=bg, text='작업과정',fg='white', font=mainfont2)
    work_process_frame.pack(fill='both', expand=True, side='right')

    runing_imglab_flie = PhotoImage(file='./image/그래프.png', master=work_process_frame)
    runing_imglab = Label(work_process_frame, image=runing_imglab_flie, relief='flat') # 작업 과정 이미지 라벨
    runing_imglab.image = runing_imglab_flie # 가비지 컬렉션 삭제 방지
    runing_imglab.pack(anchor='center', pady=0) # **** 이미지에 따른 위치 수정 필요( 파일크기 확인하세요 )


    # 학습 프레임
    learning_frame = LabelFrame(learning_management_frame, bg=bg)
    learning_frame.pack(fill='both', expand=True, side='bottom')

    # 학습 텍스트 및 파일첨부 프레임
    learning_text_frame = LabelFrame(learning_frame, bg=bg, relief='flat')
    learning_text_frame.pack(side='left', expand=False)

    ##### 여백용 #####
    for i in range(0,10):
        for j in range(0, 3):
            Label(learning_text_frame, text='', bg=bg).grid(row=i, column=j)
    #################

    def lip_sync_check():
        select_lip = lip_intvar.get() # 선택시 1 / 아니면 0 반환
        print(f'립싱크 선택 확인 : {select_lip}')
    lip_intvar = IntVar()
    select_lip_btn = Checkbutton(learning_text_frame, text='립싱크학습(중간)', bg=bg, variable=lip_intvar, activebackground=bg, fg='white',
                             activeforeground='white', font=k_font, selectcolor=bg)
    select_lip_btn.config(command=lip_sync_check)
    select_lip_btn.grid(row=0, column=0) # 립싱크학습(중간) 유무 선택

    lip_file_information_label = Label(learning_text_frame, text='중간파일 :        ', bg=bg, fg='white', padx=15, anchor='w')
    lip_file_information_label.grid(row=1, column=0)

    lipfile_label = Label(learning_text_frame, text='C\:...\...text.mp4', bg=bg, width=30,
                              relief='ridge', anchor='w', fg='white', padx=13)
    lipfile_label.grid(row=1, column=1)

    loadlipfile_btn = Button(learning_text_frame, text='...', bg=bnbg, fg='white', relief='flat', padx=30)
    loadlipfile_btn.grid(row=1, column=3)


    def fianl_load_file_check():
        final_select_loadfile_get = final_learning_intvar.get() # 선택시 1 / 아니면 0 반환
        print(f'최종학습 선택 확인 : {final_select_loadfile_get}')
    final_learning_intvar = IntVar()
    final_learning_intvar_checkbtn = Checkbutton(learning_text_frame, text='최종학습           ', bg=bg, variable=final_learning_intvar, activebackground=bg, fg='white',
                             activeforeground='white', font=k_font, selectcolor=bg, anchor='w')
    final_learning_intvar_checkbtn.config(command=fianl_load_file_check)
    final_learning_intvar_checkbtn.grid(row=3, column=0) # 최종학습 유무 선택

    fanel_save_file_name_label = Label(learning_text_frame, text='결과파일이름 :    ', bg=bg, fg='white', padx=15).grid(row=4, column=0)
    fanel_save_file_entry = Entry(learning_text_frame, bg=bg, width=33, bd=2,
                              relief='ridge', fg='white').grid(row=4, column=1)

    final_lipfile_label2 = Label(learning_text_frame, text='립싱크파일 :       ', bg=bg, fg='white', padx=15).grid(row=6, column=0)
    fianl_lipfile_name_edit_label = Label(learning_text_frame, text='C\:...\...text.mp4', bg=bg, width=30,
                              relief='ridge', anchor='w', fg='white', padx=13).grid(row=6, column=1)
    final_loadlipfile_btn = Button(learning_text_frame, text='...', bg=bnbg, fg='white', relief='flat', padx=30).grid(row=6, column=3)

    final_voicefile_label = Label(learning_text_frame, text='중간파일 :          ', bg=bg, fg='white', padx=15).grid(row=8, column=0)
    final_voicefile_name_label = Label(learning_text_frame, text='C\:...\...text.mp4', bg=bg, width=30,
                              relief='ridge', anchor='w', fg='white', padx=13).grid(row=8, column=1)
    fianl_loadlipfile_btn = Button(learning_text_frame, text='...', bg=bnbg, fg='white', relief='flat', padx=30).grid(row=8, column=3)

    # 학습 시작 버튼 프레임
    final_start_learning_labelframe = LabelFrame(learning_frame, bg=bg, relief='flat', pady=20)
    final_start_learning_labelframe.pack(fill='both', expand=False)

    final_preprocessing_btn = Button(final_start_learning_labelframe, text='전처리 시작', bg=bnbg, fg='white',
                           relief='flat', padx=50, pady=6, font=btn2_font, anchor='w').pack()
    Label(final_start_learning_labelframe, text='', bg=bg, font=null_font).pack()
    final_pause_btn = Button(final_start_learning_labelframe, text='일시정지', bg=bnbg, fg='white', 
                           relief='flat', padx=62, pady=6, font=btn2_font).pack()
    Label(final_start_learning_labelframe, text='', bg=bg, font=null_font).pack()
    final_restart_btn = Button(final_start_learning_labelframe, text='작업게속', bg=bnbg, fg='white', 
                           relief='flat', padx=62, pady=6, font=btn2_font).pack()

    # 인물인덱스 프레임
    person_index_labelframe = LabelFrame(learning_management_frame, bg=bg, relief='flat')
    person_index_labelframe.pack(fill='both', expand=True, side='top')

    model_index_label = Label(person_index_labelframe, text='  인물 인덱스', bg=bg, fg='white', font=k_font).grid(row=0, column=0)
    for i in range(1,5):
        Entry(person_index_labelframe, width=8).grid(row=0, column=i, padx=5, pady=3)
    model_index_entry = Entry(person_index_labelframe ,width = 8).grid(row=0, column=1, columnspan=5, sticky='NEWS', padx=5, pady=3) # 인물 인덱스

    # 전처리 프레임
    pretreatment_labelframe = LabelFrame(learning_management_frame, bg=bg)
    pretreatment_labelframe.pack(fill='both', expand=False, side='right')

    def pretreatment_check():
        pretreatment_select_get = pretreatment_select_intvar.get() # 선택시 1 / 아니면 0 반환
        print(f'전처리 선택 확인 : {pretreatment_select_get}')
    pretreatment_select_intvar = IntVar()
    for i in range(0,25):
        Label(pretreatment_labelframe, text='  ', bg=bg).grid(row=0, column=i)
    pretreatment_checkbtn = Checkbutton(pretreatment_labelframe, text='전처리', bg=bg, variable=pretreatment_select_intvar, activebackground=bg, fg='white', 
                             activeforeground='white', font=k_font, selectcolor=bg, state='normal')
    pretreatment_checkbtn.config(command=pretreatment_check)
    pretreatment_checkbtn.grid(row=0, column=1) # 전처리 유무 선택
    pretreatment_video_route_btn = Button(pretreatment_labelframe, text='동영상 경로...', bg=bnbg, fg='white', height=1, widt=25, relief='flat') # 영상 버튼
    pretreatment_video_route_btn.grid(row=0, column=2, columnspan=25, sticky='NEWS', padx=5, pady=3)

    pretreatment_fileroute_label = Label(pretreatment_labelframe, text='-파일경로 : '+'C:\asdfasdf\영상경로.mp4', bg=bg, fg='white')
    pretreatment_fileroute_label.grid(row=1, column=0, columnspan=10, sticky='W',padx=20, pady=5)
    pretreatment_extension_label = Label(pretreatment_labelframe, text='-지원가능한 파일확장자 : MP4,AVI..', bg=bg, fg='white')
    pretreatment_extension_label.grid(row=2, column=0, columnspan=10, sticky='w',padx=20, pady=5)
    pretreatment_videolength_label = Label(pretreatment_labelframe, text='-영상길이:000.0프레임(00.0초)', bg=bg, fg='white')
    pretreatment_videolength_label.grid(row=3, column=0, columnspan=10, sticky='w',padx=20, pady=5)
    pretreatment_timeframe_label = Label(pretreatment_labelframe, text='-오디오 : ~~~프레임(0.00분)* 수정', bg=bg, fg='white')
    pretreatment_timeframe_label.grid(row=4, column=0, columnspan=10, sticky='w',padx=20, pady=5)

    # 녹음 파일 파동 이미지 프레임
    aduio_waveimg_labelframe = LabelFrame(pretreatment_labelframe, bg=bg)
    aduio_waveimg_labelframe.grid(row=5, column=0, columnspan=25, rowspan=10, sticky='news')

    audio_waveimg_data = PhotoImage(file='./image/음파.png', master=aduio_waveimg_labelframe)
    audio_waveimg_label = Label(aduio_waveimg_labelframe, image=audio_waveimg_data, relief='flat') # 소리 음파 이미지 라벨
    audio_waveimg_label.image = audio_waveimg_data # 가비지 컬렉션 삭제 방지
    audio_waveimg_label.pack(anchor='center', pady=10) # **** 이미지에 따른 위치 수정 필요( 파일크기 확인하세요 )

    # ai 봇 이미지 프레임
    modelimg_labelframe = LabelFrame(learning_management_frame, bg=bg)
    modelimg_labelframe.pack(fill='both', expand=True, side='bottom')

    modelimg_data = PhotoImage(file='./image/test.png', master=modelimg_labelframe)
    modelimage_label = Label(modelimg_labelframe, image=modelimg_data, relief='flat') # 아나운서 이미지 라벨
    modelimage_label.image = modelimg_data # 가비지 컬렉션 삭제 방지
    modelimage_label.pack(anchor='center', pady=0) # **** 이미지에 따른 위치 수정 필요( 파일크기 확인하세요 )
    
    if __name__ == '__main__':
        tk_ai_human_train()