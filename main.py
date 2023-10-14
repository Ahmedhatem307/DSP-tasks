import matplotlib.pyplot as plt
import numpy as np
from comparesignals import SignalSamplesAreEqual


signal_type = input("type: ")
amplitude = int(input("Amplitude: "))
analog_freq = int(input("Analog Frequency: "))
sampling_freq = int(input("Sampling Frequency: "))
phase_shift = float(input("Phase Shift: "))
duration = 1    # 1 Second

if signal_type == "sin":
    t = np.linspace(0, duration, int(duration * sampling_freq), endpoint=False)
    angular_freq = 2 * np.pi * analog_freq
    wave_form = amplitude * np.sin(angular_freq * t + phase_shift)
    SignalSamplesAreEqual("SinOutput.txt", 720, wave_form)
elif signal_type == "cos":
    t = np.linspace(0, duration, int(duration * sampling_freq), endpoint=False)
    angular_freq = 2 * np.pi * analog_freq
    wave_form = amplitude * np.cos(angular_freq * t + phase_shift)
    SignalSamplesAreEqual("CosOutput.txt", 500, wave_form)


file_path = "signal1.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()

    # Read the first three line and save them which are for signal type, periodic or not and number of samples
    signal_type = int(lines[0].strip())
    is_periodic = int(lines[1].strip())
    num_samples = int(lines[2].strip())

    samples = []
    # After checking if it's a time domain or frequency domain signal add the special parameters to the sample array
    for line in lines[3:]:
        parts = line.strip().split()
        if signal_type == 0:  # Time domain signal
            sample_index = int(parts[0])
            sample_amplitude = float(parts[1])
            samples.append((sample_index, sample_amplitude))
        elif signal_type == 1:  # Frequency domain signal
            frequency = float(parts[0])
            amplitude = float(parts[1])
            phase_shift = float(parts[2])
            samples.append((frequency, amplitude, phase_shift))

# Plotting the signal samples
if signal_type == 0:  # Time domain signal
    sample_indices = [sample[0] for sample in samples]
    sample_amplitudes = [sample[1] for sample in samples]

    # Continuous representation (line plot)
    plt.figure(figsize=(8, 4))
    plt.plot(sample_indices, sample_amplitudes)
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.title('Continuous Representation (Time Domain)')
    plt.grid(True)
    plt.show()

    # Discrete representation (stem plot)
    plt.figure(figsize=(8, 4))
    plt.stem(sample_indices, sample_amplitudes, use_line_collection=True)
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.title('Discrete Representation (Time Domain)')
    plt.grid(True)
    plt.show()

elif signal_type == 1:  # Frequency domain signal
    frequencies = [sample[0] for sample in samples]
    amplitudes = [sample[1] for sample in samples]
    phase_shifts = [sample[2] for sample in samples]

    # Continuous representation (line plot)
    plt.figure(figsize=(8, 4))
    plt.plot(frequencies, amplitudes)
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.title('Continuous Representation (Frequency Domain)')
    plt.grid(True)
    plt.show()

    # Discrete representation (stem plot)
    plt.figure(figsize=(8, 4))
    plt.stem(frequencies, amplitudes, use_line_collection=True)
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.title('Discrete Representation (Frequency Domain)')
    plt.grid(True)
    plt.show()
