#! coding: UTF-8
import clr
import sys
from System import *
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *
# �t���p�X�����Ă��܂��Ă��邪
sys.path.append(r'C:\work\test\samples\IronPython\CS2\IronPythonCS')
# clr.AddReference("pyForm1")
import pyForm1
# from pyForm1 import *

ret = pyForm1.WindowsApplication1.Form1()
# class WindowsApplication10: # namespace
#     
#     @staticmethod
#     def RealEntryPoint():
#         Application.EnableVisualStyles()
#         Application.Run(WindowsApplication1.Form1())
# 
# if __name__ == "Program":
#     WindowsApplication10.RealEntryPoint();
