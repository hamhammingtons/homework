import cv2
import mediapipe as mp  # type: ignore
import numpy as np

# 1. Initialize the Neural Network (MediaPipe Face Detection)
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5
)

# 2. Load your images
# 'main_scene.jpg' is your background, 'overlay.png' is what you put on the patterns
img = cv2.imread("main_scene.jpg")
overlay = cv2.imread(
    "overlay.png", cv2.IMREAD_UNCHANGED
)  # Use UNCHANGED if it has transparency

# Convert to RGB for the neural network
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # type: ignore
results = face_detection.process(img_rgb)

if results.detections:
    for detection in results.detections:
        # 3. Get Coordinates
        bbox = detection.location_data.relative_bounding_box
        ih, iw, _ = img.shape  # type: ignore
        x, y, w, h = (
            int(bbox.xmin * iw),
            int(bbox.ymin * ih),
            int(bbox.width * iw),
            int(bbox.height * ih),
        )

        # 4. Overlay Logic
        # Resize mask to fit the detected pattern
        resized_mask = cv2.resize(overlay, (w, h))  # type: ignore

        # Simple overlay (replacing the region)
        img[y : y + h, x : x + w] = resized_mask[:, :, :3]  # type: ignore

# 5. Save and Show
cv2.imwrite("result_task1.jpg", img)  # type: ignore
cv2.imshow("Task 1 Result", img)  # type: ignore
cv2.waitKey(0)
