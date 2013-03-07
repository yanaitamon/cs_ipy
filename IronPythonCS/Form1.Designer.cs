namespace IronPythonSample
{
    partial class Form1
    {
        /// <summary>
        /// 必要なデザイナ変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージ リソースが破棄される場合 true、破棄されない場合は false です。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナで生成されたコード

        /// <summary>
        /// デザイナ サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディタで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
          this.btnRss = new System.Windows.Forms.Button();
          this.btnSimple = new System.Windows.Forms.Button();
          this.btnColor = new System.Windows.Forms.Button();
          this.btnSimple2 = new System.Windows.Forms.Button();
          this.lstRss = new System.Windows.Forms.ListBox();
          this.button1 = new System.Windows.Forms.Button();
          this.textBox1 = new System.Windows.Forms.TextBox();
          this.button2 = new System.Windows.Forms.Button();
          this.button3 = new System.Windows.Forms.Button();
          this.SuspendLayout();
          // 
          // btnRss
          // 
          this.btnRss.Location = new System.Drawing.Point(12, 93);
          this.btnRss.Name = "btnRss";
          this.btnRss.Size = new System.Drawing.Size(185, 23);
          this.btnRss.TabIndex = 3;
          this.btnRss.Text = "RSSを取得 （4th.py）";
          this.btnRss.UseVisualStyleBackColor = true;
          this.btnRss.Click += new System.EventHandler(this.btnRss_Click);
          // 
          // btnSimple
          // 
          this.btnSimple.Location = new System.Drawing.Point(12, 12);
          this.btnSimple.Name = "btnSimple";
          this.btnSimple.Size = new System.Drawing.Size(185, 23);
          this.btnSimple.TabIndex = 0;
          this.btnSimple.Text = "Globalsの利用 （1st.py）";
          this.btnSimple.UseVisualStyleBackColor = true;
          this.btnSimple.Click += new System.EventHandler(this.btnSimple_Click);
          // 
          // btnColor
          // 
          this.btnColor.Location = new System.Drawing.Point(12, 66);
          this.btnColor.Name = "btnColor";
          this.btnColor.Size = new System.Drawing.Size(185, 23);
          this.btnColor.TabIndex = 2;
          this.btnColor.Text = ".NET Frameworkの利用 （3rd.py）";
          this.btnColor.UseVisualStyleBackColor = true;
          this.btnColor.Click += new System.EventHandler(this.btnColor_Click);
          // 
          // btnSimple2
          // 
          this.btnSimple2.Location = new System.Drawing.Point(12, 39);
          this.btnSimple2.Name = "btnSimple2";
          this.btnSimple2.Size = new System.Drawing.Size(185, 23);
          this.btnSimple2.TabIndex = 1;
          this.btnSimple2.Text = "EvaluateAsの利用 （2nd.py）";
          this.btnSimple2.UseVisualStyleBackColor = true;
          this.btnSimple2.Click += new System.EventHandler(this.btnSimple2_Click);
          // 
          // lstRss
          // 
          this.lstRss.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                      | System.Windows.Forms.AnchorStyles.Left)
                      | System.Windows.Forms.AnchorStyles.Right)));
          this.lstRss.FormattingEnabled = true;
          this.lstRss.ItemHeight = 12;
          this.lstRss.Location = new System.Drawing.Point(12, 124);
          this.lstRss.Name = "lstRss";
          this.lstRss.Size = new System.Drawing.Size(639, 268);
          this.lstRss.TabIndex = 4;
          this.lstRss.DoubleClick += new System.EventHandler(this.lstRss_DoubleClick);
          // 
          // button1
          // 
          this.button1.Location = new System.Drawing.Point(466, 39);
          this.button1.Name = "button1";
          this.button1.Size = new System.Drawing.Size(185, 23);
          this.button1.TabIndex = 5;
          this.button1.Text = "C#DLL関数をIPを通して呼ぶ （5th.py）";
          this.button1.UseVisualStyleBackColor = true;
          this.button1.Click += new System.EventHandler(this.button1_Click);
          // 
          // textBox1
          // 
          this.textBox1.Location = new System.Drawing.Point(466, 14);
          this.textBox1.Name = "textBox1";
          this.textBox1.Size = new System.Drawing.Size(149, 19);
          this.textBox1.TabIndex = 6;
          // 
          // button2
          // 
          this.button2.Location = new System.Drawing.Point(622, 12);
          this.button2.Name = "button2";
          this.button2.Size = new System.Drawing.Size(29, 23);
          this.button2.TabIndex = 7;
          this.button2.Text = "空";
          this.button2.UseVisualStyleBackColor = true;
          this.button2.Click += new System.EventHandler(this.button2_Click);
          // 
          // button3
          // 
          this.button3.Location = new System.Drawing.Point(466, 93);
          this.button3.Name = "button3";
          this.button3.Size = new System.Drawing.Size(185, 23);
          this.button3.TabIndex = 8;
          this.button3.Text = "ipyで作った画面を呼ぶ";
          this.button3.UseVisualStyleBackColor = true;
          this.button3.Click += new System.EventHandler(this.button3_Click);
          // 
          // Form1
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(663, 402);
          this.Controls.Add(this.button3);
          this.Controls.Add(this.button2);
          this.Controls.Add(this.textBox1);
          this.Controls.Add(this.button1);
          this.Controls.Add(this.lstRss);
          this.Controls.Add(this.btnSimple2);
          this.Controls.Add(this.btnColor);
          this.Controls.Add(this.btnSimple);
          this.Controls.Add(this.btnRss);
          this.Name = "Form1";
          this.Text = "IronPython";
          this.Load += new System.EventHandler(this.Form1_Load);
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnRss;
        private System.Windows.Forms.Button btnSimple;
        private System.Windows.Forms.Button btnColor;
        private System.Windows.Forms.Button btnSimple2;
        private System.Windows.Forms.ListBox lstRss;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
    }
}

