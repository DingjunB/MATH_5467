### Image Input and Output
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from IPython.display import Audio
##I = plt.imread('https://homepages.cae.wisc.edu/~ece533/images/sails.png')
##I.shape # (512, 768, 3)
##print(I.max()) # 0.9882353
##print(I.min()) # 0.007843138

##plt.figure(figsize=(15,15))
##plt.imshow(I)
##plt.show()

##I_noisy = I + 0.5*np.random.randn(I.shape[0],I.shape[1],I.shape[2])
##I_noisy = np.clip(I_noisy,0,1)
##plt.figure(figsize=(15,15))
##plt.imshow(I_noisy)
##plt.show()
##
##plt.imsave('sail_noisy.png',I_noisy)

### Audio Input and Output
##!wget http://www-users.math.umn.edu/~jwcalder/5467S21/classical.mp3
##!ffmpeg -y -i classical.mp3 classical.wav
fs, data = wavfile.read('classical.wav')
print(fs) # 22050
print(data.shape) #(2161965, 2)
#The sample rate fs is 22,050. This means there are 22,050 samples per second.
#The size of the data is 2,161,965 by 2. This is stereo audio with two channels (left and right speakers).
#We can get the length of the audio file in seconds by dividing the number of samples by the sample rate.
length = data.shape[0]/fs
print('The .wav file is %.2f seconds long.'%length) #The .wav file is 98.05 seconds long.
#We can use matplotlib to plot the signal.
#plt.plot(data[:,0])
#plt.plot(data[:,1])

#We see both channel plotted in orange and blue. It's kind of a mess since we are plotting the whole song. Let's just plot part instead.
plt.plot(data[10000:10400,0])
plt.plot(data[10000:10400,1])
plt.show()
#We can use IPython to play the audio recording. IPython prefers the data to be transposed from how scipy returns a .wav file.
Audio(data.T,rate=fs,autoplay=True)
#Let's add a bit of noise to the audio recording and play that.
data_noisy = data + 500*np.random.randn(data.shape[0],data.shape[1])
Audio(data_noisy.T,rate=fs,autoplay=True)
#Finally, we can save the modified .wav file and can play it in any other audio player we like.
wavfile.write('classical_noisy.wav',fs,data_noisy)
#We can also convert the saved .wav file to .mp3 to reduce the file size.
#!ffmpeg -y -i classical_noisy.wav classical_noisy.mp3
#Try playing classical_noisy.mp3. Does it sound anything like classical_noisy.wav? Why do you think this is?
#They do not sound the same at all. The quality of classical_noisy is very low. Since it was noisy already, the compressed process for mp3 made the music almost unrecognizable. The bit rate is only bitrate=  64.1kbits/s.
