import cv2
import time
from datetime import datetime
import os

# open video stream. Select your source like...
#cap = cv2.VideoCapture(0) # Do you want to test with the local camera?
cap = cv2.VideoCapture('rtsp://admintp:abc@192.168.0.125/stream1')
#cap = cv2.VideoCapture('rtsp://admintp:abc@192.168.0.138/stream1')
#cap = cv2.VideoCapture('rtsp://62.109.19.230:554/iloveyou')

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS) 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

fontText = cv2.FONT_HERSHEY_COMPLEX

while True:

    dt  = datetime.now().isoformat().replace(':','-').replace('.','-')

    out = cv2.VideoWriter('log/output' + dt + '.mp4', fourcc, fps, (int(w),int(h)))

    try:
        # start timer
        start_time = time.time()

        # Capture video from camera per 60 seconds
        while (int(time.time() - start_time) < 60):
            ret, frame = cap.read()
            if ret==True:

                #frame = cv2.flip(frame,0) # Do you want to FLIP the images?

                # text, coordinate, font, size of text,color,thickness of font
                cv2.putText(frame,'Hello There', (100,100), fontText, 2, (255,255,255), 3)  

                out.write(frame)

                # Display the resulting frame in a window. Enable/ Disable the next three lines to show/hide the window
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                  break
            else:
                break
    except cv2.error as e:
        print('CV2 error:', e)
    except Exception as e:
        print('Error', e)    
    else:
        print("No problem reported")                
    finally:        
        # Release output stream
        out.release()

    list_of_files = os.listdir('log')
    full_path = ["log/{0}".format(x) for x in list_of_files]

    if len(list_of_files) == 15:
        oldest_file = min(full_path, key=os.path.getctime)
        os.remove(oldest_file)

# Release input stream
cap.release()
#cv2.destroyAllWindows()