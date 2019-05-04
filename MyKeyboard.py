# -*- coding: cp936 -*-
import pythoncom, win32con
import PyHook3 as pyHook
import win32api
import os
import threading

preKey = ""


def onKeyboardEvent(event):
    global preKey, currentKey
    currentKey = str(event.Key)
    if currentKey == 'Tab':
        if preKey == 'Lmenu':
            return True
        if str(preKey) != 'Tab':
            preKey = str(event.Key)
            return False
        else:
            preKey = ''
    if currentKey == 'Lmenu':
        preKey = str(event.Key)
        return True
    if preKey == 'Tab':
        preKey = ''
        if currentKey == 'Oem_Comma':
            win32api.keybd_event(35, 0, 0, 0)
            win32api.keybd_event(event.KeyID, 0, 0, 0)
            win32api.keybd_event(event.KeyID, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(13, 0, 0, 0)
            # win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
            return False
            # win32api.keybd_event(event.KeyID, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # 按下键位
            # win32api.keybd_event(event.KeyID, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开键位
        # 分号
        if currentKey == 'Oem_1':
            win32api.keybd_event(35, 0, 0, 0)
            win32api.keybd_event(event.KeyID, 0, 0, 0)
            win32api.keybd_event(event.KeyID, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(13, 0, 0, 0)
            return False
        # Left
        if currentKey == 'J':
            win32api.keybd_event(37, 0, 0, 0)
            return False
        # Up
        if currentKey == 'I':
            win32api.keybd_event(38, 0, 0, 0)
            return False
        # Right
        if currentKey == 'L':
            win32api.keybd_event(39, 0, 0, 0)
            return False
        # Down
        if currentKey == 'K':
            win32api.keybd_event(40, 0, 0, 0)
            return False
        # =
        if currentKey == 'O':
            win32api.keybd_event(32, 0, 0, 0)  # 空格
            win32api.keybd_event(187, 0, 0, 0)
            win32api.keybd_event(187, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(32, 0, 0, 0)  # 空格
            return False
        # +
        if currentKey == 'P':  # ;
            win32api.keybd_event(32, 0, 0, 0)  # 空格
            win32api.keybd_event(16, 0, 0, 0)  # shift
            win32api.keybd_event(187, 0, 0, 0)  # "=+"
            win32api.keybd_event(187, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(32, 0, 0, 0)  # 空格
            return False
        # :
        if currentKey == 'U':
            win32api.keybd_event(35, 0, 0, 0)  # 按下End
            win32api.keybd_event(16, 0, 0, 0)  # 按下Shift
            win32api.keybd_event(186, 0, 0, 0)  # 按下“;:”
            win32api.keybd_event(186, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(13, 0, 0, 0)  # 按下“Enter”
            return False
        # {}
        if currentKey == 'Oem_4':  # [
            win32api.keybd_event(35, 0, 0, 0)  # 按下End
            win32api.keybd_event(32, 0, 0, 0)  # 按下Space
            win32api.keybd_event(16, 0, 0, 0)  # 按下Shift
            win32api.keybd_event(219, 0, 0, 0)  # 按下“[{”
            win32api.keybd_event(219, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开shift
            win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开“[{”
            win32api.keybd_event(16, 0, 0, 0)
            win32api.keybd_event(221, 0, 0, 0)
            win32api.keybd_event(221, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(37, 0, 0, 0)
            win32api.keybd_event(13, 0, 0, 0)
            return False
        # 打开txt
        if currentKey == 'T':
            win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', win32con.SW_SHOW)
            return False
        # 以默认浏览器打开百度
        if currentKey == 'G':
            win32api.ShellExecute(0, 'open', 'https://baidu.com', '', '', win32con.SW_SHOW)
            return False
        if currentKey == 'Y':
            win32api.ShellExecute(0, 'open', 'http://fanyi.youdao.com/', '', '', win32con.SW_SHOW)
            return False
        if currentKey == 'F12':  # 按下F12后终止
            win32api.PostQuitMessage()
            return False
    preKey = ''
    return True


def openEXE(name, bool):
    win32api.ShellExecute(0, 'open', name, '', '', bool)


if __name__ == "__main__":
    print("我的键盘我做主 V1.0.0\n")
    print("感谢与您的相遇！在您使用之前，阅读下面这段文字，你会了解该工具并爱上它")
    print("这是一个设置个人快捷键的小工具，可以设置你喜欢的快捷键。")
    print("比如，先按一下tab键并松开，再按一下“[”键,便相当于依次按下End,Space,Shift+[,Left,Enter(程序员专用)，")
    print("将我们平时不断重复的操作浓缩为两次按键，极大节约了宝贵时间。")
    print("我发现一些组合键，比如“shift”+“+=”这种方式敲出“+”，是一件耗费时间且容易按错操作。")
    print("为此我们想改变这种快捷键模式，改为依次按键的方式并启用一些离手指更近的组合键。")
    print("比如，我们可以按一下Tab键，再按一下“P”，同样能输出“+”。")
    print("故以下设定的所有快捷键，均为依次按键，无须一直按着上一个键。")
    print("比如，先按一下tab键并松开，再按一下W键,便可轻易的打开word,开始您的编写工作。")
    print("比如，先按一下tab键并松开，再按一下G键,用默认浏览器打开百度搜索。")
    print("再比如，先按一下tab键并松开，再按一下Y键,用默认浏览器打开有道翻译。\n")

    print("经过慎重的考虑与选择，我们启用了离左手尾指最近的Tab键，极大的减轻了尾指的负担。")
    print("当然，作为牺牲，如果你想实现原先Tab键功能，则需要按两次Tab键。")
    print("如果你想关闭本程序，一是直接关掉该窗口；二是按Tab,F12(按下Tab，松开后按F12)。\n")
    print("目前产品只支持windows，有桌面版与非桌面版。如果启动程序后能看到该文字，则为桌面版。")
    print("如果您不想看见这个大黑框，可联系我们，领取该工具的非桌面版")
    print("目前暂不支持用户自定义快捷方式，如有需要，可直接联系工程师为您量身定制，微信w713422")
    print("打赏渠道，支付宝：18859325023，再次感谢！")

    # 创建hook句柄
    hm = pyHook.HookManager()

    # 监控键盘
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()

    # 循环获取消息
    pythoncom.PumpMessages(10000)
