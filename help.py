import ctypes, time
so = ctypes.cdll.LoadLibrary('./lib.so')

        self.pushButton_6.released.connect(self.btn_go)
    def btn_go(self):
            fs = so.firstSample 
            fs = so.firstSample
            num = self.spinBox_6.value()
            fs.restype = ctypes.c_void_p
            fs.argtypes=[ctypes.c_int]
            fsout = fs(num)
            self.progressBar_6.setValue(0)
            time.sleep(0.025)
            self.progressBar_6.setValue(100)
            fbytes = ctypes.string_at(fsout)
            fstring = fbytes.decode('utf-8')
            farr  = fstring.split('\n')
            list.reverse(farr)
            time2 = list.pop(farr)
            list.reverse(farr)
            fstring = '\n'.join(farr) 
            self.label_24.setText(time2)
            self.plainTextEdit_2.setPlainText(fstring)