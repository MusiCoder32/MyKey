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
        # ��Ĭ��������򿪰ٶ�
        if currentKey == 'G':
            win32api.ShellExecute(0, 'open', 'https://baidu.com', '', '', win32con.SW_SHOW)
            return False
        if currentKey == 'Y':
            win32api.ShellExecute(0, 'open', 'http://fanyi.youdao.com/', '', '', win32con.SW_SHOW)
            return False
        if currentKey == 'F12':  # ����F12����ֹ
            win32api.PostQuitMessage()
            return False
    preKey = ''
    return True


def openEXE(name, bool):
    win32api.ShellExecute(0, 'open', name, '', '', bool)


if __name__ == "__main__":
    print("�ҵļ��������� V1.0.0\n")
    print("��л����������������ʹ��֮ǰ���Ķ�����������֣�����˽�ù��߲�������")
    print("����һ�����ø��˿�ݼ���С���ߣ�����������ϲ���Ŀ�ݼ���")
    print("���磬�Ȱ�һ��tab�����ɿ����ٰ�һ�¡�[����,���൱�����ΰ���End,Space,Shift+[,Left,Enter(����Աר��)��")
    print("������ƽʱ�����ظ��Ĳ���Ũ��Ϊ���ΰ����������Լ�˱���ʱ�䡣")
    print("�ҷ���һЩ��ϼ������硰shift��+��+=�����ַ�ʽ�ó���+������һ���ķ�ʱ�������װ��������")
    print("Ϊ��������ı����ֿ�ݼ�ģʽ����Ϊ���ΰ����ķ�ʽ������һЩ����ָ��������ϼ���")
    print("���磬���ǿ��԰�һ��Tab�����ٰ�һ�¡�P����ͬ���������+����")
    print("�������趨�����п�ݼ�����Ϊ���ΰ���������һֱ������һ������")
    print("���磬�Ȱ�һ��tab�����ɿ����ٰ�һ��W��,������׵Ĵ�word,��ʼ���ı�д������")
    print("���磬�Ȱ�һ��tab�����ɿ����ٰ�һ��G��,��Ĭ��������򿪰ٶ�������")
    print("�ٱ��磬�Ȱ�һ��tab�����ɿ����ٰ�һ��Y��,��Ĭ����������е����롣\n")

    print("�������صĿ�����ѡ������������������βָ�����Tab��������ļ�����βָ�ĸ�����")
    print("��Ȼ����Ϊ�������������ʵ��ԭ��Tab�����ܣ�����Ҫ������Tab����")
    print("�������رձ�����һ��ֱ�ӹص��ô��ڣ����ǰ�Tab,F12(����Tab���ɿ���F12)��\n")
    print("Ŀǰ��Ʒֻ֧��windows����������������档�������������ܿ��������֣���Ϊ����档")
    print("��������뿴�������ڿ򣬿���ϵ���ǣ���ȡ�ù��ߵķ������")
    print("Ŀǰ�ݲ�֧���û��Զ����ݷ�ʽ��������Ҫ����ֱ����ϵ����ʦΪ�������ƣ�΢��w713422")
    print("����������֧������18859325023���ٴθ�л��")

    # ����hook���
    hm = pyHook.HookManager()

    # ��ؼ���
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()

    # ѭ����ȡ��Ϣ
    pythoncom.PumpMessages(10000)
