#!/usr/bin/env python
# coding: utf-8

from threading import *
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os, re, subprocess, glob
from num2words import num2words as nws
import soundfile as sf
import numpy as np

# -- 설정 --
bg = '#2c3e50'
bnbg = '#2f3640'


# -- 숫자 -> 한글 변환 --
def num_kr_translator(number):
    number_retrun = []
    run_app = []
    
    if re.findall("\d+", number) != []:
        number_list = re.findall("\d+", number)
        
        for i in number_list:
            run_join = ''.join(i)
            run_app.append(int(run_join))
            run_sorted = sorted(run_app, reverse=True)
        
        for i in range(len(number_list)):
            number_retrun.append(nws(run_sorted[i], lang='ko'))
            number = number.replace(str(run_sorted[i]), number_retrun[i])
    return number


# -- 텍스트 활성화 --
def get_text_input(): # input_text 가져올 함수
    result = tts_text_input_text.get("1.0","end")
    print(result)# 텍스트 확인용
    
# -- 텍스트 불러오기 --
def get_load_text():
    try:
        try:
            file = filedialog.askopenfilename(initialdir='/', title='Select file', defaultextension='.txt',
                                        filetypes=(("text files", "*.txt"),("all files", "*.*")))
            f = open(file, 'rt', encoding='cp949')
            tts_text_input_text.delete('1.0', END)
            tts_text_input_text.insert(END,f.read())
            loding_label.config(text = '텍스트 불러오기 성공')
        except:
            f = open(file, 'rt', encoding='utf-8')
            tts_text_input_text.delete('1.0', END)
            tts_text_input_text.insert(END,f.read())
            loding_label.config(text = '텍스트 불러오기 성공')         
    except:
        loding_label.config(text = '텍스트 불러오기 에러')
   

# -- 텍스트 저장 --
def save_text():
    try:
        file = filedialog.asksaveasfile(title= 'file save', mode='w', defaultextension=".txt",
                                        filetypes=(("text files", "*.txt"),("all files", "*.*")))
        if file != None:
            lines = tts_text_input_text.get('1.0', 'end')
            file.write(lines)
            file.close()
            loding_label.config(text = '텍스트 저장 성공')
    except:
        messagebox.showinfo('에러', '에러')


# -- Thread --
def therading_text_edit():
    try:
        therad = Thread(target = text_edit)
        therad.daemon = True
        therad.start()
    except:
        print(f'Thread error : {therad}')


# -- TTS 모델 사용 --
def text_edit():
    try:
        text_result_list = []
        tts_model_execution_list = []
        
        file = filedialog.askopenfilename(initialdir='/', title='Select file', defaultextension='.txt',
                                    filetypes=(("text files", "*.txt"),("all files", "*.*")))
        
        try:
            f = open(file, 'r', encoding='cp949')
            txt_file = f.readlines()
            print('cp949')
        except:
            f = open(file, 'r', encoding='utf-8')
            txt_file = f.readlines()
            print('utf-8')
            
        loding_label.config(text = '음성 생성 시작')

        for i in range(len(txt_file)):
            sentence_break = (txt_file[i])
            text_process = sentence_break
        
            if text_process[0] == ' ': # 문자열 start 공백 제거
                text_process = text_process[1:]
                
            if '  ' in text_process:
                text_process = text_process.replace('  ',' ')
            
            # 가공
            text_process = text_process.replace('코로나19','코로나일구')
            text_process = text_process.replace('kg','킬로그램')
            text_process = text_process.replace('cm','센티미터')
            text_process = text_process.replace('km','킬로미터')
            text_process = text_process.replace('mm','밀리미터')
            text_process = text_process.replace('%', '퍼센트')
            text_process = text_process.replace('·', ' ')
            text_process = text_process.replace('“','')
            text_process = text_process.replace('”','')
            text_process = text_process.replace('. ',' ')
            text_process = text_process.replace('.','쩜')
            text_process = text_process.replace('"','')
            text_process = text_process.replace('  ',' ')
            text_process = text_process.strip('\n')
            text_process = text_process.strip('\t')

            text_process = text_process.replace('A', '에이')
            text_process = text_process.replace('B', '비')
            text_process = text_process.replace('C', '씨')
            text_process = text_process.replace('D', '디')
            text_process = text_process.replace('E', '이')
            text_process = text_process.replace('F', '에프')
            text_process = text_process.replace('G', '지')
            text_process = text_process.replace('H', '에이치')
            text_process = text_process.replace('I', '아이')
            text_process = text_process.replace('J', '제이')
            text_process = text_process.replace('K', '케이')
            text_process = text_process.replace('L', '앨')
            text_process = text_process.replace('M', '엠')
            text_process = text_process.replace('N', '엔')
            text_process = text_process.replace('O', '오')
            text_process = text_process.replace('P', '피')
            text_process = text_process.replace('Q', '큐')
            text_process = text_process.replace('R', '알')
            text_process = text_process.replace('S', '에스')
            text_process = text_process.replace('T', '티')
            text_process = text_process.replace('U', '유')
            text_process = text_process.replace('V', '브이')
            text_process = text_process.replace('W', '더블유')
            text_process = text_process.replace('X', '엑스')
            text_process = text_process.replace('Y', '와이')
            text_process = text_process.replace('Z', '제트')
            
            text_process = text_process.replace('a', '에이')
            text_process = text_process.replace('b', '비')
            text_process = text_process.replace('c', '씨')
            text_process = text_process.replace('d', '디')
            text_process = text_process.replace('e', '이')
            text_process = text_process.replace('f', '에프')
            text_process = text_process.replace('g', '지')
            text_process = text_process.replace('h', '에이치')
            text_process = text_process.replace('i', '아이')
            text_process = text_process.replace('j', '제이')
            text_process = text_process.replace('k', '케이')
            text_process = text_process.replace('l', '앨')
            text_process = text_process.replace('m', '엠')
            text_process = text_process.replace('n', '엔')
            text_process = text_process.replace('o', '오')
            text_process = text_process.replace('p', '피')
            text_process = text_process.replace('q', '큐')
            text_process = text_process.replace('r', '알')
            text_process = text_process.replace('s', '에스')
            text_process = text_process.replace('t', '티')
            text_process = text_process.replace('u', '유')
            text_process = text_process.replace('v', '브이')
            text_process = text_process.replace('w', '더블유')
            text_process = text_process.replace('x', '엑스')
            text_process = text_process.replace('y', '와이')
            text_process = text_process.replace('z', '제트')
            
            text_process = text_process.replace('게임', '께임')
            text_process = text_process.replace('5G', '파이브지')
            text_process = text_process.replace('5g', '파이브지')
            
            text_process = text_process.replace('석유', '서규')
            
            if text_process[-1:] == ' ':
                text_process = text_process[:-1]
            
            if text_process[0] == ' ':
                text_process = text_process[1:]
                
            if text_process[-1:] == '쩜':
                text_process = text_process[:-1]
                
            text_result_list.append(text_process[:])       
                
        for i in text_result_list: # 숫자 -> 한글 변환 실행
            tts_model_execution_list.append(num_kr_translator(i))
        
        
        model_select = model_select_cbbox.get()

        # 단일화자
        # if model_sel == 'AI_황이화':
        #     models = 'model_1'
        # elif model_sel == 'AI_추민선':
        #     models = 'model_2'

        # 다중화자
        if model_select == 'AI_황이화':
            models = '1'
        elif model_select == 'AI_추민선':
            models = '0'
        print(model_select) # 선택한 모델 확인
        
        tts_create_cnt = 1 # 진행률 표시용
        for i in tts_model_execution_list:
            # 단일화자
            # cmd = f'python audio_create/synthesizer.py --load_path audio_create/model/{models} --sample_path sample --text "{i}"'
            # 다중화자
            cmd = f'python audio_create/synthesizer.py --load_path audio_create/model/1and2 --num_speaker 2 --speaker_id {models} --sample_path sample --text "{i}"'
            
            subprocess.run(cmd)
            
            print(f'{i} - 오디오 생성 진행중')
            cnt = (tts_create_cnt/len(tts_model_execution_list))*100
            loding_label.config(text = f'진행률 - {int(cnt)}%')         
            tts_create_cnt += 1
            
        print('파일 이름 변경 시작')
        sample_path = glob.glob('./sample/**', recursive=True)

        exts = ('png', 'jpg', 'txt', 'mp4') # 폴더에 해당 확장자 파일 삭제
        for i in sample_path:
            if any(ext in i for ext in exts):
                os.remove(i)


        aduio_sample_path = "./sample" # 오디오 파일 저장 경로
        file_names = os.listdir(aduio_sample_path)
        file_names

        str_cnt = 1
        for name in file_names:
            src = os.path.join(aduio_sample_path, name)
            dst = str(str_cnt) + '.wav'
            dst = os.path.join(aduio_sample_path, dst)
            os.rename(src, dst)
            str_cnt += 1

        # ------------------------ 개별 생성시 여기서부터 주석 -------------------------        
        # -- 오디오 생성 부 --
        audio_list = [] # 합칠 오디오 파일 리스트
        sample_rate = 24000
        filecnt = os.listdir('./sample/')

        # -- 파일마다 1초의 간격 추가 --
        for i in range(len(filecnt)):
            x, sr = sf.read(f'./sample/{i+1}.wav')
            y, sr = sf.read(f'./TTSOUT/1sec/1sec.wav')
            x = np.concatenate((x,y),axis=0)
            sf.write(f'./TTSOUT/audio_{i+1}.wav', x, sample_rate)

        # -- 전체 오디오 결합 --    
        for i in range(len(filecnt)):
            cnt, sr = sf.read(f'./TTSOUT/audio_{i+1}.wav')
            audio_list.append(cnt)

        audio_list = np.concatenate((audio_list), axis=0)
        
        name = file_name_input_text.get('1.0', 'end-1c')
        print(name)
        
        sf.write(f'./TTSOUT/audio/{name}.wav', audio_list, sample_rate)

        # -- 생성된 파일 삭제 --
        [os.remove(f) for f in glob.glob('./TTSOUT/*.wav')]
        [os.remove(f) for f in glob.glob('./sample/*.wav')]
        
        print("오디오 생성완료")
        loding_label.config(text = '음성 생성 완료')
        
        # 다음 프로세스를 위해 초기화
        txt_file = ''
        tts_model_execution_list = []
        f.close()
    except:
        messagebox.showinfo('에러', '에러')
        loding_label.config(text = '음성 생성')
        [os.remove(f) for f in glob.glob('./TTSOUT/*.wav')]
        [os.remove(f) for f in glob.glob('./sample/*.wav')]
        f.close()

    # ----------------------------------------------------------------------

# -- tkinter tts program --
def tk_tts_program(win, mainfont2, mainfont, k_font, text_font):
    global loding_label, file_name_input_text, tts_text_input_text
    
    tts_program_window = Toplevel(win)
    tts_program_window.geometry('800x630')
    tts_program_window['bg'] = bg

    text_fg = 'white'
    btn_fg = 'white'

    Label(tts_program_window, bg=bg, text='     ').pack(side='left') # 사각 패딩
    Label(tts_program_window, bg=bg, text='     ').pack(side='right')
    Label(tts_program_window, bg=bg, text='     ').pack(side='top')
    Label(tts_program_window, bg=bg, text='     ').pack(side='bottom')

    # -- 메인프레임 --
    main_labelframe = LabelFrame(tts_program_window, bg=bg, text='Text To Speech', fg=text_fg, font=mainfont, pady=15)
    main_labelframe.pack(fill='both', expand=True)


    main_info_frame = Frame(main_labelframe, bg=text_fg, width=600, height=180)
    main_info_frame.pack(expand=False, side='top')

    file_info_labelframe = LabelFrame(main_info_frame, bg=bg, text='모델선택', fg=text_fg, font=mainfont2, width=300, height=180, pady=35, padx=30)
    file_info_labelframe.pack(fill='both', expand=True, side='left')

    text_info_labelframe = LabelFrame(main_info_frame, bg=bg, text='대본입력', fg=text_fg, font=mainfont2, width=400, height=300, pady=35, padx=50)
    text_info_labelframe.pack(fill='both', expand=False, side='right')

    Label(file_info_labelframe, text='모델선택   ', bg=bg, fg='white').grid(column=0, row=0)
    Label(file_info_labelframe, text='파일이름   ', bg=bg, fg='white').grid(column=0, row=1)
    
    file_name_input_text = Text(file_info_labelframe, width=23, height=1, font=k_font)
    file_name_input_text.insert(END , '파일 이름')
    file_name_input_text.grid(column=2, row=1)
    
    global model_select_cbbox
    model_select_cbbox = ttk.Combobox(file_info_labelframe)
    model_select_cbbox['values'] = ('AI_황이화','AI_추민선', 'AI 3(준비중)', 'AI 4(준비중)')
    model_select_cbbox.current(0)
    model_select_cbbox.grid(column=2, row=0)
    
    # -- 참고사항 --
    Label(file_info_labelframe, text='', bg=bg, fg=text_fg).grid(column=0, row=2) # 여백용
    Label(file_info_labelframe, text=' * 사용 규칙 *', bg=bg, fg=text_fg, font=text_font).grid(columnspan=5, row=3)
    Label(file_info_labelframe, text='1. 원하는 뉴스 대본 작성', bg=bg, fg=text_fg).grid(columnspan=5, row=4, sticky=W)
    Label(file_info_labelframe, text='2. 대본 저장하기 버튼 클릭', bg=bg, fg=text_fg).grid(columnspan=5, row=5, sticky=W)
    Label(file_info_labelframe, text='3. 대본 불러오기 버튼으로 대본 수정', bg=bg, fg=text_fg).grid(columnspan=5, row=6, sticky=W)
    Label(file_info_labelframe, text='4. 2번 3번 반복', bg=bg, fg=text_fg).grid(columnspan=5, row=7, sticky=W)
    Label(file_info_labelframe, text='5. 음성생성 버튼 클릭', bg=bg, fg=text_fg).grid(columnspan=5, row=8, sticky=W)
    Label(file_info_labelframe, text='6. 파일 이름 기입 후 대본파일 선택 시 TTS 음성 생성', bg=bg, fg=text_fg).grid(columnspan=5, row=9, sticky=W)
    Label(file_info_labelframe, text='', bg=bg, fg='white').grid(column=0, row=10)
    Label(file_info_labelframe, text='*   비정상적 에러시 관리자 문의', bg=bg, fg='red').grid(columnspan=5, row=12, sticky=W)

    tts_text_input_text = Text(text_info_labelframe)
    tts_text_input_text.insert(END, '대본을 입력하세요.')
    tts_text_input_text.place(width=300, height=260)


    # -- 버튼 프레임 --
    btn_frame = Frame(main_labelframe, bg=bg, width=695, height=50, pady=2)
    btn_frame.pack(expand=True, side='bottom')

    loding_label = Label(btn_frame, text='현재 상태가 표시됩니다.', bg=bg, fg=text_fg)
    loding_label.grid(columnspan=10, row=0)

    Label(btn_frame, bg=bg, text='     ').grid(column=1, row=1) # 버튼 공백용
    load_textfile_btn = Button(btn_frame, bg=bnbg, text='대본 불러오기', fg=btn_fg, relief='flat', command=get_load_text, padx=30, pady=8)
    load_textfile_btn.grid(column=0, row=2)

    Label(btn_frame, bg=bg, text='     ').grid(column=1, row=2) # 버튼 공백용
    save_textfile_btn = Button(btn_frame, bg=bnbg, text='대본 저장하기', fg=btn_fg, relief='flat', command=save_text, padx=30, pady=8)
    save_textfile_btn.grid(column=2, row=2)

    Label(btn_frame, bg=bg, text='     ').grid(column=3, row=2) # 버튼 공백용
    tts_create_btn = Button(btn_frame, bg=bnbg, text='음성 생성', fg=btn_fg, relief='flat', command=therading_text_edit, padx=30, pady=8)
    tts_create_btn.grid(column=4, row=2)

    Label(btn_frame, bg=bg, text='     ').grid(column=5, row=2) # 버튼 공백용
    gui_stop_btn = Button(btn_frame, bg=bnbg, text='강제 종료', fg=btn_fg, relief='flat', command=tts_program_window.destroy, padx=30, pady=8)
    gui_stop_btn.grid(column=6, row=2)

    [os.remove(f) for f in glob.glob('./TTSOUT/*.wav')]
    [os.remove(f) for f in glob.glob('./sample/*.wav')]
    
    tts_program_window.resizable(False, False)
    tts_program_window.mainloop()