# Camera Testing

Camera Testing

Author

Benedict Thekkel

``` python
import cv2

print("Scanning for available camera devices...\n")

available_cams = []
for index in range(10):
    cap = cv2.VideoCapture(index)
    if cap is not None and cap.read()[0]:
        print(f"  Camera [{index}] is available and working.")
        available_cams.append(index)
        cap.release()
    else:
        print(f"  Camera [{index}] not found or cannot be opened.")

# Summary
print("\nScan Complete")
print(f"Total cameras scanned: 10")
print(f"Working cameras found: {len(available_cams)}")

if available_cams:
    print("Available camera indices:", available_cams)
else:
    print("No working cameras were detected.")
```

    🔍 Scanning for available camera devices...

      ❌ Camera [0] not found or cannot be opened.

    [ WARN:0@10.018] global cap_v4l.cpp:1136 tryIoctl VIDEOIO(V4L2:/dev/video0): select() timeout.

      ✅ Camera [1] is available and working.
      ❌ Camera [2] not found or cannot be opened.
      ❌ Camera [3] not found or cannot be opened.
      ❌ Camera [4] not found or cannot be opened.
      ❌ Camera [5] not found or cannot be opened.
      ❌ Camera [6] not found or cannot be opened.
      ❌ Camera [7] not found or cannot be opened.
      ❌ Camera [8] not found or cannot be opened.
      ❌ Camera [9] not found or cannot be opened.

    📊 Scan Complete
    🔢 Total cameras scanned: 10
    📷 Working cameras found: 1
    ✅ Available camera indices: [1]

    [ WARN:0@10.640] global cap_v4l.cpp:999 open VIDEOIO(V4L2:/dev/video2): can't open camera by index
    [ERROR:0@10.640] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
    [ WARN:0@10.640] global cap_v4l.cpp:999 open VIDEOIO(V4L2:/dev/video3): can't open camera by index
    [ERROR:0@10.641] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
    [ WARN:0@10.641] global cap_v4l.cpp:999 open VIDEOIO(V4L2:/dev/video4): can't open camera by index
    [ERROR:0@10.641] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
    [ WARN:0@10.641] global cap_v4l.cpp:999 open VIDEOIO(V4L2:/dev/video5): can't open camera by index
    [ERROR:0@10.642] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
    [ WARN:0@10.642] global cap_v4l.cpp:999 open VIDEOIO(V4L2:/dev/video6): can't open camera by index
    [ERROR:0@10.642] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
    [ WARN:0@10.642] global cap_v4l.cpp:999 open VIDEOIO(V4L2:/dev/video7): can't open camera by index
    [ERROR:0@10.643] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
    [ WARN:0@10.643] global cap_v4l.cpp:999 open VIDEOIO(V4L2:/dev/video8): can't open camera by index
    [ERROR:0@10.643] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
    [ WARN:0@10.643] global cap_v4l.cpp:999 open VIDEOIO(V4L2:/dev/video9): can't open camera by index
    [ERROR:0@10.644] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range

``` python
import cv2
import numpy as np
import time
import threading
from IPython.display import display
import ipywidgets as widgets

# --- Camera defaults ---
camera_index = 1
default_width = 640
default_height = 480
default_delay = 0.05  # seconds (20 FPS)

# Global mutable state
frame_width = default_width
frame_height = default_height
frame_delay = default_delay
streaming = False
cap = None
stream_thread = None

# --- UI widgets ---
# Live video widget
live_widget = widgets.Image(
    format='jpg',
    width=frame_width,
    height=frame_height
)

# Camera status
status_label = widgets.Label("Camera ready", layout=widgets.Layout(margin='10px 0 0 10px'))

# Resolution selector
resolution_dropdown = widgets.Dropdown(
    options=[
        ("640x480", (640, 480)),
        ("800x600", (800, 600)),
        ("1280x720", (1280, 720)),
        ("1920x1080", (1920, 1080))
    ],
    value=(default_width, default_height),
    description='Resolution:'
)

# FPS selector
fps_dropdown = widgets.Dropdown(
    options=[
        ("10 FPS", 0.1),
        ("20 FPS", 0.05),
        ("30 FPS", 0.033)
    ],
    value=default_delay,
    description='Frame rate:'
)

# Control buttons
start_button = widgets.Button(description="Start Camera", button_style='success')
stop_button = widgets.Button(description="Stop Camera", button_style='danger', disabled=True)

# Output log
output_box = widgets.Output()

# --- Layout ---
control_panel = widgets.VBox([status_label, resolution_dropdown, fps_dropdown])
video_row = widgets.HBox([live_widget, control_panel])
button_row = widgets.HBox([start_button, stop_button])
layout = widgets.VBox([video_row, button_row, output_box])
display(layout)

# --- Helper functions ---
def frame_to_bytes(frame):
    _, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()

def update_camera_settings():
    global frame_width, frame_height, frame_delay
    frame_width, frame_height = resolution_dropdown.value
    frame_delay = fps_dropdown.value

def stream_camera():
    global cap, streaming
    with output_box:
        print("Camera stream started.")
    status_label.value = "Camera streaming..."
    try:
        while streaming:
            ret, frame = cap.read()
            if not ret:
                status_label.value = "Frame read failed"
                break
            live_widget.value = frame_to_bytes(frame)
            time.sleep(frame_delay)
    finally:
        if cap is not None:
            cap.release()
        status_label.value = "Camera stopped"
        with output_box:
            print("Camera released.")

def start_camera(_=None):
    global cap, streaming, stream_thread
    update_camera_settings()  # Update settings based on dropdowns
    
    # Stop the previous camera stream if it's running
    if cap is not None:
        cap.release()
    
    # Reinitialize the camera with new settings
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    
    # Try to set the frame rate (this may or may not work depending on the camera)
    cap.set(cv2.CAP_PROP_FPS, 1.0 / frame_delay)

    streaming = True
    stream_thread = threading.Thread(target=stream_camera, daemon=True)
    stream_thread.start()
    start_button.disabled = True
    stop_button.disabled = False

def stop_camera(_=None):
    global streaming
    streaming = False
    start_button.disabled = False
    stop_button.disabled = True
    if cap is not None:
        cap.release()

# --- Bind actions ---
start_button.on_click(start_camera)
stop_button.on_click(stop_camera)

# Automatically apply new settings if dropdowns change while streaming
def on_setting_change(change):
    # Print the updated resolution and frame rate when settings are changed
    print(f"Resolution: {frame_width}x{frame_height}")
    print(f"Frame rate: {1 / frame_delay:.2f} FPS")
    
    if streaming:
        stop_camera()  # Stop the camera
        while streaming:  # Wait for the stream to stop
            time.sleep(0.1)  # Wait a bit before restarting
        start_camera()  # Restart with new settings

# Observing dropdown changes
resolution_dropdown.observe(on_setting_change, names='value')
fps_dropdown.observe(on_setting_change, names='value')
```

``` python
import cv2
import numpy as np
import time
import threading
from IPython.display import display
import ipywidgets as widgets

# --- Camera defaults ---
camera_index = 1
# frame_width = 1920
# frame_height = 1080
frame_width = 640
frame_height = 480
frame_delay = 0.015  # seconds (20 FPS)

# Global mutable state
streaming = False
cap = None
stream_thread = None

# --- UI widgets ---
# Live video widget
live_widget = widgets.Image(
    format='jpg',
    width=frame_width,
    height=frame_height
)

# Camera status
status_label = widgets.Label("Camera ready", layout=widgets.Layout(margin='10px 0 0 10px'))

# Control buttons
start_button = widgets.Button(description="Start Camera", button_style='success')
stop_button = widgets.Button(description="Stop Camera", button_style='danger', disabled=True)

# Output log
output_box = widgets.Output()

# --- Layout ---
button_row = widgets.HBox([start_button, stop_button])
layout = widgets.VBox([live_widget, button_row, output_box])
display(layout)

# --- Helper functions ---
def frame_to_bytes(frame):
    _, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()

def stream_camera():
    global cap, streaming
    with output_box:
        print("Camera stream started.")
    status_label.value = "Camera streaming..."
    try:
        while streaming:
            ret, frame = cap.read()
            if not ret:
                status_label.value = "Frame read failed"
                break
            live_widget.value = frame_to_bytes(frame)
            time.sleep(frame_delay)
    finally:
        if cap is not None:
            cap.release()
        status_label.value = "Camera stopped"
        with output_box:
            print("Camera released.")

def start_camera(_=None):
    global cap, streaming, stream_thread
    # Initialize camera with default resolution and frame rate
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    cap.set(cv2.CAP_PROP_FPS, 1.0 / frame_delay)  # Set frame rate
    
    streaming = True
    stream_thread = threading.Thread(target=stream_camera, daemon=True)
    stream_thread.start()
    start_button.disabled = True
    stop_button.disabled = False

def stop_camera(_=None):
    global streaming
    streaming = False
    start_button.disabled = False
    stop_button.disabled = True
    if cap is not None:
        cap.release()

# --- Bind actions ---
start_button.on_click(start_camera)
stop_button.on_click(stop_camera)
```

``` python
import cv2
import numpy as np
import time
import threading
from IPython.display import display
import ipywidgets as widgets

# --- Camera defaults ---
camera_index = 1
frame_width = 1920
frame_height = 1080

frame_delay = 0.015  # seconds (20 FPS)

# Global mutable state
streaming = False
cap = None
stream_thread = None

# --- UI widgets ---
# Live video widget
live_widget = widgets.Image(
    format='jpg',
    width=frame_width,
    height=frame_height
)

# Camera status
status_label = widgets.Label("Camera ready", layout=widgets.Layout(margin='10px 0 0 10px'))

# Control buttons
start_button = widgets.Button(description="Start Camera", button_style='success')
stop_button = widgets.Button(description="Stop Camera", button_style='danger', disabled=True)

# Output log
output_box = widgets.Output()

# --- Layout ---
button_row = widgets.HBox([start_button, stop_button])
layout = widgets.VBox([live_widget, button_row, output_box])
display(layout)

# --- Helper functions ---
def frame_to_bytes(frame):
    _, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()

def stream_camera():
    global cap, streaming
    with output_box:
        print("Camera stream started.")
    status_label.value = "Camera streaming..."
    try:
        while streaming:
            ret, frame = cap.read()
            if not ret:
                status_label.value = "Frame read failed"
                break
            live_widget.value = frame_to_bytes(frame)
            time.sleep(frame_delay)
    finally:
        if cap is not None:
            cap.release()
        status_label.value = "Camera stopped"
        with output_box:
            print("Camera released.")

def start_camera(_=None):
    global cap, streaming, stream_thread
    # Initialize camera with default resolution and frame rate
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    cap.set(cv2.CAP_PROP_FPS, 1.0 / frame_delay)  # Set frame rate
    
    streaming = True
    stream_thread = threading.Thread(target=stream_camera, daemon=True)
    stream_thread.start()
    start_button.disabled = True
    stop_button.disabled = False

def stop_camera(_=None):
    global streaming
    streaming = False
    start_button.disabled = False
    stop_button.disabled = True
    if cap is not None:
        cap.release()

# --- Bind actions ---
start_button.on_click(start_camera)
stop_button.on_click(stop_camera)
```

Back to top
