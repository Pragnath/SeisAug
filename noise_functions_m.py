import numpy as np
import matplotlib.pyplot as plt
from obspy import read, Trace
from scipy import signal

def add_noise(data, noise_level_db):
    noise_level_linear = 10 ** (noise_level_db / 20)
    noise = np.random.normal(size=data.shape)
    noise = noise / np.std(noise)
    return data + noise_level_linear * noise

def add_pink_noise(data, noise_level_db):
    noise_level_linear = 10 ** (noise_level_db / 20)
    n = len(data)
    freqs = np.fft.rfftfreq(n)
    freqs[0] = 1
    white = np.fft.rfft(np.random.normal(size=n))
    pink_spectrum = white / np.sqrt(freqs)
    pink_noise = np.fft.irfft(pink_spectrum, n=n)
    std = np.std(pink_noise)
    if std == 0:
        std = 1
    pink_noise = pink_noise / std
    return data + noise_level_linear * pink_noise

def add_monofrequency_noise(data, noise_level_db, fs, freq):
    noise_level_linear = 10 ** (noise_level_db / 20)
    time = np.arange(data.shape[0]) / fs
    noise = np.sin(2 * np.pi * freq * time)
    noise = noise / np.std(noise)
    return data + noise_level_linear * noise

def add_bandpass_noise(data, noise_level_db, fs, low_freq, high_freq):
    noise_level_linear = 10 ** (noise_level_db / 20)
    white_noise = np.random.normal(size=data.shape)
    white_noise = white_noise / np.std(white_noise)
    sos = signal.butter(10, [low_freq, high_freq], btype='band', fs=fs, output='sos')
    bandpass_noise = signal.sosfilt(sos, white_noise)
    std = np.std(bandpass_noise)
    if std == 0:
        std = 1
    bandpass_noise = bandpass_noise / std
    return data + noise_level_linear * bandpass_noise

def add_spikes(num_spikes, spike_amp_ratio, file_path):
    st = read(file_path)
    sp = st[0].stats.sampling_rate
    waveform = st[0].data
    waveform_copy = waveform.copy()
    max_amp = np.max(np.abs(waveform_copy))
    spike_amp = spike_amp_ratio * max_amp
    spike_indices = np.random.randint(0, len(waveform_copy), num_spikes)
    for idx in spike_indices:
        waveform_copy[idx] += spike_amp * np.random.choice([-1, 1])
    t = np.arange(len(waveform)) / sp
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, waveform, label='Original Data')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Original Data')
    plt.grid(True)
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(t, waveform_copy, label='Modified Data')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Modified Data')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(10, 9))
    plt.subplot(2, 1, 1)
    plt.specgram(waveform, Fs=sp, NFFT=1024, noverlap=512)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectrogram of Original Data')
    plt.subplot(2, 1, 2)
    plt.specgram(waveform_copy, Fs=sp, NFFT=1024, noverlap=512)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectrogram of Modified Data')
    plt.tight_layout()
    plt.show()
    return waveform_copy

def time_shift(trace, seconds, plot=False):
    delta = trace.stats.delta
    num_points = int(seconds / delta)
    if num_points <= 0:
        return
    last_seconds = trace.data[-num_points:]
    trace.data = np.concatenate((last_seconds, trace.data[:-num_points]))
    if plot:
        trace.plot()
