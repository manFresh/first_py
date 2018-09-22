import pyautogui
import time
print("按Ctrl + c 退出")

try:
    while True:
        x, y = pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + "Y: " + str(y).rjust(4)
        print("按Ctrl + c 退出")
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        time.sleep(10)
        pyautogui.click(941, 34, button='left')
        #print("我在左击 主人！")
        time.sleep(10)
except KeyboardInterrupt:
    print("\n完成。")

name = input("waiting....")
print(name)