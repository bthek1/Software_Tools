# Sound Testing

Sound Testing

Author

Benedict Thekkel

## 🎙️ 2. **Record Audio from Microphone in Jupyter**

``` python
import sounddevice as sd

devices = sd.query_devices()

print("Available audio input devices:")
for i, device in enumerate(devices):
    if device['max_input_channels'] > 0:
        print(f"[{i}] {device['name']} - Input - {device['hostapi']}")

print("\nAvailable audio output devices:")
for i, device in enumerate(devices):
    if device['max_output_channels'] > 0:
        print(f"[{i}] {device['name']} - Output - {device['hostapi']}")
```

    🎙️ Available audio input devices:
    [0] UM02: USB Audio (hw:1,0) — Input — 0
    [5] HD-Audio Generic: ALC897 Analog (hw:3,0) — Input — 0
    [7] HD-Audio Generic: ALC897 Alt Analog (hw:3,2) — Input — 0
    [8] UGREEN camera 2K: USB Audio (hw:4,0) — Input — 0

    🔊 Available audio output devices:
    [1] HDA NVidia: KAMN27UC6LA (hw:2,3) — Output — 0
    [2] HDA NVidia: KAMN27UC6LA (hw:2,7) — Output — 0
    [3] HDA NVidia: HDMI 2 (hw:2,8) — Output — 0
    [4] HDA NVidia: HDMI 3 (hw:2,9) — Output — 0
    [5] HD-Audio Generic: ALC897 Analog (hw:3,0) — Output — 0
    [6] HD-Audio Generic: ALC897 Digital (hw:3,1) — Output — 0

``` python
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os
import threading

# Configuration
samplerate = 44100
duration = 10  # seconds

# Devices and labels
mic_devices = {
    0: "mic",
    8: "camera"
}
recordings = {}

# Output folder
os.makedirs("mic_tests", exist_ok=True)

print("Starting mic recordings...\n")

# Thread worker to record from a mic
def record_mic(device_id, name):
    try:
        print(f"Recording from {name} (device {device_id})...")
        data = sd.rec(
            int(samplerate * duration),
            samplerate=samplerate,
            channels=1,
            dtype='float32',
            device=device_id
        )
        sd.wait()  # Wait until recording is complete

        # Save to WAV
        int16_data = np.clip(data * 32767, -32768, 32767).astype(np.int16)
        write(f"mic_tests/{name}.wav", samplerate, int16_data)

        recordings[name] = data.flatten()
        print(f"Saved: {name} (device {device_id})")
    except Exception as e:
        print(f"Error with {name} (device {device_id}): {e}")

# Start mic recording threads
threads = []
for device_id, name in mic_devices.items():
    thread = threading.Thread(target=record_mic, args=(device_id, name))
    thread.start()
    threads.append(thread)

# Wait for recordings to finish
for thread in threads:
    thread.join()

print("\nAll recordings complete.")
```

    🎙️ Starting mic recordings...

    ⏺️ Recording from mic (device 0)...
    ⏺️ Recording from camera (device 8)...
    ✔️ Saved: mic (device 0)
    ✔️ Saved: camera (device 8)

    ✅ All recordings complete.

✅ You now have a 5-second recording from your default microphone.

------------------------------------------------------------------------

## 📊 3. **Visualize the Audio Waveform**

``` python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create subplots for each mic
fig = make_subplots(rows=len(recordings), cols=1, shared_xaxes=True,
                    vertical_spacing=0.05,
                    subplot_titles=[f"Waveform: {name}" for name in recordings.keys()])

# Plot each waveform
for idx, (name, signal) in enumerate(recordings.items(), start=1):
    fig.add_trace(go.Scatter(
        y=signal,
        mode='lines',
        name=name,
        line=dict(width=1)
    ), row=idx, col=1)

# Layout
fig.update_layout(
    height=250 * len(recordings),
    width=1000,
    title_text="Microphone Waveform Comparison",
    showlegend=False,
)

fig.update_xaxes(title_text="Samples")
fig.update_yaxes(title_text="Amplitude")

fig.show()
```

## 🔊 4. **Playback in Notebook (Optional)**

``` python
from IPython.display import Audio, display

print("Playing back recorded audio...\n")

for name in recordings.keys():
    filepath = f"mic_tests/{name}.wav"
    print(f"{name.capitalize()}")
    display(Audio(filepath))
```

    🎧 Playing back recorded audio...

    ▶️ Mic

Your browser does not support the audio element.

    ▶️ Camera

Your browser does not support the audio element.

## Quality Checks

``` python
for name, signal in recordings.items():
    rms = np.sqrt(np.mean(signal**2))
    peak = np.max(np.abs(signal))
    print(f"{name.capitalize()}: RMS = {rms:.4f}, Peak Amplitude = {peak:.4f}")
```

    Mic: RMS = 0.0130, Peak Amplitude = 0.1201
    Camera: RMS = 0.0642, Peak Amplitude = 1.0000

``` python
from IPython.display import Audio, display
import wave
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'notebook'  # Change to 'iframe' or 'browser' if needed

print("\nMicrophone Quality Analysis:\n")

for name in sorted(recordings.keys()):
    filepath = f"mic_tests/{name}.wav"
    print(f"\n{name.capitalize()}: {filepath}")
    
    # Playback
    display(Audio(filepath))

    # Load audio file
    with wave.open(filepath, 'rb') as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()
        audio_bytes = wf.readframes(n_frames)

    # Determine dtype
    dtype = np.int16 if sampwidth == 2 else np.uint8
    audio = np.frombuffer(audio_bytes, dtype=dtype)

    # Normalize if needed
    if dtype == np.int16:
        audio = audio.astype(np.float32) / 32768.0

    # === Waveform Plot ===
    waveform_fig = go.Figure()
    waveform_fig.add_trace(go.Scatter(
        y=audio,
        mode='lines',
        name='Amplitude',
        line=dict(width=1),
    ))
    waveform_fig.update_layout(
        title=f"{name.capitalize()} - Waveform",
        xaxis_title="Samples",
        yaxis_title="Amplitude (normalized)",
        height=300,
        margin=dict(l=40, r=40, t=40, b=40),
    )
    waveform_fig.show()

    # === Metrics ===
    rms = np.sqrt(np.mean(audio**2))
    peak = np.max(np.abs(audio))
    noise_est = np.sqrt(np.mean(audio[:samplerate]**2))  # First second

    print(f"  - RMS Amplitude: {rms:.4f}")
    print(f"  - Peak Amplitude: {peak:.4f}")
    print(f"  - Estimated Noise Floor (RMS, first second): {noise_est:.4f}")

    # === Frequency Spectrum ===
    fft_data = np.fft.fft(audio)
    freqs = np.fft.fftfreq(len(audio), 1 / framerate)
    magnitude_db = 20 * np.log10(np.abs(fft_data[:len(freqs)//2]) + 1e-6)

    spectrum_fig = go.Figure()
    spectrum_fig.add_trace(go.Scatter(
        x=freqs[:len(freqs)//2],
        y=magnitude_db,
        mode='lines',
        name='Magnitude (dB)',
        line=dict(width=1),
    ))
    spectrum_fig.update_layout(
        title=f"{name.capitalize()} - Frequency Spectrum",
        xaxis_title="Frequency (Hz)",
        yaxis_title="Magnitude (dB)",
        height=300,
        margin=dict(l=40, r=40, t=40, b=40),
    )
    spectrum_fig.show()
```

    📊 Microphone Quality Analysis:


    🎙️ Camera: mic_tests/camera.wav

Your browser does not support the audio element.

      • RMS Amplitude: 0.0642
      • Peak Amplitude: 1.0000
      • Estimated Noise Floor (RMS, first second): 0.0020

    🎙️ Mic: mic_tests/mic.wav

Your browser does not support the audio element.

      • RMS Amplitude: 0.0129
      • Peak Amplitude: 0.1201
      • Estimated Noise Floor (RMS, first second): 0.0085

Back to top
