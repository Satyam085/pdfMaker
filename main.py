# This is tool used to making pdf files of any online pdf which are not downloadable
import os
import time
import pyautogui
from datetime import datetime
from fpdf import FPDF

pyautogui.FAILSAFE = True

print('Enter the no. of pages below and open the browser window so that the file is visible in next 10 secs')
n = int(input('Enter no. of pages: '))
time.sleep(10)

# Enter the dimensions of page according to screen size
x1 = 0
y1 = 0
x2 = 500
y2 = 1000

now = datetime.now()
date_time = now.strftime("%m%d%Y%H%M")
fileName = date_time + '.pdf'

pdf = FPDF()

pyautogui.PAUSE = 2
pyautogui.press('home')

for i in range(n):
    page = pyautogui.screenshot('page' + str(i) + '.png', region=(x1, y1, x2, y2))
    pdf.add_page()
    pdf.image('page' + str(i) + '.png', 0, 0)
    pyautogui.press('pagedown')
    os.remove('page' + str(i) + '.png')

pdf.output(fileName, 'F')
pyautogui.alert('The file is successfully created')
