# -*- coding: cp936 -*-
import pythoncom, win32con
import PyHook3 as pyHook
import win32api, threading

preKey = ''
timer = False
isQuiet = False
isTimer = False


def func_timer():
    global preKey, timer, isTimer
    preKey = ''
    timer.cancel()
    isTimer = False


def onKeyboardEvent(event):
    global timer, isQuiet, isTimer
    if isTimer:
        timer.cancel()
    global preKey, currentKey
    currentKey = str(event.Key)
    if currentKey == 'Tab':
        # (win32api.GetKeyState(20) == 1)��ʾ��д��������
        if preKey == 'Lmenu' or preKey == 'Lshift' or preKey == 'Rshift':
            return True
        if str(preKey) != 'Tab':
            preKey = str(event.Key)
            timer = threading.Timer(1, func_timer)
            timer.start()
            isTimer = True
            if not isQuiet:
                return False
    if currentKey == 'Lmenu':
        return True
    if preKey == 'Tab':
        if currentKey == 'Q':  # ����Q����ͣ��ݼ�����
            isQuiet = not isQuiet
            preKey = ''
            return False
        if not isQuiet:
            preKey = ''
            # ����
            if currentKey == 'Oem_Comma':
                win32api.keybd_event(35, 0, 0, 0)
                win32api.keybd_event(event.KeyID, 0, 0, 0)
                win32api.keybd_event(event.KeyID, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(13, 0, 0, 0)
                # win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
                return False
                # win32api.keybd_event(event.KeyID, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # ���¼�λ
                # win32api.keybd_event(event.KeyID, 0, win32con.KEYEVENTF_KEYUP, 0)  # �ɿ���λ
            # �ֺ�
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
                win32api.keybd_event(32, 0, 0, 0)  # �ո�
                win32api.keybd_event(187, 0, 0, 0)
                win32api.keybd_event(187, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(32, 0, 0, 0)  # �ո�
                return False
            # +
            if currentKey == 'P':  # ;
                win32api.keybd_event(32, 0, 0, 0)  # �ո�
                win32api.keybd_event(16, 0, 0, 0)  # shift
                win32api.keybd_event(187, 0, 0, 0)  # "=+"
                win32api.keybd_event(187, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(32, 0, 0, 0)  # �ո�
                return False
            # :
            if currentKey == 'U':
                win32api.keybd_event(35, 0, 0, 0)  # ����End
                win32api.keybd_event(16, 0, 0, 0)  # ����Shift
                win32api.keybd_event(186, 0, 0, 0)  # ���¡�;:��
                win32api.keybd_event(186, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(13, 0, 0, 0)  # ���¡�Enter��
                return False
            # {}
            if currentKey == 'Oem_4':  # [
                win32api.keybd_event(35, 0, 0, 0)  # ����End
                win32api.keybd_event(32, 0, 0, 0)  # ����Space
                win32api.keybd_event(16, 0, 0, 0)  # ����Shift
                win32api.keybd_event(219, 0, 0, 0)  # ���¡�[{��
                win32api.keybd_event(219, 0, win32con.KEYEVENTF_KEYUP, 0)  # �ɿ�shift
                win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)  # �ɿ���[{��
                win32api.keybd_event(16, 0, 0, 0)
                win32api.keybd_event(221, 0, 0, 0)
                win32api.keybd_event(221, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(37, 0, 0, 0)
                win32api.keybd_event(13, 0, 0, 0)
                return False
            # ��txt
            if currentKey == 'T':
                win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', win32con.SW_SHOW)
                return False
            # # ��word
            # if currentKey == 'W':
            #     win32api.ShellExecute(0, 'open', 'word.exe', '', '', win32con.SW_SHOW)
            #     return False
            # ��Ĭ��������򿪰ٶ�
            if currentKey == 'G':
                win32api.ShellExecute(0, 'open', 'https://baidu.com', '', '', win32con.SW_SHOW)
                return False
            # ��Ĭ����������е�����
            if currentKey == 'Y':
                win32api.ShellExecute(0, 'open', 'http://fanyi.youdao.com/', '', '', win32con.SW_SHOW)
                return False
        if currentKey == 'F12':  # ����F12����ֹ
            win32api.PostQuitMessage()
            return False
    if currentKey != 'Tab':
        preKey = ''
    return True


def openEXE(name, bool):
    win32api.ShellExecute(0, 'open', name, '', '', bool)


if __name__ == "__main__":
    # ����hook���
    hm = pyHook.HookManager()

    # ��ؼ���
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()

    # ѭ����ȡ��Ϣ
    pythoncom.PumpMessages(10000)
