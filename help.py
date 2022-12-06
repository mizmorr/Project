#!/usr/bin/python
# import ctypes, time
# so = ctypes.cdll.LoadLibrary('./lib.so')

#     self.pushButton_6.released.connect(self.btnFirst_go)
#         self.pushButton_7.released.connect(self.btnSecond_go)

#     def btnFirst_go(self):
#             fs = so.firstSample 
#             num = self.spinBox_6.value()
#             fs.restype = ctypes.c_void_p
#             fs.argtypes=[ctypes.c_int]
#             fsout = fs(num)
#             self.progressBar_6.setValue(0)
#             time.sleep(0.025)
#             self.progressBar_6.setValue(100)
#             fbytes = ctypes.string_at(fsout)
#             fstring = fbytes.decode('utf-8')
#             time2,fstring = strconv(fstring)
#             if fstring=="no such k-core found\n":
#                  self.label_18.setText("")
#             else:
#                 self.label_18.setText(time2)
#             self.plainTextEdit_2.setPlainText(fstring)
    
#     def btnSecond_go(self):
#             fs = so.SecondSample 
#             num = self.spinBox_7.value()
#             fs.restype = ctypes.c_void_p
#             fs.argtypes=[ctypes.c_int]
#             fsout = fs(num)
#             self.progressBar_7.setValue(0)
#             time.sleep(0.025)
#             self.progressBar_7.setValue(100)
#             fbytes = ctypes.string_at(fsout)
#             fstring = fbytes.decode('utf-8')
#             time2,fstring = strconv(fstring)
#             if fstring=="no such k-core found\n":
#                  self.label_24.setText("")
#             else:
#                 self.label_24.setText(time2)
#             self.plainTextEdit_3.setPlainText(fstring)
import subprocess
subprocess.Popen(r'explorer /select,"/home"')
