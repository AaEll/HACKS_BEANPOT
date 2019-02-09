import pdb
import sys
import simpleaudio as sa
import wave
import time



data ={}
wav_path = 'C:\\Users\\musicalpdb\\resources\\music\\44mozarts15b.wav'#44mozarts15b.wav' #NWA.wav
wave_read = wave.open(wav_path, 'rb')
num_channels = wave_read.getnchannels()
bytes_per_sample = wave_read.getsampwidth()
sample_rate = wave_read.getframerate()
no_frames = wave_read.getnframes()
no_partitions = no_frames//70000
for i in range(no_partitions):
	data[i] = wave_read.readframes(70000)

class infinite_array():
    def __init__(self,inp):
        self.standard_input = inp

    def pop(self,*args):
        return self.standard_input
    def append(self,*args):
        return None


class myPdb(pdb.Pdb):
    play_obj = None

    def precmd(self,line):
        line_no = self.curframe.f_lineno
        if self.play_obj:
            self.play_obj.wait_done()
        self.play_obj = sa.play_buffer(data[line_no%no_partitions], num_channels, bytes_per_sample, sample_rate)
        return line

    def postcmd(self, stop, line):
        #self.play_obj.wait_done()
        return stop

    def _cmdloop(self):
        while True:
            try:
                # keyboard interrupts allow for an easy way to cancel
                # the current command, so allow them during interactive input
                self.allow_kbdint = True
                self.cmdloop()
                self.allow_kbdint = False
                break
            except KeyboardInterrupt:
                self.message('--KeyboardInterrupt--')
    def do_play2(self, line):
        self.cmdqueue  = infinite_array('n\r\n')
    def do_play(self, line):
        self.cmdqueue  = infinite_array('s\r\n')



def my_set_trace(*, header=None):
    mypdb = myPdb(skip = ['musicalpdb','importlib*'])
    if header is not None:
        mypdb.message(header)
    mypdb.set_trace(sys._getframe().f_back)
my_set_trace()
