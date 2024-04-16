import array
import math
import time
import pyaudio

def cw(duration=0, volume=0):
    p = pyaudio.PyAudio()
    
    fs = 44100

    f = 440.0
    
    # Generate samples (convert to float32 array)
    num_samples = int(fs * duration)
    samples = [volume * math.sin(2 * math.pi * k * f / fs) for k in range(0, num_samples)]

    # Convert samples to bytes sequence
    output_bytes = array.array('f', samples).tobytes()

    # Open audio stream and play
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    start_time = time.time()
    stream.write(output_bytes)
    # print(f"Played sound for {time.time() - start_time:.2f} seconds")
    stream.stop_stream()
    stream.close()
    p.terminate()


def play(c, wpm):
    stan = 50
    if c == "A":
        cw(60 / wpm / stan, 0.5)
        cw(60 *3 / wpm / stan, 0.5)
    elif c == "B":
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5)   
    elif c == "C":
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
        cw(60 *3 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5)   
    elif c == "D":
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
    elif c == "E":
        cw(60 / wpm / stan, 0.5)
    elif c == "F":
        cw(60 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
        cw(60 * 3/ wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
    elif c == "G":
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
    elif c == "H":
        cw(60 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
    elif c == "I":
        cw(60 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
    elif c == "J":
        cw(60 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
    elif c == "K":
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
    elif c == "L":
        cw(60 / wpm / stan, 0.5)
        cw(60 * 3/ wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
    elif c == "M":
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
    elif c == "N":
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
    elif c == "O":
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
    elif c == "P":
        cw(60 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
    elif c == "Q":
        cw(60 * 3/ wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
    elif c == "R":
        cw(60 / wpm / stan, 0.5)
        cw(60 * 3 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
    elif c == "S":
        cw(60 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5)
        cw(60 / wpm / stan, 0.5) 
    elif c == "T":
        cw(60 * 3/ wpm / stan, 0.5)
    elif c == "U":
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5)  
        cw(60 * 3 / wpm / stan, 0.5)  
    elif c == "V":
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5)   
        cw(60 * 3 / wpm / stan, 0.5) 
    elif c == "W":
        cw(60 / wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5)    
    elif c == "X":
        cw(60 * 3/ wpm / stan, 0.5)   
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5)  
    elif c == "Y":
        cw(60 * 3/ wpm / stan, 0.5)   
        cw(60 / wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5)   
        cw(60 * 3/ wpm / stan, 0.5) 
    elif c == "Z":
        cw(60 * 3/ wpm / stan, 0.5)   
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5)   
        cw(60 / wpm / stan, 0.5) 
    elif c == "0":
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
    elif c == "1":
        cw(60 / wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
    elif c == "2":
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
    elif c == "3":
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
    elif c == "4":
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
    elif c == "5":
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
    elif c == "6":
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
    elif c == "7":
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
    elif c == "8":
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
    elif c == "9":
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
    elif c == "?":
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5)  
    elif c == "/":
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5) 
        cw(60 * 3/ wpm / stan, 0.5) 
        cw(60 / wpm / stan, 0.5)    
    elif c == " ":
        cw(60 * 2 / wpm / stan)

    cw(60 / wpm / stan)