
from flask import Flask, render_template, request, send_file, url_for, redirect, session
import pymysql , os
from tts_model import *
from ai_human import *


app = Flask(__name__)
# app.secret_key = (secret_key)

try:
    db = pymysql.connect(host = "you host",
                        port = "you port",
                        user = "you user",
                        password = "you pw",
                        db = "you db name")
except Exception as e:
    print("DB ERROR")

cur = db.cursor(pymysql.cursors.DictCursor)

# -- 시작 페이지 (로그인) --
@app.route("/")
def signin():
    session.clear()
    return render_template('signin.html')

# -- 로그인 페이지 --
@app.route("/login", methods = ['POST'])
def login():
    Login_id = request.form['id']
    Login_pw = request.form['pw']
    
    sql = f"SELECT * FROM user WHERE user_id = '{Login_id}' AND user_pw = '{Login_pw}'"
    
    cur.execute(sql)
    select_login = cur.fetchone()
    db.commit()
    
    print(Login_id, Login_pw, select_login)
    session['id'] = request.form['id']
    
    if select_login == None:
        return "0"
    elif select_login['user_id'] == Login_id and select_login['user_pw'] == Login_pw:
        return "1"

    return render_template('signin.html')


# -- 메인페이지 (TTS) --
@app.route("/main")
def index():
    return render_template('index.html')


# -- TTS 모델 작동 페이지 --
@app.route("/down", methods=['GET', 'POST'])
def tts():
    if request.method == 'POST':
        print("파일 개수 :", path_listdir)
        
        model = request.form['model']
        textbox = request.form['textbox']
        print(model, textbox)
        
        try:
            path_dir = './TTSOUT/audio/'
            path_listdir = os.listdir(path_dir)
            [os.remove(f) for f in glob.glob('./TTSOUT/audio/*.wav')]  
            
            if len(path_listdir) == 0:
                print('생성시작')
                    
                if model == "모델 선택":
                    print("model error")
                else:
                    text_list = textbox.split('\r\n')
                    print(type(text_list), text_list)
                    text_edit(model, text_list)
                    
                    return render_template('download.html')

            else:
                print('대본없음')
                return redirect(url_for('index'))
            
        except:
            print('except')
            return redirect(url_for('index'))
        
    return redirect(url_for('index'))
        

# -- TTS 파일 다운로드 링크페이지 --
@app.route("/downlink")
def downlink():

        print('file 다운시작')
        return send_file('./TTSOUT/audio/voice.wav',
                mimetype='audio/wav',
                as_attachment=True,
                attachment_filename="tts.wav")
    

# -- TTS + LipFake 페이지 --
@app.route("/video", methods=['GET', 'POST'])
def video():
    return render_template('video.html')


# -- TTS + LipFake 모델 작동 페이지 --
@app.route("/fake", methods=['GET', 'POST'])
def fake():
    try:
        [os.remove(f) for f in glob.glob('./static/video/*.mp4')]
        [os.remove(f) for f in glob.glob('./static/audio/*.wav')]
        [os.remove(f) for f in glob.glob('./static/lipfake/*.mp4')]
        
        video_file = request.files["video_file"]
        audio_file = request.files["audio_file"]
        
        video_file.save("static/video/video.mp4")
        audio_file.save("static/audio/audio.wav")
        
        video_file_path = "static/video/video.mp4"
        audio_file_path = "static/audio/audio.wav"
        
        print(video_file, audio_file)
        
        start_tts(video_file_path, audio_file_path)
        return render_template('fake_download.html')
    except:
        return redirect(url_for('video'))


# -- TTS + LipFake 파일 다운로드 페이지 --
@app.route("/fake_downlink")
def fake_downlink():

        print('file 다운시작')
        return send_file('./static/lipfake/fake.mp4',
                mimetype='video/mp4',
                as_attachment=True,
                attachment_filename="fake.mp4")
        
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)