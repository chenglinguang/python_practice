#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename=fiename

class MP3File(AudioFile):
    exit="mp3"
    def play(self):
        print("playing {} as map3".format(self.filename))

class WavFile(AudioFile):
    exit="wav"
    def play(self):
        print("playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    exit="ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename))


