# AINEWROOM
### Tacotron2 모델과 wav2lip 모델을 결합하여 AI 아나운서를 만드는 tkiner 기반 GUI 프로그램 입니다.

![image](https://user-images.githubusercontent.com/92764800/218385808-da3fa78a-ce24-4374-afad-0c6bfd41ae72.png)

개발 환경
---
 - windows 10
 - anaconda
 - python 3.7
 - tensorflow 1.x
```sh
pip install requirements.txt
```
 

## 사용 예제

### 1. TTS
![image](https://user-images.githubusercontent.com/92764800/218385825-aafd53b1-eda1-4834-ad4b-0858e131c59e.png)

- Text to Speech 모델 학습 및 구현은 [carpedm20](https://github.com/carpedm20/multi-speaker-tacotron-tensorflow) 참고
- 생성한 data 파일 추가
- 본 프로그램은 multi-speaker 사용 (다중화자)
```sh
../audio_create/model/(you_file)
```
```sh
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
```
### 대본 불러오기
- 수정할 .text 파일을 "대본입력" 프레임에 불러온다.
### 대본 저장하기
- "대본입력" 프레임의 Text 정보를 .text 형태로 저장한다.
### 음성생성
- 생성할 .text 파일을 선택하고 모델을 실행한다.
- 생성된 wav 파일은 text의 단락마다 1초의 간격을 두고 합쳐진다.
- 최종적으로 생성된 wav 파일은 "./TTSOUT/audio" 에 저장된다.
```sh
tts_model.py

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
```
### 강제종료
- 생성중인 모델을 강제로 종료한다.
---
### 2. TTS+LipFake
![image](https://user-images.githubusercontent.com/92764800/218385838-94c4aeec-bc29-4388-bc8e-ea3e068a9b8f.png)
### 동영상 프레임 - 파일업로드
- lipfake를 진행할 영상을 선택한다.
- 입을 움직이지 않는 영상이 가장 자연스러운 결과를 가져온다.
- 영상의 길이보다 오디오의 길이가 길다면 실행되지 않는다. & Tip. FFmpeg로 영상 조정

### 오디오 프레임 - 파일업로드
- lipfake에 사용될 오디오 파일을 선택한다.

### 작업진행 프레임 - 합성시작
- 저장경로를 선택하고 이름을 기입한다.
- 모델이 실행되며 결과물을 .mp4 파일로 저장시킨다.

### 최근결과물
- 최근에 작업한 결과물을 4개까지 저장한다.
```sh
./save/video
```


라이센스 인용
---
- https://github.com/hccho2/Tacotron2-Wavenet-Korean-TTS
- https://github.com/hccho2/Tacotron-Wavenet-Vocoder

- https://github.com/Rudrabha/Wav2Lip
```sh
@inproceedings{10.1145/3394171.3413532,
author = {Prajwal, K R and Mukhopadhyay, Rudrabha and Namboodiri, Vinay P. and Jawahar, C.V.},
title = {A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild},
year = {2020},
isbn = {9781450379885},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3394171.3413532},
doi = {10.1145/3394171.3413532},
booktitle = {Proceedings of the 28th ACM International Conference on Multimedia},
pages = {484–492},
numpages = {9},
keywords = {lip sync, talking face generation, video generation},
location = {Seattle, WA, USA},
series = {MM '20}
}
```
