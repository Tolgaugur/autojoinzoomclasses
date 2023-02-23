import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime


def sign_in(meetingid, pswd):
    # Opens up the zoom app
    # change the path specific to your computer

    # If on windows use below line for opening zoom
    print("Opening Zoom")
    # subprocess.call('C:\\Users\\{USER}\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    subprocess.Popen('C:\\Users\\{USER}\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
   
    time.sleep(2)
    pyautogui.getWindowsWithTitle("Zoom")[0].activate()
    print("Zoom activated on the screen")
    time.sleep(5)
    


    
  
    # clicks the join button
    print("Joining the meeting")
  
    
    join_btn = pyautogui.locateCenterOnScreen('join_button.png',confidence=0.9)
    print(join_btn)
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # Type the meeting ID
    meeting_id_btn = pyautogui.locateCenterOnScreen("meeting_id_button.png")
    print(meeting_id_btn)
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meetingid)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)
    

    # Disables both the camera and the mic
    # media_btn = pyautogui.locateAllOnScreen("media_btn.png")
    # print(media_btn)
    # for btn in media_btn:
    #     pyautogui.moveTo(btn)
    #     pyautogui.click()
    #     time.sleep(5)

    # Hits the join button
    # join_btn = pyautogui.locateCenterOnScreen("join_btn.png",confidence=0.5)
    
    # pyautogui.moveTo(join_btn)
    # print("clicked join_btn",join_btn)
    
    # pyautogui.click()
    # time.sleep(5)

    # Types the password and hits enter

    meeting_pswd_btn = pyautogui.locateCenterOnScreen("meeting_pswd.png",confidence=0.9)
    print("found meeting pswd",meeting_pswd_btn)
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press("enter")


# Reading the file
df = pd.read_csv("timings.csv")

while True:
   # checking of the current time exists in our csv file
    now = datetime.now()
    current_day = now.strftime("%A")
    current_time = now.strftime("%H:%M")
    matches = df[(df["days"] == current_day) & (df["timings"] == current_time)]
    if not matches.empty:
        # sign in to Zoom meeting(s) for the current time and day

        for index, row in matches.iterrows():
            m_id = str(row["meetingid"])
            m_pswd = str(row["meetingpswd"])
            sign_in(m_id, m_pswd)
            time.sleep(40)
            print("signed in to meeting id:", m_id)
