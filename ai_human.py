import subprocess

# -- TTS + LipFake Start --
def start_tts(video, audio):
    video_file_path = video
    audio_file_path = audio
    outfile_path = "./static/lipfake/fake"
    cmd = f'python lipfake/inference.py --checkpoint_path ./checkpoints/wav2lip_gan.pth --face {video_file_path} --audio {audio_file_path} --outfile {outfile_path}.mp4 --resize_factor 2'
    print(cmd)
    subprocess.run(cmd)
    
    print("fake file 생성완료")
if __name__ == '__name__':
    start_tts()