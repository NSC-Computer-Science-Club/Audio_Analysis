import os
import numpy as np
import scipy
import librosa
from librosa import display
import matplotlib.pyplot as plt

"""
Dependencies
* numpy
* scipy
* librosa
* matplotlib
"""

class Audio_Loader:


    @staticmethod
    def load_audio(file_path):
        """
        Loads audio data from a file and returns the samples and sampling rate

        Parameters
        file_path - the path of the file

        Return
        1. the samples (audio time series)
        2. the sampling rate (amplitudes per second)
        """
        
        return librosa.load(file_path)


    @staticmethod
    def fourier_transform(samples, sampling_rate):
        """
        Performs a Fourier transformation on some samples

        Parameters
        samples - the samples
        sampling_rate - the sampling rate (amplitudes per second)

        Return
        I have no idea
        1. the x values (frequency)?
        2. the y values (magnitude)?
        """

        T = 1 / sampling_rate
        yf = scipy.fft.fft(samples)
        xf = np.linspace(0.0, 1.0/(2.0*T), sampling_rate//2)
        return xf, yf


    @staticmethod
    def plot_waveform(samples, sampling_rate, title="No Title"):
        """
        Plots the original waveform

        Parameters
        samples - the samples
        sampling_rate - the sampling rate (amplitudes per second)
        title - the title of the graph
        """

        librosa.display.waveplot(y = samples, sr = sampling_rate)
        plt.title(title)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.show()


    @staticmethod
    def plot_fft(xf, yf, sampling_rate, title="No Title"):
        """
        Plots the Fourier transformation

        Parameters
        xf - the frequency
        yf - the magnitude
        sampling_rate - the sampling rate
        title - the title of the graph
        """

        plt.plot(xf, 2.0/sampling_rate * np.abs(yf[0:sampling_rate//2]))
        plt.grid()
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title(title)
        plt.show()


    @staticmethod
    def spectrogram(samples, sampling_rate):
        """
        Generates spectrogram data using the samples and sampling rate

        Parameters
        samples - the samples
        sampling_rate - the sampling rate

        Return
        1. f (frequency?)
        2. t (time?)
        3. Sxx ?
        """
        
        return scipy.signal.spectrogram(samples, sampling_rate)


    @staticmethod
    def plot_spectrogram(f, t, Sxx, title="No Title"):
        """
        Plots the spectrogram

        Parameters
        f
        t
        Ssx
        title - the title of the graph
        """
        
        plt.pcolormesh(t, f, Sxx, shading='gouraud')
        plt.title(title)
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.show()
        

# Usage of the above class
def main():
    
    v_samples, v_sampling_rate = Audio_Loader.load_audio(os.path.join("data", "violin.wav"))
    t_samples, t_sampling_rate = Audio_Loader.load_audio(os.path.join("data", "trumpet.wav"))

    Audio_Loader.plot_waveform(v_samples, v_sampling_rate, "Violin Original Waveform")
    Audio_Loader.plot_waveform(t_samples, t_sampling_rate, "Trumpet Original Waveform")

    v_xf, v_yf = Audio_Loader.fourier_transform(v_samples, v_sampling_rate)
    t_xf, t_yf = Audio_Loader.fourier_transform(t_samples, t_sampling_rate)

    Audio_Loader.plot_fft(v_xf, v_yf, v_sampling_rate, "Violin Fourier Transform")
    Audio_Loader.plot_fft(t_xf, t_yf, t_sampling_rate, "Trumpet Fourier Transform")

    v_f, v_t, v_Sxx = Audio_Loader.spectrogram(v_samples, v_sampling_rate)
    t_f, t_t, t_Sxx = Audio_Loader.spectrogram(t_samples, t_sampling_rate)
    
    Audio_Loader.plot_spectrogram(v_f, v_t, v_Sxx, "Violin Spectrogram")
    Audio_Loader.plot_spectrogram(t_f, t_t, t_Sxx, "Trumpet Spectrogram")
    
    
main()
