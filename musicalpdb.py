import pdb
import sys
import simpleaudio as sa
import wave
import time


class infinite_array():
    def __init__(self,inp):
        self.standard_input = inp

    def pop(self,*args):
        return self.standard_input
    def append(self,*args):
        return None


class myPdb(pdb.Pdb):
    play_obj = None

    def inpWav(self, wav_path, length_of_partition):
        """
        :wav_path: TODO
        :length_of_partition: TODO
        :returns: TODO

        """
        self.data = {}
        wave_read = wave.open(wav_path, 'rb')
        self.num_channels = wave_read.getnchannels()
        self.bytes_per_sample = wave_read.getsampwidth()
        self.sample_rate = wave_read.getframerate()
        no_frames = wave_read.getnframes()
        self.no_partitions = no_frames//length_of_partition

        for i in range(self.no_partitions):
            self.data[i] = wave_read.readframes(length_of_partition)

    def precmd(self,line):
        line_no = self.curframe.f_lineno
        if self.play_obj:
            self.play_obj.wait_done()
        self.play_obj = sa.play_buffer(self.data[line_no%self.no_partitions], self.num_channels, self.bytes_per_sample, self.sample_rate)
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

def my_set_trace(*, wav_path='music/alex-skrindo-miza-thinkin.wav', length_of_partition=80000, header=None):
    mypdb = myPdb(skip = ['musicalpdb','importlib*'])

    mypdb.inpWav(wav_path, length_of_partition)

    if header is not None:
        mypdb.message(header)
    mypdb.set_trace(sys._getframe().f_back)
