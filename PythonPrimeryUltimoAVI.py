import cv2

# Get the path to the DAV file
video_path = "C:\\Users\\hjorquera\\Desktop\\DAV\\NVR_ch1_main_20230131000000_20230131010000.dav"

# Get the path to the output file
output_path = "C:\\Users\\hjorquera\\Desktop\\DAV\\RESUMEN_NVR_ch1_main_20230131000000_20230131010000.avi"

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit(1)

# Get the frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Read the first frame
ret, first_frame = cap.read()

# Read the last frame
cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
ret, last_frame = cap.read()

# Create a VideoWriter object
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# Write the first frame to the output file
out.write(first_frame)

# Write the last frame to the output file
out.write(last_frame)

# Close the output file
out.release()

# Close the video file
cap.release()

# Destroy the window
cv2.destroyAllWindows()
