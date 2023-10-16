import subprocess
import pyautogui
import time
import pyperclip as pyp
import pandas as pd
from datetime import datetime


def sign_in(meetingid, pswd, meetingurl, classname):
    # Opens up the zoom app
    # change the path specific to your computer

    # If on windows use below line for opening zoom
    print("Opening Zoom")
    # Replace the {USER} with your username on your pc
    subprocess.call("C:\\Users\\{USER}\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

    time.sleep(5)
    pyautogui.getWindowsWithTitle("Zoom")[0].activate()
    print("Zoom activated on the screen")
    if classname != "nan":
        print("Joinning for the class: " + classname)
    if meetingurl != "nan":
        print(meetingurl)
    if meetingid != "nan":
        print("Meeting ID: " + meetingid)
    if pswd != "nan":
        print("Meeting password: " + pswd)

    time.sleep(3)

    # clicks the join button
    print("Joining the meeting")

    join_btn = pyautogui.locateCenterOnScreen("pics/join_button.png", confidence=0.9)
    # print(join_btn)
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # Type the meeting ID
    meeting_id_btn = pyautogui.locateCenterOnScreen("pics/meeting_id_button.png")
    # print(meeting_id_btn)
    pyautogui.moveTo(meeting_id_btn)
    # pyautogui.click()
    if meetingid == "nan":
        # print("No meeting id")
        pyp.copy(meetingurl)
        print("Copied link to clipboard : " + meetingurl)
        pyautogui.hotkey("ctrl", "v")
        # pyautogui.write(meetingurl)
    else:
        pyautogui.write(meetingid)
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(5)

    # Types the password and hits enter

    meeting_pswd_btn = pyautogui.locateCenterOnScreen(
        "pics/meeting_pswd.png", confidence=0.9
    )

    pyautogui.moveTo(meeting_pswd_btn)
    # pyautogui.click()
    pyautogui.write(pswd)
    print("Typed password")
    time.sleep(3)
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
            if row["meetingid"] == "None":
                m_id = ""
            else:
                m_id = str(row["meetingid"])
            if row["meetingpswd"] == "None":
                m_pswd = ""
            else:
                m_pswd = str(row["meetingpswd"])
            m_url = row["meetingurl"]
            if row["classname"] == "None":
                m_name = ""
            else:
                m_name = str(row["classname"])

            sign_in(m_id, m_pswd, m_url, m_name)
            time.sleep(46)
            print("signed in to meeting id:", m_id)
