import cv2

# This always points to the correct location for your installed opencv-python package
cascade_path = r"c:\Users\HP\OneDrive\Desktop\CV\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Sanity check — this is the key fix
if face_cascade.empty():
    raise IOError(f"Failed to load cascade classifier from: {cascade_path}")