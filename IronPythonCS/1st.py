# coding: utf-8

####################################
#最初の例(MyButtonをGlobalで共有)
####################################
if "IronPythonが動きました" == MyButton.Parent.Text:
	MyButton.Text = "Globalsの利用 （1st.py）"
	MyButton.Parent.Text = "IronPython"
elif "IronPython" == MyButton.Parent.Text:
	MyButton.Text = "スクリプトを実行しました"
	MyButton.Parent.Text = "IronPythonが動きました"
