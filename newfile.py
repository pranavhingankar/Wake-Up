import cv2
import obswebsocket
from obswebsocket import obsws

ip_address = "192.168.1.8"
port = 4455
password = "XOiDvavjR9yOcLmI"

# Create a websocket connection to OBS
ws = obsws(ip_address, port, password)
ws.connect()
# Get the list of scenes
get_scenes_request = obswebsocket.requests.GetSceneList()
scenes = ws.call(get_scenes_request)

# Create a VideoCapture object for the websocket connection
for scene in scenes:
    cap = cv2.VideoCapture(ws, scene.name)

# Start capturing frames
while True:
    # Capture a frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("OBS WebSocket Capture", frame)

    # Quit if the user presses ESC
    if cv2.waitKey(1) == 27:
        break

# Close the websocket connection
ws.close()
