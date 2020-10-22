from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
from pydub.playback import play
import soundfile
alist=["2.wav", "3.wav", "4.wav", "5.wav", "6.wav", "7.wav", "8.wav", "9.wav", "10.wav", "11.wav", "12.wav"]
playlist=["wav_file_1", "wav_file_2", "wav_file_3", "wav_file_4", "wav_file_5", "wav_file_6", "wav_file_7", "wav_file_8", "wav_file_9", "wav_file_10", "wav_file_11", "wav_file_12"]
def get_higher_pitch(filename, outfile):
    sound = AudioSegment.from_file(filename, format="wav") # shift the pitch up by half an octave (speed will increase proportionally)
    octaves = 0.5
    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    # keep the same samples but they ought to be played at the new, higher sample rate. This file sounds like a chipmunk but has a weird sample rate.
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    #convert it to a common sample rate (44.1k - standard audio CD) to make sure it works in regular audio players
    hipitch_sound = hipitch_sound.set_frame_rate(44100)
    #export / save pitch changed sound
    hipitch_sound.export(outfile, format="wav")
get_higher_pitch("1.wav", "2.wav") 
for i in range (len(alist) - 1):
    get_higher_pitch(alist[i], alist[i+1])

wav_file_1 = AudioSegment.from_file("1.wav")
wav_file_2 = AudioSegment.from_file("2.wav") 
wav_file_3 =  AudioSegment.from_file("3.wav")
wav_file_4 =  AudioSegment.from_file("4.wav")
wav_file_5 =  AudioSegment.from_file("5.wav")
wav_file_6 =  AudioSegment.from_file("6.wav")
wav_file_7 =  AudioSegment.from_file("7.wav")
wav_file_8 =  AudioSegment.from_file("8.wav")
wav_file_9 =  AudioSegment.from_file("9.wav")
wav_file_10 =  AudioSegment.from_file("10.wav")
wav_file_11 =  AudioSegment.from_file("11.wav")
wav_file_12 =  AudioSegment.from_file("12.wav")

wav_file_13 = wav_file_1+wav_file_2+wav_file_3+wav_file_4+wav_file_5+wav_file_6+wav_file_7+wav_file_8+wav_file_9+wav_file_10+wav_file_11+wav_file_12
wav_file_13.export("continuous.wav", format="wav")    
    