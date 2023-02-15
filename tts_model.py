from threading import *
import os, re, subprocess, glob
from num2words import num2words as nws
import soundfile as sf
import numpy as np


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


def text_edit(model, text):
    try:
        text_result_list = []
        tts_model_execution_list = []
        txt_file = text

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
        

        # 단일화자
        # if model_sel == 'ai_h':
        #     models = 'model_1'
        # elif model_sel == 'ai_c':
        #     models = 'model_2'
        model_sel = model
        # 다중화자
        if model_sel == 'ai_h':
            models = '1'
        elif model_sel == 'ai_c':
            models = '0'
        print(model_sel) # 선택한 모델 확인
        
        tts_create_cnt = 1 # 진행률 표시용
        for i in tts_model_execution_list:
            # 단일화자
            # cmd = f'python audio_create/synthesizer.py --load_path audio_create/model/{models} --sample_path sample --text "{i}"'
            # 다중화자
            cmd = f'python audio_create/synthesizer.py --load_path audio_create/model/1and2 --num_speaker 2 --speaker_id {models} --sample_path sample --text "{i}"'
            
            subprocess.run(cmd)
            
            print(f'{i} - 오디오 생성 진행중')
            
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

        default_name = 'voice'
        
        sf.write(f'./TTSOUT/audio/{default_name}.wav', audio_list, sample_rate)

        # -- 생성된 파일 삭제 --
        [os.remove(f) for f in glob.glob('./TTSOUT/*.wav')]
        [os.remove(f) for f in glob.glob('./sample/*.wav')]
        print("오디오 생성완료")
        
        # 다음 프로세스를 위해 초기화
        txt_file = ''
        tts_model_execution_list = []
    except:

        [os.remove(f) for f in glob.glob('./TTSOUT/*.wav')]
        [os.remove(f) for f in glob.glob('./sample/*.wav')]

if __name__ == '__name__':
    text_edit()