import pyautogui
import pyscreeze
import time

# 设定按钮图片的路径
button_image = 'E:/Desktop/button.png'  # 你的按钮小图

while True:
    location = pyautogui.locateCenterOnScreen(button_image, confidence=0.8)  # confidence可以调（0.8-0.9）
    if location is not None:
        print(f"找到按钮，坐标: {location}")
        pyautogui.moveTo(location.x, location.y, duration=0.5)
        pyautogui.click()
    else:
        print("没有找到按钮，继续检测...")

    time.sleep(10)  # 每10秒检测一次



import pyautogui
import pytesseract
from PIL import Image
import time
import tkinter as tk
from tkinter import messagebox

# （可选）指定tesseract路径，如果需要的话
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# 按钮截图文件
first_button_image = 'E:/Desktop/button.png'    # 第一个按钮小截图
second_button_image = 'E:/Desktop/buttonsubmit.png'  # 第二个按钮小截图

while True:
    # 第一步：找到第一个按钮并点击
    first_location = pyautogui.locateCenterOnScreen(first_button_image, confidence=0.8)
    if first_location:
        print(f"找到第一个按钮，点击中... {first_location}")
        pyautogui.moveTo(first_location.x, first_location.y, duration=0.5)
        pyautogui.click()
    else:
        print("未找到第一个按钮，继续等待...")
        time.sleep(1)
        continue

    # 第二步：等界面刷新
    time.sleep(2)

    # 第三步：截屏
    screenshot = pyautogui.screenshot()

    # 第四步：OCR识别+拿位置信息
    data = pytesseract.image_to_data(screenshot, lang='chi_sim', output_type=pytesseract.Output.DICT)

    found = False

    if '余' in data['text']:

            # 弹窗提醒
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        messagebox.showinfo("提示", "检测到 '余' 字✅！")

        found = True
        break

    if found:
        # 第五步：点击第二个按钮
        time.sleep(1)  # 稍微等一等
        second_location = pyautogui.locateCenterOnScreen(second_button_image, confidence=0.8)
        if second_location:
            print(f"找到第二个按钮，点击中... {second_location}")
            pyautogui.moveTo(second_location.x, second_location.y, duration=0.5)
            pyautogui.click()
        else:
            print("未找到第二个按钮，请检查截图。")

        print("程序执行完成，退出。")
        break

    else:
        print("未检测到 '余' 字，继续等待...")

    time.sleep(10) 
if '余' in data['text']:
    print("yes")


    for i, text in enumerate(data['text']):
        if '余' in text:
            print('yes')
            # 获取"余"的中心位置
            x = data['left'][i] + data['width'][i] // 2
            y = data['top'][i] + data['height'][i] // 2

            print(f"检测到 '余'，位置：({x}, {y})，点击它！")
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()

            # 弹窗提醒
            root = tk.Tk()
            root.withdraw()  # 隐藏主窗口
            messagebox.showinfo("提示", "检测到 '余' 字✅！")

            found = True
            break

for i, text in enumerate(data['text']):
    print(i, text)
    if '张' in text:
        print('yes')
        x = data['left'][i] + data['width'][i] // 2
        y = data['top'][i] + data['height'][i] // 2
        print(f"检测到 '余'，位置：({x}, {y})，点击它！")
        pyautogui.moveTo(x, y, duration=0.8)
        pyautogui.click()
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        messagebox.showinfo("提示", "检测到 '余' 字✅！")
        found = True
        break

if '余' in data['text']:
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("提示", "检测到'余'字✅！")
    found = True
