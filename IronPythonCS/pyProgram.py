#! coding: UTF-8
import clr
import sys
from System import *
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *
# ƒtƒ‹ƒpƒX‚ð“ü‚ê‚Ä‚µ‚Ü‚Á‚Ä‚¢‚é‚ª
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
