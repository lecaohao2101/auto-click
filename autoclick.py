import pyautogui
import time
import keyboard

print("Di chuyển chuột đến vị trí bạn muốn click trong vòng 5 giây...")
time.sleep(5)

x, y = pyautogui.position()

print(f"Đã lưu tọa độ: x = {x}, y = {y}")

delay = 0.000001

print("Nhấn ESC để dừng chương trình...")
while True:
    pyautogui.click(x, y)

    time.sleep(delay)

    if keyboard.is_pressed('esc'):
        print("Đã dừng chương trình.")
        break