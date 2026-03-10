<div align="center">

# 🌍 SeisAug
### A Python Toolkit for Seismological Waveform Data Augmentation

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![ObsPy](https://img.shields.io/badge/Powered%20by-ObsPy-green.svg)](https://www.obspy.org/)
[![Journal](https://img.shields.io/badge/Published-Applied%20Computing%20%26%20Geosciences-red.svg)](https://www.sciencedirect.com/science/article/pii/S259019742500014X)

</div>

---

## Overview

**SeisAug** addresses a fundamental challenge in seismological deep learning: the scarcity of region- and depth-specific labeled waveform data. By providing a suite of physically motivated augmentation techniques, SeisAug enables researchers to expand training datasets, improve model generalization, and simulate diverse noise environments encountered in real seismic networks.

> 📄 **Published in** *Applied Computing and Geosciences*, Volume 25, 2025.

---

## Augmentation Methods

| Method | Function | Description |
|---|---|---|
| White noise | `add_noise` | Additive Gaussian noise at a specified dB level |
| Pink (1/f) noise | `add_pink_noise` | Spectrally shaped 1/f noise via FFT domain scaling |
| Monofrequency noise | `add_monofrequency_noise` | Sinusoidal interference at a target frequency |
| Bandpass noise | `add_bandpass_noise` | Band-limited noise shaped by a Butterworth filter |
| Spike injection | `add_spikes` | Impulsive transients at random sample indices |
| Time shift | `time_shift` | Circular shift of waveform by N samples |
| Signal convolution | `interactive_plot` | Convolution of seismic trace with sine or step signal |

---

## Installation

### Via pip

```bash
git clone https://github.com/Pragnath/SeisAug.git
cd SeisAug
pip install -r requirements.txt
```

### Via Conda (recommended)

```bash
git clone https://github.com/Pragnath/SeisAug.git
cd SeisAug
conda env create -f environment.yml
conda activate seisaug
```

### Google Colab

```python
!git clone https://github.com/Pragnath/SeisAug
%cd SeisAug
!pip install -r requirements.txt
%run SeisAug.ipynb
```

---

## Quickstart

```python
from obspy import read
from noise_functions_m import add_noise, add_pink_noise, add_bandpass_noise, time_shift

st = read("data/2015-01-20-1711-04M.SJX___003_uni")
tr = st[0]

# Add white Gaussian noise at 20 dB
tr.data = add_noise(tr.data, noise_level_db=20)

# Add spectrally correct pink (1/f) noise
tr.data = add_pink_noise(tr.data, noise_level_db=15)

# Add band-limited noise between 5–25 Hz
fs = tr.stats.sampling_rate
tr.data = add_bandpass_noise(tr.data, noise_level_db=10, fs=fs, low_freq=5, high_freq=25)

# Circular time shift by 5 seconds
time_shift(tr, seconds=5)
```

---

## Example Output

**White noise augmentation** at 20%, 40%, 60%, and 80% signal levels:

![White_noise](https://github.com/ISR-AIML/SeisAug/assets/163402495/db64d62e-beed-481d-a6f7-039bd1169669)

**Band-limited noise** in the 15–30 Hz range (changes in spectral content are visible in corresponding spectrograms):

![bandpass_noise](https://github.com/ISR-AIML/SeisAug/assets/163402495/98f3a745-1ed7-4f2d-83d9-afff27dba0f6)

**Monofrequency (30 Hz) sinusoidal noise** with spectral footprint visible in spectrograms:

![mono_freq](https://github.com/ISR-AIML/SeisAug/assets/163402495/614712ff-da18-44c8-a63d-efc8746c0de5)

---

## Data

The example MiniSEED files provided in `data/` are sourced from the **Southern California Earthquake Data Center (SCEDC)**.

> SCEDC (2013): Southern California Earthquake Data Center. Caltech. Dataset. doi:[10.7909/C3WD3xH1](https://doi.org/10.7909/C3WD3xH1)

---

## Authors

| Name | Affiliation | Profile |
|---|---|---|
| **Pragnath D.** | Lead Author | [![Google Scholar](https://img.shields.io/badge/Google%20Scholar-4285F4?logo=google-scholar&logoColor=white)](https://scholar.google.com/citations?user=ZAzbmKYAAAAJ&hl=en) |
| Srijayanthi G. | Co-Author | — |
| Sanjay Kumar | Co-Author | — |
| Sandeep Chopra | Co-Author | — |

---

## Citation

If you use SeisAug in your research, please cite the following paper:

**APA:**
> Pragnath, D., Srijayanthi, G., Kumar, S., & Chopra, S. (2025). SeisAug: A data augmentation python toolkit. *Applied Computing and Geosciences, 25*, 100232. https://doi.org/10.1016/j.acags.2025.100232

**BibTeX:**

```bibtex
@article{Pragnath2025SeisAug,
  title   = {{SeisAug}: A data augmentation python toolkit},
  author  = {Pragnath, D. and Srijayanthi, G. and Kumar, S. and Chopra, S.},
  journal = {Applied Computing and Geosciences},
  volume  = {25},
  pages   = {100232},
  year    = {2025},
  doi     = {10.1016/j.acags.2025.100232},
  url     = {https://www.sciencedirect.com/science/article/pii/S259019742500014X}
}
```

---

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.
