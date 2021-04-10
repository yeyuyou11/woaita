import time
# pynput 第三方的库 需要单独安装 pip install pynput
from pynput.keyboard import Key, Controller as key_cl   #键盘的控制器
from pynput.mouse import Button,Controller as mouse_cl  #鼠标的控制器


# 键盘的控制函数
def keyboard_input(string):
    keyboard = key_cl()         # 获取键盘的权限
    keyboard.type(string)       # 设置数据的类型

# 鼠标的控制器
def mouse_click():
    mouse = mouse_cl()          # 获取鼠标的权限
    mouse.press(Button.left)    # 模拟鼠标左键的按下
    mouse.release(Button.left)  # 模拟鼠标左键的弹起

# 实现消息的发送函数
def send_message(number,string):
    print('穿')
    time.sleep(3)


    keyboard = key_cl()

    for i in range(number):
         keyboard_input(string)
         mouse_click()
         time.sleep(0.3)              # 括号里的数值是延迟时间
         keyboard.press(Key.enter)    # 模拟回车键的按下
         keyboard.release(Key.enter)  # 模拟回车的弹起


if __name__ == '__main__':
    send_message(10,'穿')
