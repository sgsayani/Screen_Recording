#project
#screen reording 

import cv2 as c
import pyautogui as p
import numpy as np

#create resolution
rs = (1700,1000)


#filename in which we store recording 
fn = input("Please enter any file name and path : ")

#fix frame rate
fps=20.0

#object
fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)

#create recording module

c.namedWindow("LIve_Rcording",c.WINDOW_NORMAL)
#c.resizeWindow("LIve_Recording", (600, 400))
#c.resizeWindow("LIve_Recording", 500, 200)


while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f, c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("LIve_Recording", f)
    if c.waitKey(1) ==ord("q"):
        break
output.release()
c.destroyAllWindows()

