import moviepy.editor as mp
import os
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        #return help
        print("Please specify filename(s) to convert")
        exit(0)
    else: 
        for f in sys.argv[1:]:
            clip = mp.VideoFileClip((f))
            clip.write_videofile(os.path.splitext(f)[0]+'.mp4')
    