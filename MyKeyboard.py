# -*- coding: cp936 -*-
import pythoncom, win32con
import PyHook3 as pyHook
import win32api, threading

preKey = ''
timer = False  # ��ʱ��
isQuiet = False  # �Ƿ���ͣ�����ܣ�Ϊtrueʱ��ͣ������
isTimer = False  # �Ƿ��Ѵ��ڶ�ʱ����Ϊtrueʱ���ڶ�ʱ��


def func_timer():
    global preKey, timer, isTimer
    preKey = ''
    timer.cancel()
    isTimer = False


def onKeyboardEvent(event):
    global timer, isQuiet, isTimer, LmenuState, shiftState
    LmenuState = win32api.GetKeyState(18)
    shiftState = win32api.GetKeyState(16)
    if isTimer:
        timer.cancel()
    global preKey, currentKey
    currentKey = str(event.Key)
    # �����ǰ����Ϊalt/lshift/rshift,����ֵ�洢��prekey�����ΰ����������������������һ�ΰ���������
    if currentKey == 'Lmenu' or currentKey == 'Lshift' or currentKey == 'Rshift':
        preKey = str(event.Key)
        return True
    # �����ǰ����Ϊtab,�����prekey�ж�
    if currentKey == 'Tab':
        # (win32api.GetKeyState(20) == 1)��ʾ��д��������
        # prekeyΪ���¼���ֵ��˵���û���������ԭ�еĿ�ݼ�������������Ϣ�������μ���������������һ�ΰ�������
        # ����bug��Ϊ��ʹalt/shift��tab������ʹ�ã�δ�����¼��alt/shift��״̬,��ʱ������tab������������ݷ�ʽ
        # �޸����������ȡalt�İ���״̬��win32ap.GetKeyState��ȡ����ʹ��������������win32ap.GetKeyState(16)Ϊ1��
        # ��һ��shift��win32ap.GetKeyState(16)=0���ٰ�һ��shift win32ap.GetKeyState(16)�ֱ�Ϊ1
        if preKey == 'Lmenu' or preKey == 'Lshift' or preKey == 'Rshift':
            # ״̬Ϊ-128��-127,������ü����ڰ���״̬
            # ������ǰ״̬Ϊ0���򳤰�ʱ����ȡ����״ֵ̬Ϊ-127������ǰ״̬Ϊ0���򳤰�ʱ����ȡ����״ֵ̬Ϊ-128��
            if LmenuState == -128 or LmenuState == -127 or shiftState == -128 or shiftState == -127:
                return True
            else:
                preKey = 'Tab'
                return False
        #
        if preKey != 'Tab':
            preKey = str(event.Key)
            timer = threading.Timer(1, func_timer)
            timer.start()
            isTimer = True
            # ��������ܲ�Ϊ��ͣ������ֹ��������ִ��
            if not isQuiet:
                return False
    if preKey == 'Tab':
        if currentKey == 'Q':  # ����Q����ͣ��ݼ�����
            isQuiet = not isQuiet
            preKey = ''
            return False
        if not isQuiet:
            preKey = ''
            if currentKey == 'M':
                win32api.keybd_event(9, 0, 0, 0)
                win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
                return False
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
