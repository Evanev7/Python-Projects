#imports external modules
import numpy, pylab
from scipy.io import wavfile

#define the constant PI
PI = numpy.pi

#sampling rate
rate = 44100
period = 1.0/rate

#number of seconds the sound file should last
duration = 5

#frequency of the analogue to be sampled
freq = 440

#max amplitude
amp = 2**15 - 1

#defines special "numpy arrays"
time = numpy.arange(duration*rate)*period
wave = amp*numpy.sin(2*PI*time*freq)

#creates a sound file
#second parameter is the sampling rate
#third parameter is the bit depth - currently set to 16 bits
wavfile.write("sound.wav", rate, wave.astype(numpy.int16))
print("Wrote %d samples to sound.wav"%len(wave))

#code to create a plot of the digitised wave
pylab.plot(time[:rate//100], wave[:rate//100], ':b')
pylab.xlabel("time (seconds)")
pylab.ylabel("Amplitude")

#saves the plot
pylab.savefig("plot.png")