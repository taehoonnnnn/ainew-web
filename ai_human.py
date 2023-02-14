from threading import *
from tkinter import * 
from tkinter import messagebox, filedialog
from tkinter.tix import COLUMN
import cv2, av, os, wave, subprocess, datetime, shutil, wave, librosa, librosa.display 
import matplotlib.pyplot as plt

# 설정
bg = '#2c3e50'
bnbg = '#2f3640'
fg = 'white'


def get_extract_video_information(filename): # 비디오 정보 추출
    container = av.open(filename)
    video = container.streams.video[0]
    frames = container.decode(video=0)
    fps = video.average_rate
    fps_calculate = int(str(fps).split('/')[0]) / int(str(fps).split('/')[1])
    print("fps : " + str(fps_calculate))
    print("movie seconds : " + str(round(video.frames, 2) / fps_calculate))
    seconds = video.frames/fps_calculate
    video_file_length_label.config(text='-영상길이 : ' + str(round(fps_calculate, 2)) + '프레임' + f'({round(seconds,1)}초)')


# -- 동영상 메인 사진 변경 --
def set_video_main_picture(path, name):
    vidcap = cv2.VideoCapture(path)
    success,image = vidcap.read()
    success = True
    resize_img = cv2.resize(image, (309,331))
    cv2.imwrite(f"./image/{name}.png", resize_img)
    vidcap.release()


def get_video_file(): # 비디오 파일 열기
    global video_file_path
    video_file_path = filedialog.askopenfilename(initialdir='', title='동영상 파일선택', filetypes=(
    ('mp4 files', '*.mp4'), ('avi files', '*.avi'), ('all files', '*.*')))
    try:
        get_extract_video_information(video_file_path)
        print(video_file_path)
        video_file_path_label.config(text='-파일경로 : ' + video_file_path)
        name = 'image'
        set_video_main_picture(video_file_path, name)
        img_change = PhotoImage(file=f'./image/{name}.png', master=video_right_labelframe)
        video_img_label.image = img_change
        video_img_label.configure(image=img_change)
    except:
        messagebox.showinfo("오류", "오류")
    
    
def get_extract_audio_information(filename): # 오디오 정보 추출
    audio = wave.open(filename)
    frames = audio.getnframes()
    rate = audio.getframerate()
    seconds = frames/float(rate)
    audio_file_lenght_label.config(text='-오디오길이 : ' + f'{round(seconds,1)}초')


# -- 오디오 메인 스펙트럼 사진 변경 --
def set_audio_spectrum_image(path, name):
    sig, sr = librosa.load(path, sr = 23500)
    plt.figure(figsize = (5.04,2.88))
    plt.axis('off')
    librosa.display.waveshow(sig, sr, color='white', alpha=1)
    plt.savefig(f'./image/{name}.png', facecolor=bg, pad_inches=0)
    
    
def get_audio_file(): # 오디오 파일 열기
    global audio_file_path
    audio_file_path = filedialog.askopenfilename(initialdir='', title='동영상 파일선택', filetypes=(
    ('wav files', '*.wav'), ('mp3 files', '*.mp3'), ('all files', '*.*')))
    try:
        get_extract_audio_information(audio_file_path)
        print(audio_file_path)
        name = 'audio'
        set_audio_spectrum_image(audio_file_path, name)
        img_change = PhotoImage(file=f'./image/{name}.png', master=audio_right_labelframe)
        audio_img_label.image = img_change
        audio_img_label.configure(image=img_change)     
    except:
        messagebox.showinfo("오류", "파일을 선택해주세요.")

# -- 최종 AI 모델 저장 경로 --
def get_final_aimodel_path():
    global ai_path
    ai_path = filedialog.askdirectory()
    print(ai_path)
    savefile_path_label.config(text=ai_path)

# -- 쓰레드 --
def therading_final_ai():
    try:
        t1 = Thread(target=model_synth)
        t1.daemon = True
        t1.start()
    except:
        print(f'Thread error : {t1}')


# -- TTS + LipFake Start --
def model_synth():
    try:
        outfile = ai_path+'/'+savefile_name_edit_entry.get()
        print(outfile)
        cmd = f'python lipfake/inference.py --checkpoint_path ./checkpoints/wav2lip_gan.pth --face {video_file_path} --audio {audio_file_path} --outfile {outfile}.mp4 --resize_factor 2'
        status_message_label.config(text='AI 생성중...')
        print(cmd)
        subprocess.run(cmd)
 
        status_message_label.config(text='최근작업 저장중...')   
        
        # -- 이미지 복사 --
        path_dir = './save'
        filecnt = os.listdir(path_dir)[:4]
        
        vidcap2 = cv2.VideoCapture(video_file_path)
        success,image = vidcap2.read()
        success = True
        resize_img2 = cv2.resize(image, (100,90))
        
        if '1.png' not in filecnt:
            cv2.imwrite('./save/1.png', resize_img2)
            print('1')
            
        elif '2.png' not in filecnt:
            cv2.imwrite('./save/2.png', resize_img2)
            print('2')
            
        elif '3.png' not in filecnt:
            cv2.imwrite('./save/3.png', resize_img2)
            print('3')
            
        elif '4.png' not in filecnt:
            cv2.imwrite('./save/4.png', resize_img2)
            print('4')

        elif '4.png' in filecnt:
            cv2.imwrite('./save/5.png', resize_img2)
            os.remove('./save/1.png')

            for i in range(len(filecnt)):
                src = os.path.join(path_dir, str(i+2)+'.png')
                dst = str(i+1) + '.png'
                dst = os.path.join(path_dir, dst)
                os.rename(src, dst)
        
        # -- 영상 복사 --
        video_path_dir = './save/video/'
        videocnt = os.listdir(video_path_dir)
        
        if 'save_1.mp4' not in videocnt:
            shutil.copy2(f'{outfile}.mp4', f'{video_path_dir}save_1.mp4')
            
        elif 'save_2.mp4' not in videocnt:
            shutil.copy2(f'{outfile}.mp4', f'{video_path_dir}save_2.mp4')
            
        elif 'save_3.mp4' not in videocnt:
            shutil.copy2(f'{outfile}.mp4', f'{video_path_dir}save_3.mp4')
            
        elif 'save_4.mp4' not in videocnt:
            shutil.copy2(f'{outfile}.mp4', f'{video_path_dir}save_4.mp4')

        elif 'save_4.mp4' in videocnt:
            shutil.copy2(f'{outfile}.mp4', f'{video_path_dir}save_5.mp4')
            os.remove('./save/video/save_1.mp4')
            
            for i in range(len(videocnt)):
                src = os.path.join(video_path_dir, f'save_{str(i+2)}.mp4')
                dst = f'save_{str(i+1)}.mp4'
                dst = os.path.join(video_path_dir, dst)
                os.rename(src, dst)
        
        befo_img = PhotoImage(file='./save/1.png', master=beforefile_img_frame)
        beforefile_img_label_1.image = befo_img
        beforefile_img_label_1.configure(image=befo_img)
        
        befo_img = PhotoImage(file='./save/2.png', master=beforefile_img_frame)
        beforefile_img_label_2.image = befo_img
        beforefile_img_label_2.configure(image=befo_img)

        befo_img = PhotoImage(file='./save/3.png', master=beforefile_img_frame)
        beforefile_img_label_3.image = befo_img
        beforefile_img_label_3.configure(image=befo_img)

        befo_img = PhotoImage(file='./save/4.png', master=beforefile_img_frame)
        beforefile_img_label_4.image = befo_img
        beforefile_img_label_4.configure(image=befo_img)
        
        video_dir = os.getcwd()
        
        beforefile_img_label_4.image = befo_img
        beforefile_img_label_4.configure(image=befo_img)
        
        beforefile_path_label_1.config(text=fr"{video_dir}\save\video\{videocnt[0]}")
        beforefile_time_label_1.config(text=f"{datetime.datetime.fromtimestamp(os.path.getmtime(video_path_dir+videocnt[0]))}")
        
        beforefile_path_label_2.config(text=fr"{video_dir}\save\video\{videocnt[1]}")
        beforefile_time_label_2.config(text=f"{datetime.datetime.fromtimestamp(os.path.getmtime(video_path_dir+videocnt[1]))}")
        
        beforefile_path_label_3.config(text=fr"{video_dir}\save\video\{videocnt[2]}")
        beforefile_time_label_3.config(text=f"{datetime.datetime.fromtimestamp(os.path.getmtime(video_path_dir+videocnt[2]))}")
        
        beforefile_path_label_4.config(text=fr"{video_dir}\save\video\{videocnt[3]}")
        beforefile_time_label_4.config(text=f"{datetime.datetime.fromtimestamp(os.path.getmtime(video_path_dir+videocnt[3]))}")
        
        status_message_label.config(text='생성 완료')
    except:
        status_message_label.config(text='파일 생성 오류')



def tk_ai_human(win, mainfont2):  # AI_HUMAN

    tk_window = Toplevel(win)
    tk_window.geometry('1450x770')
    
    main_labelframe = LabelFrame(tk_window, bg=bg, relief='flat')
    main_labelframe.pack(fill='both', expand=False)

    title_label = Label(main_labelframe, text='AI NEW ROOM', bg=bg, fg='white', font=mainfont2)
    title_label.pack() # 타이틀
    
    Label(main_labelframe, bg=bg, text='  ').pack(side='left') # 여백용
    Label(main_labelframe, bg=bg, text='  ').pack(side='right')

    main_left_labelframe = LabelFrame(main_labelframe, bg=bg, relief='flat',width=800, height=150)
    main_left_labelframe.pack(fill='both', expand=True, side='left')

    main_right_labelframe = LabelFrame(main_labelframe, bg=bg, relief='flat',width=800, height=150)
    main_right_labelframe.pack(fill='both', expand=True, side='right')

    # 동영상 프레임
    video_main_labelframe = LabelFrame(main_left_labelframe, bg=bg, text='동영상', relief='groove', width=500, height=150, font=mainfont2, fg='white')
    video_main_labelframe.pack(fill='both', expand=False) # 메인프레임

    video_left_labelframe = LabelFrame(video_main_labelframe, bg=bg, relief='flat') # 왼쪽 프레임
    video_left_labelframe.pack(fill='both', expand=True, side='left', padx=20)

    video_loadfile_btn = Button(video_left_labelframe, text='파일업로드', height=3, widt=25, bg=bnbg, 
                    fg='white', relief='flat', command=get_video_file).pack(pady=20)
    
    global video_file_path_label, video_file_length_label, video_img_label, video_right_labelframe
    video_file_path_label = Label(video_left_labelframe, text='-파일경로 : '+'C:\영상경로.mp4', bg=bg, fg='white')
    video_file_path_label.pack(anchor='nw', padx=20, pady=10)
    
    video_file_extension_label = Label(video_left_labelframe, text='-지원가능한 파일확장자 : MP4,AVI..', bg=bg, fg='white')
    video_file_extension_label.pack(anchor='nw', padx=20, pady=10)
    
    video_file_resolution_label = Label(video_left_labelframe, text='-해상도 : 1080x1920', bg=bg, fg='white')
    video_file_resolution_label.pack(anchor='nw', padx=20, pady=10)
    
    video_file_length_label = Label(video_left_labelframe, text='-영상길이 : ~~~fps(0.00)', bg=bg, fg='white')
    video_file_length_label.pack(anchor='nw', padx=20, pady=10)

    video_right_labelframe = LabelFrame(video_main_labelframe, bg=bg) # 오른쪽 프레임
    video_right_labelframe.pack(fill='both', expand=True, side='right')

    video_loadimgfile_photoimage = PhotoImage(file='./image/test.png', master=video_right_labelframe)
    video_img_label = Label(video_right_labelframe, image=video_loadimgfile_photoimage, relief='flat') # 아나운서 이미지 라벨
    video_img_label.image = video_loadimgfile_photoimage # 가비지 컬렉션 삭제 방지
    video_img_label.pack(anchor='center', pady=10) # **** 이미지에 따른 위치 수정 필요( 파일크기 확인하세요 )


    # 오디오 프레임
    audio_main_frame = LabelFrame(main_left_labelframe, bg=bg, text='오디오', relief='groove',width=500, height=450, font=mainfont2, fg='white') # 메인 프레임
    audio_main_frame.pack(fill='both', expand=False)

    audio_left_frame = LabelFrame(audio_main_frame, bg=bg, relief='flat') # 왼쪽 프레임
    audio_left_frame.pack(fill='both', expand=True, side='left', padx=20)

    global audio_file_lenght_label, audio_right_labelframe,audio_img_label
    audio_loadfile_btn = Button(audio_left_frame, text='파일업로드', height=3, widt=25, bg=bnbg, fg='white', relief='flat',
                    command=get_audio_file).pack(pady=30)
    audio_file_extension_label = Label(audio_left_frame, text='-지원가능한 파일 확장자 : WAV,MP3', bg=bg, fg='white').pack(anchor='nw', padx=20, pady=10)
    audio_file_lenght_label = Label(audio_left_frame, text='-오디오길이 : 00.0초', bg=bg, fg='white')
    audio_file_lenght_label.pack(anchor='nw', padx=20, pady=10)

    audio_right_labelframe = LabelFrame(audio_main_frame, bg=bg) # 오른쪽 프레임
    audio_right_labelframe.pack(fill='both', expand=False, side='right')

    audio_loadimgfile_photoimage = PhotoImage(file='./image/audio.png', master=video_right_labelframe)
    audio_img_label = Label(audio_right_labelframe, image=audio_loadimgfile_photoimage) # 소리 음파 이미지 라벨
    audio_img_label.image = audio_loadimgfile_photoimage # 가비지 컬렉션 삭제 방지
    audio_img_label.pack(anchor='center', pady=10) # **** 이미지에 따른 위치 수정 필요( 파일크기 확인할 것 )


    # -- 작업진행 프레임 --
    work_progress_labelframe = LabelFrame(main_right_labelframe, bg=bg, text='작업진행', relief='groove',
                            width=5000, height=20, font=mainfont2, fg='white')
    work_progress_labelframe.pack(expand=False, fill="both")

    work_progress_bottom_labelframe = LabelFrame(work_progress_labelframe, bg=bg, relief='flat')
    work_progress_bottom_labelframe.pack(fill='both', expand=False, side='bottom', pady=10) # 하단프레임
    
    start_compositing_btn = Button(work_progress_bottom_labelframe, text='합성시작', bg=bnbg, fg='white', height=3, width=110, relief='flat', command=therading_final_ai)
    start_compositing_btn.pack()
    
    global status_message_label
    status_message_label = Label(work_progress_bottom_labelframe, text='시작대기중', bg=bg, fg='white', relief='groove',height=2, width=110)
    status_message_label.pack()

    work_progress_left_labelframe = LabelFrame(work_progress_labelframe, bg=bg, relief='flat')
    work_progress_left_labelframe.pack(fill='both', expand=False, side='left', pady=10) # 왼쪽프레임
    
    savefile_path_text_label = Label(work_progress_left_labelframe, bg=bg, text='저장경로', fg='white').pack(anchor='nw', padx=20, pady=3)
    savefile_name_text_label = Label(work_progress_left_labelframe, bg=bg, text='저장파일이름', fg='white').pack(anchor='nw', padx=20, pady=3)

    work_progress_right_labelframe = LabelFrame(work_progress_labelframe, bg=bg, relief='flat')
    work_progress_right_labelframe.pack(fill='both', expand=True, side='right', pady=10) # 오른쪽프레임
    
    global savefile_path_label, savefile_name_edit_entry
    savefile_path_label = Label(work_progress_right_labelframe, text='', bg=bg, fg='white')
    savefile_path_label.grid(row=0, column=0, padx=5, pady=3, columnspan=5, sticky=W) # 저장경로
    
    savefile_path_select_btn = Button(work_progress_right_labelframe, width=8, bg=bnbg, text='...', relief='flat', fg='white', command=get_final_aimodel_path)
    savefile_path_select_btn.grid(row=0, column=5, padx=3, pady=2)
    
    savefile_name_edit_entry = Entry(work_progress_right_labelframe, width = 30)
    savefile_name_edit_entry.grid(row=1, column=0, padx=5, pady=3, columnspan=6, sticky='NEWS') # 저장파일이름

    # 최근결과물
    beforefile_labelframe = LabelFrame(main_right_labelframe, bg=bg, text='최근결과물', relief='groove',
                            width=500, height=20, font=mainfont2, fg='white')
    beforefile_labelframe.pack(fill='both', expand=True) # DB 작업 이후에 만들 것(DB에서 데이터 가져와야함)
    
    global beforefile_img_frame
    beforefile_img_frame = Frame(beforefile_labelframe, bg=bg, width=150, height=550)
    beforefile_img_frame.pack(side='left', expand=True)

    beforefile_text_frame = Frame(beforefile_labelframe, bg=bg, width=300, height=550)
    beforefile_text_frame.pack(side='right', expand=True)


    global beforefile_img_label_1, beforefile_img_label_2, beforefile_img_label_3, beforefile_img_label_4
    # 최근 이미지 파일
    beforefile_img_data_photoimage = PhotoImage(file='./save/1.png', master=beforefile_img_frame)
    beforefile_img_label_1 = Label(beforefile_img_frame, bg=bg, pady=50, padx=60, image=beforefile_img_data_photoimage)
    beforefile_img_label_1.image = beforefile_img_data_photoimage
    beforefile_img_label_1.grid(row=0, column=0)
    Label(beforefile_img_frame, bg=bg, pady=3).grid(row=1)
    
    beforefile_img_data_photoimage = PhotoImage(file='./save/2.png', master=beforefile_img_frame)
    beforefile_img_label_2 = Label(beforefile_img_frame, bg=bg, pady=50, padx=60, image=beforefile_img_data_photoimage)
    beforefile_img_label_2.image = beforefile_img_data_photoimage 
    beforefile_img_label_2.grid(row=2, column=0)
    Label(beforefile_img_frame, bg=bg, pady=3).grid(row=3)
    
    
    beforefile_img_data_photoimage = PhotoImage(file='./save/3.png', master=beforefile_img_frame)
    beforefile_img_label_3 = Label(beforefile_img_frame, bg=bg, pady=50, padx=60, image=beforefile_img_data_photoimage)
    beforefile_img_label_3.image = beforefile_img_data_photoimage
    beforefile_img_label_3.grid(row=4, column=0)
    Label(beforefile_img_frame, bg=bg, pady=3).grid(row=5)
    
    
    beforefile_img_data_photoimage = PhotoImage(file='./save/4.png', master=beforefile_img_frame)
    beforefile_img_label_4 = Label(beforefile_img_frame, bg=bg, pady=50, padx=60, image=beforefile_img_data_photoimage)
    beforefile_img_label_4.image = beforefile_img_data_photoimage
    beforefile_img_label_4.grid(row=6, column=0)


    global beforefile_path_label_1, beforefile_path_label_2, beforefile_path_label_3, beforefile_path_label_4
    global beforefile_time_label_1, beforefile_time_label_2, beforefile_time_label_3, beforefile_time_label_4

    # 최근 저장경로 및 파일 이름 // 저장 날짜
    beforefile_path_dir = os.getcwd()
    beforefile_path = './save/video/'
    beforefile_path_listdir = os.listdir(beforefile_path)
    
    beforefile_path_label_1 = Label(beforefile_text_frame, bg=bg, pady=13, padx=5, fg=fg,
                        text=fr'{beforefile_path_dir}\save\video\{beforefile_path_listdir[0]}.mp4')
    beforefile_path_label_1.grid(row=1, column=0, sticky='nw')
    beforefile_time_label_1 = Label(beforefile_text_frame, bg=bg, pady=15, padx=5, fg=fg,
                        text=f'{datetime.datetime.fromtimestamp(os.path.getmtime(beforefile_path+beforefile_path_listdir[0]))}')
    beforefile_time_label_1.grid(row=2, column=0, sticky='nw')    
    Label(beforefile_text_frame, bg=bg, pady=2, padx=180).grid(row=3)
    
    
    beforefile_path_label_2 = Label(beforefile_text_frame, bg=bg, pady=13, padx=5, fg=fg,
                        text=fr'{beforefile_path_dir}\save\video\{beforefile_path_listdir[1]}.mp4')
    beforefile_path_label_2.grid(row=4, column=0, sticky='nw')
    beforefile_time_label_2 = Label(beforefile_text_frame, bg=bg, pady=15, padx=5, fg=fg,
                        text=f'{datetime.datetime.fromtimestamp(os.path.getmtime(beforefile_path+beforefile_path_listdir[1]))}')
    beforefile_time_label_2.grid(row=5, column=0, sticky='nw')
    Label(beforefile_text_frame, bg=bg, pady=3).grid(row=6)
    
    
    beforefile_path_label_3 = Label(beforefile_text_frame, bg=bg, pady=13, padx=5, fg=fg, 
                        text=fr'{beforefile_path_dir}\save\video\{beforefile_path_listdir[2]}.mp4')
    beforefile_path_label_3.grid(row=7, column=0, sticky='nw')
    beforefile_time_label_3 = Label(beforefile_text_frame, bg=bg, pady=15, padx=5, fg=fg,
                        text=f'{datetime.datetime.fromtimestamp(os.path.getmtime(beforefile_path+beforefile_path_listdir[2]))}')
    beforefile_time_label_3.grid(row=8, column=0, sticky='nw')
    Label(beforefile_text_frame, bg=bg, pady=2).grid(row=9)
    
    
    beforefile_path_label_4 = Label(beforefile_text_frame, bg=bg, pady=13, padx=5, fg=fg,
                        text=fr'{beforefile_path_dir}\save\video\{beforefile_path_listdir[3]}.mp4')
    beforefile_path_label_4.grid(row=10, column=0, sticky='nw')
    beforefile_time_label_4 = Label(beforefile_text_frame, bg=bg, pady=15, padx=5, fg=fg,
                        text=f'{datetime.datetime.fromtimestamp(os.path.getmtime(beforefile_path+beforefile_path_listdir[3]))}')
    beforefile_time_label_4.grid(row=11, column=0, sticky='nw')


    tk_window.resizable(False, False)