# =================import library====================

# https://pypi.org/project/SpeechRecognition/

import speech_recognition as sr #pip install SpeechRecognition in advance
import glob,os,re
r = sr.Recognizer()

# *caution* speech recognition has file limitation: 10mb per 1 API process
# *caution* speech recognition works with only wav file(almost)/ cannot work with mp3,m4a etc..

# ================= 0. preprocessing of recognition ====================
# =======read WAV file
wav_path_glob = os.path.join("localpath/*.wav") 
wav_paths = sorted(glob.glob(wav_path_glob))    


# # OPTION ========normalize wav file dbfs for quality
from pydub import AudioSegment
norm_dir="localpath"

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

for i,file in enumerate(wav_paths):
    a=re.split("[./]",file)[-2].replace("\\","/")
    b=re.split("[./]",a)[-1]
    c=norm_dir+"/"+b+".wav"
    sound = AudioSegment.from_file(file, "wav")
    normalized_sound = match_target_amplitude(sound, -20.0)
    normalized_sound.export(c, format="wav")



# ========analyze wav file size 
print("checking file size...")
for i,file in enumerate(wav_paths):
    size = int(os.stat(file).st_size/1000000)
    print("file size:", size, "mb")


# =======if size is over 10mb, split WAV file because of size limitation
# =======export each splitted file

from pydub import AudioSegment
from pydub.utils import make_chunks
import math

for i,file in enumerate(wav_paths):
	# for export, make new directory
    a=re.split("[./]",file.replace("\\","/"))
    b="/".join(a[:-1])
    os.mkdir(b)     
    
    myaudio = AudioSegment.from_file(file , "wav")
    channel_count = myaudio.channels    #Get channels
    sample_width = myaudio.sample_width #Get sample width
    duration_in_sec = len(myaudio) / 1000 #Length of audio in sec
    sample_rate = myaudio.frame_rate

    wav_file_size=os.stat(file).st_size
    file_split_size = 10000000  # 10Mb OR 10, 000, 000 bytes
    total_chunks =  wav_file_size // file_split_size
    chunk_length_in_sec = math.ceil((duration_in_sec * 10000000 ) /wav_file_size)   #in sec
    chunk_length_ms = chunk_length_in_sec * 1000
    chunks = make_chunks(myaudio, chunk_length_ms)
    for j, chunk in enumerate(chunks):
        out_file=os.path.join(b,"%s.wav"%j)
        print ("out_file", chunk)
        chunk.export(out_file, format="wav")


# ================= 1. start to recognition ====================

# =======read splited WAV file
wavS_path_glob = os.path.join("localpath/split/*.wav") 
wavS_paths = sorted(glob.glob(wavS_path_glob))    

# =======convert each audio files to one txt file

linet=[]
for i,file in enumerate(wavS_paths):
    read=sr.AudioFile(file)
    with read as source:
    	audio = r.record(source)
        text = r.recognize_google(audio,language="ja-JP") # because audio file is japanese
        line=re.findall('.*?[。]', text)
        linet.extend(line)

result_file="localpath/result.txt"
print(linet, file=open(result_file,'w'))
