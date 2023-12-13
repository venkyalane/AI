import cv2 as cv

# images reading
# img = cv.imread('images1.jpg')
# cv.imshow('image', img)
# cv.waitKey(0)

# reading videos
# capture = cv.VideoCapture("AdWhirl.mp4")
#
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video', frame)
#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break
#
# capture.release()
# cv.destroyAllWindows()

# Resized videos
capture = cv.VideoCapture("AdWhirl.mp4")


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


while True:
    isTrue, Frame = capture.read()
    frame_resized_1 = rescaleFrame(Frame)
    frame_resized_2 = rescaleFrame(Frame, scale=0.65)
    frame_resized_3 = rescaleFrame(Frame, scale=0.55)
    cv.imshow('original_video', Frame)
    cv.imshow('video_resized_1', frame_resized_1)
    cv.imshow('video_resized_2', frame_resized_2)
    cv.imshow('video_resized_3', frame_resized_3)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
