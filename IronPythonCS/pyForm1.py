#! coding: UTF-8
import clr
import System
from System.Windows.Forms import *
from System.ComponentModel import *
clr.AddReference("System.Drawing")
from System.Drawing import *
from clr import *
class WindowsApplication1: # namespace
    
    class Form1(System.Windows.Forms.Form):
        """type(_button_N7) == System.Windows.Forms.Button, type(_button_N8) == System.Windows.Forms.Button, type(_button_N9) == System.Windows.Forms.Button, type(_button_N4) == System.Windows.Forms.Button, type(_button_N5) == System.Windows.Forms.Button, type(_button_N6) == System.Windows.Forms.Button, type(_button_N3) == System.Windows.Forms.Button, type(_button_N2) == System.Windows.Forms.Button, type(_button_N1) == System.Windows.Forms.Button, type(_button_Equal) == System.Windows.Forms.Button, type(_button_Neg) == System.Windows.Forms.Button, type(_button_N0) == System.Windows.Forms.Button, type(_button_Add) == System.Windows.Forms.Button, type(_button_Sub) == System.Windows.Forms.Button, type(_button_Mul) == System.Windows.Forms.Button, type(_button_Div) == System.Windows.Forms.Button, type(operation) == Dummy, type(lastkeyisoperator) == Dummy, type(_button_Clear) == System.Windows.Forms.Button, type(_button_AllClear) == System.Windows.Forms.Button, type(_label1) == System.Windows.Forms.Label, type(result) == Dummy"""
        __slots__ = ['_button_N7', '_button_N8', '_button_N9', '_button_N4', '_button_N5', '_button_N6', '_button_N3', '_button_N2', '_button_N1', '_button_Equal', '_button_Neg', '_button_N0', '_button_Add', '_button_Sub', '_button_Mul', '_button_Div', 'operation', 'lastkeyisoperator', '_button_Clear', '_button_AllClear', '_label1', 'result']
        def __init__(self):
            self.InitializeComponent()
            self.operation = '='
            self.lastkeyisoperator = False
            self.result = 0
        
        @accepts(Self(), bool)
        @returns(None)
        def Dispose(self, disposing):
            super(type(self), self).Dispose(disposing)
        
        @returns(None)
        def InitializeComponent(self):
            self._button_N0 = System.Windows.Forms.Button()
            self._button_N1 = System.Windows.Forms.Button()
            self._button_N2 = System.Windows.Forms.Button()
            self._button_N3 = System.Windows.Forms.Button()
            self._button_N4 = System.Windows.Forms.Button()
            self._button_N5 = System.Windows.Forms.Button()
            self._button_N6 = System.Windows.Forms.Button()
            self._button_N7 = System.Windows.Forms.Button()
            self._button_N8 = System.Windows.Forms.Button()
            self._button_N9 = System.Windows.Forms.Button()
            self._button_Equal = System.Windows.Forms.Button()
            self._button_Add = System.Windows.Forms.Button()
            self._button_Sub = System.Windows.Forms.Button()
            self._button_Mul = System.Windows.Forms.Button()
            self._button_Div = System.Windows.Forms.Button()
            self._button_Neg = System.Windows.Forms.Button()
            self._button_Clear = System.Windows.Forms.Button()
            self._button_AllClear = System.Windows.Forms.Button()
            self._label1 = System.Windows.Forms.Label()
            self.SuspendLayout()
            # 
            # button_N0
            # 
            self._button_N0.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_N0.Location = System.Drawing.Point(10, 176)
            self._button_N0.Name = 'button_N0'
            self._button_N0.Size = System.Drawing.Size(47, 29)
            self._button_N0.TabIndex = 10
            self._button_N0.TabStop = False
            self._button_N0.Text = '0'
            self._button_N0.UseVisualStyleBackColor = True
            self._button_N0.Click += self._button_N0_Click
            # 
            # button_N1
            # 
            self._button_N1.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_N1.Location = System.Drawing.Point(10, 141)
            self._button_N1.Name = 'button_N1'
            self._button_N1.Size = System.Drawing.Size(47, 29)
            self._button_N1.TabIndex = 7
            self._button_N1.TabStop = False
            self._button_N1.Text = '1'
            self._button_N1.UseVisualStyleBackColor = True
            self._button_N1.Click += self._button_N1_Click
            # 
            # button_N2
            # 
            self._button_N2.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_N2.Location = System.Drawing.Point(62, 141)
            self._button_N2.Name = 'button_N2'
            self._button_N2.Size = System.Drawing.Size(47, 29)
            self._button_N2.TabIndex = 8
            self._button_N2.TabStop = False
            self._button_N2.Text = '2'
            self._button_N2.UseVisualStyleBackColor = True
            self._button_N2.Click += self._button_N2_Click
            # 
            # button_N3
            # 
            self._button_N3.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_N3.Location = System.Drawing.Point(114, 141)
            self._button_N3.Name = 'button_N3'
            self._button_N3.Size = System.Drawing.Size(47, 29)
            self._button_N3.TabIndex = 9
            self._button_N3.TabStop = False
            self._button_N3.Text = '3'
            self._button_N3.UseVisualStyleBackColor = True
            self._button_N3.Click += self._button_N3_Click
            # 
            # button_N4
            # 
            self._button_N4.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_N4.Location = System.Drawing.Point(10, 106)
            self._button_N4.Name = 'button_N4'
            self._button_N4.Size = System.Drawing.Size(47, 29)
            self._button_N4.TabIndex = 4
            self._button_N4.TabStop = False
            self._button_N4.Text = '4'
            self._button_N4.UseVisualStyleBackColor = True
            self._button_N4.Click += self._button_N4_Click
            # 
            # button_N5
            # 
            self._button_N5.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_N5.Location = System.Drawing.Point(62, 106)
            self._button_N5.Name = 'button_N5'
            self._button_N5.Size = System.Drawing.Size(47, 29)
            self._button_N5.TabIndex = 5
            self._button_N5.TabStop = False
            self._button_N5.Text = '5'
            self._button_N5.UseVisualStyleBackColor = True
            self._button_N5.Click += self._button_N5_Click
            # 
            # button_N6
            # 
            self._button_N6.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_N6.Location = System.Drawing.Point(114, 106)
            self._button_N6.Name = 'button_N6'
            self._button_N6.Size = System.Drawing.Size(47, 29)
            self._button_N6.TabIndex = 6
            self._button_N6.TabStop = False
            self._button_N6.Text = '6'
            self._button_N6.UseVisualStyleBackColor = True
            self._button_N6.Click += self._button_N6_Click
            # 
            # button_N7
            # 
            self._button_N7.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_N7.Location = System.Drawing.Point(10, 71)
            self._button_N7.Name = 'button_N7'
            self._button_N7.Size = System.Drawing.Size(47, 29)
            self._button_N7.TabIndex = 1
            self._button_N7.TabStop = False
            self._button_N7.Text = '7'
            self._button_N7.UseVisualStyleBackColor = True
            self._button_N7.Click += self._button_N7_Click
            # 
            # button_N8
            # 
            self._button_N8.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_N8.Location = System.Drawing.Point(62, 71)
            self._button_N8.Name = 'button_N8'
            self._button_N8.Size = System.Drawing.Size(47, 29)
            self._button_N8.TabIndex = 2
            self._button_N8.TabStop = False
            self._button_N8.Text = '8'
            self._button_N8.UseVisualStyleBackColor = True
            self._button_N8.Click += self._button_N8_Click
            # 
            # button_N9
            # 
            self._button_N9.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_N9.Location = System.Drawing.Point(114, 71)
            self._button_N9.Name = 'button_N9'
            self._button_N9.Size = System.Drawing.Size(47, 29)
            self._button_N9.TabIndex = 3
            self._button_N9.TabStop = False
            self._button_N9.Text = '9'
            self._button_N9.UseVisualStyleBackColor = True
            self._button_N9.Click += self._button_N9_Click
            # 
            # button_Equal
            # 
            self._button_Equal.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_Equal.Location = System.Drawing.Point(114, 176)
            self._button_Equal.Name = 'button_Equal'
            self._button_Equal.Size = System.Drawing.Size(47, 29)
            self._button_Equal.TabIndex = 12
            self._button_Equal.TabStop = False
            self._button_Equal.Text = '='
            self._button_Equal.UseVisualStyleBackColor = True
            self._button_Equal.Click += self._button_Equal_Click
            # 
            # button_Add
            # 
            self._button_Add.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_Add.Location = System.Drawing.Point(166, 176)
            self._button_Add.Name = 'button_Add'
            self._button_Add.Size = System.Drawing.Size(47, 29)
            self._button_Add.TabIndex = 16
            self._button_Add.TabStop = False
            self._button_Add.Text = '+'
            self._button_Add.UseVisualStyleBackColor = True
            self._button_Add.Click += self._button_Add_Click
            # 
            # button_Sub
            # 
            self._button_Sub.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_Sub.Location = System.Drawing.Point(166, 141)
            self._button_Sub.Name = 'button_Sub'
            self._button_Sub.Size = System.Drawing.Size(47, 29)
            self._button_Sub.TabIndex = 15
            self._button_Sub.TabStop = False
            self._button_Sub.Text = '-'
            self._button_Sub.UseVisualStyleBackColor = True
            self._button_Sub.Click += self._button_Sub_Click
            # 
            # button_Mul
            # 
            self._button_Mul.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_Mul.Location = System.Drawing.Point(166, 106)
            self._button_Mul.Name = 'button_Mul'
            self._button_Mul.Size = System.Drawing.Size(47, 29)
            self._button_Mul.TabIndex = 14
            self._button_Mul.TabStop = False
            self._button_Mul.Text = '*'
            self._button_Mul.UseVisualStyleBackColor = True
            self._button_Mul.Click += self._button_Mul_Click
            # 
            # button_Div
            # 
            self._button_Div.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_Div.Location = System.Drawing.Point(166, 71)
            self._button_Div.Name = 'button_Div'
            self._button_Div.Size = System.Drawing.Size(47, 29)
            self._button_Div.TabIndex = 13
            self._button_Div.TabStop = False
            self._button_Div.Text = '/'
            self._button_Div.UseVisualStyleBackColor = True
            self._button_Div.Click += self._button_Div_Click
            # 
            # button_Neg
            # 
            self._button_Neg.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_Neg.Location = System.Drawing.Point(62, 176)
            self._button_Neg.Name = 'button_Neg'
            self._button_Neg.Size = System.Drawing.Size(47, 29)
            self._button_Neg.TabIndex = 11
            self._button_Neg.TabStop = False
            self._button_Neg.Text = '+/-'
            self._button_Neg.UseVisualStyleBackColor = True
            self._button_Neg.Click += self._button_Neg_Click
            # 
            # button_Clear
            # 
            self._button_Clear.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_Clear.ForeColor = System.Drawing.Color.Red
            self._button_Clear.Location = System.Drawing.Point(10, 36)
            self._button_Clear.Name = 'button_Clear'
            self._button_Clear.Size = System.Drawing.Size(99, 29)
            self._button_Clear.TabIndex = 17
            self._button_Clear.TabStop = False
            self._button_Clear.Text = 'C'
            self._button_Clear.UseVisualStyleBackColor = True
            self._button_Clear.Click += self._button_Clear_Click
            # 
            # button_AllClear
            # 
            self._button_AllClear.BackColor = System.Drawing.SystemColors.Control
            self._button_AllClear.Font = System.Drawing.Font('MS UI Gothic', 9.0, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 128)
            self._button_AllClear.ForeColor = System.Drawing.Color.Red
            self._button_AllClear.Location = System.Drawing.Point(114, 36)
            self._button_AllClear.Name = 'button_AllClear'
            self._button_AllClear.Size = System.Drawing.Size(99, 29)
            self._button_AllClear.TabIndex = 18
            self._button_AllClear.TabStop = False
            self._button_AllClear.Text = 'AC'
            self._button_AllClear.UseVisualStyleBackColor = True
            self._button_AllClear.Click += self._button_AllClear_Click
            # 
            # label1
            # 
            self._label1.BackColor = System.Drawing.SystemColors.Window
            self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
            self._label1.Cursor = System.Windows.Forms.Cursors.IBeam
            self._label1.Location = System.Drawing.Point(10, 11)
            self._label1.Name = 'label1'
            self._label1.Size = System.Drawing.Size(203, 19)
            self._label1.TabIndex = 1
            self._label1.Text = '0'
            self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
            self._label1.UseMnemonic = False
            # 
            # Form1
            # 
            self.ClientSize = System.Drawing.Size(222, 214)
            self.Controls.Add(self._label1)
            self.Controls.Add(self._button_AllClear)
            self.Controls.Add(self._button_Clear)
            self.Controls.Add(self._button_Add)
            self.Controls.Add(self._button_Sub)
            self.Controls.Add(self._button_Mul)
            self.Controls.Add(self._button_Div)
            self.Controls.Add(self._button_Equal)
            self.Controls.Add(self._button_Neg)
            self.Controls.Add(self._button_N0)
            self.Controls.Add(self._button_N3)
            self.Controls.Add(self._button_N2)
            self.Controls.Add(self._button_N1)
            self.Controls.Add(self._button_N6)
            self.Controls.Add(self._button_N5)
            self.Controls.Add(self._button_N4)
            self.Controls.Add(self._button_N9)
            self.Controls.Add(self._button_N8)
            self.Controls.Add(self._button_N7)
            self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle
            self.ImeMode = System.Windows.Forms.ImeMode.Disable
            self.MaximizeBox = False
            self.Name = 'Form1'
            self.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide
            self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
            self.Text = u'\u96FB\u5353'
            self.Shown += self._Form1_Shown
            self.KeyPress += self._Form1_KeyPress
            self.KeyDown += self._Form1_KeyDown
            self.ResumeLayout(False)
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_N0_Click(self, sender, e):
            self.OnNumericButtonClick('0')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_N1_Click(self, sender, e):
            self.OnNumericButtonClick('1')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_N2_Click(self, sender, e):
            self.OnNumericButtonClick('2')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_N3_Click(self, sender, e):
            self.OnNumericButtonClick('3')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_N4_Click(self, sender, e):
            self.OnNumericButtonClick('4')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_N5_Click(self, sender, e):
            self.OnNumericButtonClick('5')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_N6_Click(self, sender, e):
            self.OnNumericButtonClick('6')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_N7_Click(self, sender, e):
            self.OnNumericButtonClick('7')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_N8_Click(self, sender, e):
            self.OnNumericButtonClick('8')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_N9_Click(self, sender, e):
            self.OnNumericButtonClick('9')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_Neg_Click(self, sender, e):
            self._label1.Text = str(int(self._label1.Text) * -1)
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_Add_Click(self, sender, e):
            self.OnOperationButtonClick('+')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_Sub_Click(self, sender, e):
            self.OnOperationButtonClick('-')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_Mul_Click(self, sender, e):
            self.OnOperationButtonClick('*')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_Div_Click(self, sender, e):
            self.OnOperationButtonClick('/')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_Equal_Click(self, sender, e):
            self.OnOperationButtonClick('=')
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_Clear_Click(self, sender, e):
            self.OnClearClick()
        
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _button_AllClear_Click(self, sender, e):
            self.OnAllClearClick()
        
        @accepts(Self(), System.Object, System.Windows.Forms.KeyPressEventArgs)
        @returns(None)
        def _Form1_KeyPress(self, sender, e):
            if '0' <= e.KeyChar <= '9':
                self.OnNumericButtonClick(e.KeyChar)
            elif str(e.KeyChar) in '+-*/':
                self.OnOperationButtonClick(str(e.KeyChar))
            elif e.KeyChar == '\r':
                self.OnOperationButtonClick('=')
            elif e.KeyChar == '\b':
                self.OnBackClick()
            e.Handled = True
        
        def OnNumericButtonClick(self, number):
            if self.lastkeyisoperator:
                self.lastkeyisoperator = False
                self._label1.Text = ''
            if self._label1.Text == '0':
                self._label1.Text = ''
            if len(self._label1.Text) < 30:
                self._label1.Text += number
        
        def OnOperationButtonClick(self, operator):
            if not self.lastkeyisoperator:
                entry = int(self._label1.Text)
                self.Calcuration(entry, self.operation)
                text = str(self.result)
                if len(text) > 30:                  # Overflow
                    text = '9' * 30
                self._label1.Text = text
            self.operation = operator
            self.lastkeyisoperator = True
        
        def Calcuration(self, entry, op):
            if op == '+':
	            self.result += entry
            elif op == '-':
	            self.result -= entry
            elif op == '*':
	            self.result *= entry
            elif op == '/':
	            self.result /= entry
            elif op == '=':
	            self.result = entry
	    
        def OnBackClick(self):
            if not self.lastkeyisoperator:
	            self._label1.Text = self._label1.Text[0:-1]
	            if len(self._label1.Text) == 0:
	                self._label1.Text = '0'
	    
        def OnClearClick(self):
            self._label1.Text = '0'
	    
        def OnAllClearClick(self):
            self.operation = '='
            self.lastkeyisoperator = False
            self.result = 0
            self._label1.Text = '0'
	    
        @accepts(Self(), System.Object, System.EventArgs)
        @returns(None)
        def _Form1_Shown(self, sender, e):
            # コンストラクタからSetStyle()を呼ぶとフォームデザイナに怒られるので
            # ここで設定している。
            self._button_N0.SetStyle(ControlStyles.Selectable, False)
            self._button_N1.SetStyle(ControlStyles.Selectable, False)
            self._button_N2.SetStyle(ControlStyles.Selectable, False)
            self._button_N3.SetStyle(ControlStyles.Selectable, False)
            self._button_N4.SetStyle(ControlStyles.Selectable, False)
            self._button_N5.SetStyle(ControlStyles.Selectable, False)
            self._button_N6.SetStyle(ControlStyles.Selectable, False)
            self._button_N7.SetStyle(ControlStyles.Selectable, False)
            self._button_N8.SetStyle(ControlStyles.Selectable, False)
            self._button_N9.SetStyle(ControlStyles.Selectable, False)
            self._button_Equal.SetStyle(ControlStyles.Selectable, False)
            self._button_Neg.SetStyle(ControlStyles.Selectable, False)
            self._button_Add.SetStyle(ControlStyles.Selectable, False)
            self._button_Sub.SetStyle(ControlStyles.Selectable, False)
            self._button_Mul.SetStyle(ControlStyles.Selectable, False)
            self._button_Div.SetStyle(ControlStyles.Selectable, False)
            self._button_Clear.SetStyle(ControlStyles.Selectable, False)
            self._button_AllClear.SetStyle(ControlStyles.Selectable, False)
        
        @accepts(Self(), System.Object, System.Windows.Forms.KeyEventArgs)
        @returns(None)
        def _Form1_KeyDown(self, sender, e):
            if e.Modifiers == Keys.Control:
                if e.KeyCode == Keys.C:
                    e.Handled = True
                    entry = self._label1.Text
                    Clipboard.SetText(entry)
                elif e.KeyCode == Keys.V:
                    e.Handled = True
                    if Clipboard.ContainsText():
                        text = Clipboard.GetText()
                        try:
                            entry = str(int(text))
                            if len(entry) > 30:
                                entry = '9' * 30
                            self._label1.Text = entry
                            self.lastkeyisoperator = False
                        except ValueError:
                            pass
                        
                    
                
            
        
    
