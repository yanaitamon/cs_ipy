# coding: utf-8

####################################
#.NET Framework�̃I�u�W�F�N�g���g�p
####################################
#.NET Framework�̃N���X���C�u�������g���錾
import clr

#Color�N���X�𗘗p���đO�i�F��ύX
clr.AddReference("System.Drawing")
from System.Drawing import *
#if Color.White != MyForm.ForeColor:
#	MyForm.ForeColor = Color.White
#else:
#	MyForm.ForeColor = Color.Azure

#Random�N���X��Color�N���X�𗘗p���Ĕw�i�F��ύX
from System import *
random = Random()
MyForm.BackColor = Color.FromArgb(random.Next(255), random.Next(255), random.Next(255))
MyForm.ForeColor = Color.FromArgb(random.Next(255), random.Next(255), random.Next(255))
