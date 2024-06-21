import cv2
import numpy as np
import imutils
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Ứng dụng nhận diện màu sắc")

def start_capture():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_Yellow = np.array([20, 100, 100])
        upper_Yellow = np.array([40, 255, 255])

        lower_Green = np.array([40, 40, 40])
        upper_Green = np.array([80, 255, 255])

        lower_Red = np.array([0, 100, 100])
        upper_Red = np.array([10, 255, 255])

        lower_Blue = np.array([90, 50, 50])
        upper_Blue = np.array([130, 255, 255])

        lower_Purple = np.array([120, 50, 50])
        upper_Purple = np.array([160, 255, 255])

        lower_White = np.array([0, 0, 200])
        upper_White = np.array([180, 30, 255])

        lower_Black = np.array([0, 0, 0])
        upper_Black = np.array([180, 255, 30])

        lower_Skin = np.array([0, 20, 70])
        upper_Skin = np.array([20, 255, 255])
        
        lower_Pink = np.array([140, 40, 40])
        upper_Pink = np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower_Yellow, upper_Yellow)
        mask2 = cv2.inRange(hsv, lower_Green, upper_Green)
        mask3 = cv2.inRange(hsv, lower_Red, upper_Red)
        mask4 = cv2.inRange(hsv, lower_Blue, upper_Blue)
        mask5 = cv2.inRange(hsv, lower_Purple, upper_Purple)
        mask6 = cv2.inRange(hsv, lower_White, upper_White)
        mask7 = cv2.inRange(hsv, lower_Black, upper_Black)
        mask_skin = cv2.inRange(hsv, lower_Skin, upper_Skin)
        mask_pink = cv2.inRange(hsv, lower_Pink, upper_Pink)

        cnts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts1 = imutils.grab_contours(cnts1)

        cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts2 = imutils.grab_contours(cnts2)

        cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts3 = imutils.grab_contours(cnts3)

        cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts4 = imutils.grab_contours(cnts4)

        cnts5 = cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts5 = imutils.grab_contours(cnts5)

        cnts6 = cv2.findContours(mask6, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts6 = imutils.grab_contours(cnts6)

        cnts7 = cv2.findContours(mask7, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts7 = imutils.grab_contours(cnts7)

        cnts_skin = cv2.findContours(mask_skin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts_skin = imutils.grab_contours(cnts_skin)

        cnts_pink = cv2.findContours(mask_pink, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts_pink = imutils.grab_contours(cnts_pink)

        for c in cnts1:
            area1 = cv2.contourArea(c)
            if area1 > 5000:
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "Yellow", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        for c in cnts2:
            area2 = cv2.contourArea(c)
            if area2 > 5000:
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "Green", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        for c in cnts3:
            area3 = cv2.contourArea(c)
            if area3 > 5000:
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "Red", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        for c in cnts4:
            area4 = cv2.contourArea(c)
            if area4 > 5000:
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "Blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        for c in cnts5:
            area5 = cv2.contourArea(c)
            if area5 > 5000:
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "Purple", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        for c in cnts6:
            area6 = cv2.contourArea(c)
            if area6 > 5000:
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "White", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        for c in cnts7:
            area7 = cv2.contourArea(c)
            if area7 > 5000:
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "Black", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        for c in cnts_skin:
            area_skin = cv2.contourArea(c)
            if area_skin > 5000:
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "Skin", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        for c in cnts_pink:
            area_pink = cv2.contourArea(c)
            if area_pink > 5000:
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "Pink", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        frame = cv2.resize(frame, (1280, 960))

        cv2.namedWindow("frame", cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()

def stop_capture():
    cv2.destroyAllWindows()
    root.destroy()

start_button = tk.Button(root, text="Bắt đầu", command=start_capture)
start_button.pack(pady=100, padx=500)

stop_button = tk.Button(root, text="Thoát", command=stop_capture)
stop_button.pack(pady=100, padx=500)

panel = tk.Label(root)
panel.pack(padx=10, pady=10)

root.mainloop()
