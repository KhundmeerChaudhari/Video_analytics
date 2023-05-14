import cv2
import numpy as np
import easyocr

def run():
        
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("failed to capture video")
        exit()

    while True:
        ret, frame = cap.read()
        reader=easyocr.Reader(['en'],gpu=False)
        result=reader.readtext(frame)
        for detection in result:
            text = detection[1]
            bounding_box = detection[0]
            org = (int(bounding_box[0][0]), int(bounding_box[0][1] - 10))
            cv2.putText(frame, text, org, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            pt1 = (int(bounding_box[0][0]), int(bounding_box[0][1]))
            pt2 = (int(bounding_box[2][0]), int(bounding_box[2][1]))
            cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 2)
            print(detection)

        if ret:
            cv2.imshow('Live Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()
run()