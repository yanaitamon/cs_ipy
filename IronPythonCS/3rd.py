# coding: utf-8

####################################
#.NET Frameworkのオブジェクトを使用
####################################
#.NET Frameworkのクラスライブラリを使う宣言
import clr

#Colorクラスを利用して前景色を変更
clr.AddReference("System.Drawing")
from System.Drawing import *
#if Color.White != MyForm.ForeColor:
#	MyForm.ForeColor = Color.White
#else:
#	MyForm.ForeColor = Color.Azure

#RandomクラスとColorクラスを利用して背景色を変更
from System import *
random = Random()
MyForm.BackColor = Color.FromArgb(random.Next(255), random.Next(255), random.Next(255))
MyForm.ForeColor = Color.FromArgb(random.Next(255), random.Next(255), random.Next(255))
