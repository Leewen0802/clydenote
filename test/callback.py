# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("輸入此PIN碼 '" + pin + "'在2分鐘內在您手機的LINE上")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='或掃描此QR'
        else:
            notice=''
        self.callback('【YTER登入】以下賴網址啟動,感謝您的使用 ' + notice + '打開此鏈接在2分鐘內在您手機的LINE上登陸\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
