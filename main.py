import signal, subprocess, sys, requests, subprocess

def signal_handler(sig, frame):
    try:
        subprocess.run(["taskkill", "/F", "/IM", "ffmpeg.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(f"Error while taskkilling ffmpeg.exe: {e}")
    finally:
        sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)

    try:
        filename = input("Filename: ")
        with open('stream_keys.txt','r') as keys:
            for key in keys:
                subprocess.Popen(f'ffmpeg -loglevel quiet -stream_loop -1 -re -i {filename} -stream_loop -1 -i music.mp3 -c:v libx264 -preset veryfast -b:v 3000k -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv "rtmp://live.twitch.tv/app/{key}"', shell=True)
                
    except Exception as e:
        print(f"An error occurred: {e}")
        signal_handler(signal.SIGINT, None) 

if __name__ == "__main__":
    main()