import cv2 as cv

# Resized videos
capture = cv.VideoCapture("AdWhirl.mp4")

def rescale_function(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize((frame, dimensions, cv.INTER_AREA))


while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_function(frame)
    cv.imshow('video', frame)
    cv.imshow('video_resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
