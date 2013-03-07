using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

//IronPython用の名前空間
using IronPython.Hosting;

namespace IronPythonSample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        /// <summary>
        /// Globalsを利用した簡単なサンプル
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnSimple_Click(object sender, EventArgs e)
        {
            //IronPythoの実行エンジンを生成
            PythonEngine pe = new PythonEngine();
            //ボタンをMyButtonという名前でIronPythonのグローバル変数に登録
            pe.Globals.Add("MyButton", this.btnSimple);
            //「1st.py」という名前のスクリプトファイルを実行
            pe.ExecuteFile(@".\..\..\1st.py");
        }

        /// <summary>
        /// EvaluateAsを利用した簡単なサンプル
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnSimple2_Click(object sender, EventArgs e)
        {
            PythonEngine pe = new PythonEngine();
            //ボタンのHeightプロパティをIronPythonのグローバル変数に登録
            pe.Globals.Add("height", this.btnSimple2.Height);
            //「2nd.py」という名前のスクリプトファイルを実行
            pe.ExecuteFile(@".\..\..\2nd.py");
            //widthという変数の値をint型で取得
            this.btnSimple2.Width = pe.EvaluateAs<int>("width");
        }

        /// <summary>
        /// .NET Frameworkを利用するサンプル
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnColor_Click(object sender, EventArgs e)
        {
            //「3rd.py」という名前のスクリプトファイルを実行
            PythonEngine pe = new PythonEngine();
            pe.Globals.Add("MyForm", this);
            pe.ExecuteFile(@".\..\..\3rd.py");
        }


        /// <summary>
        /// RSSを取得するロジックをIronPythonに外出しする例
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnRss_Click(object sender, EventArgs e)
        {
          if (null != lstRss.DataSource)
          {
            lstRss.DataSource = null;
            this.Update();
          }
          else
          {
            //リストに設定するデータテーブルを作成
            DataTable table = new DataTable();
            DataColumn colTitle = new DataColumn("title", typeof(string));
            DataColumn colUrl = new DataColumn("url", typeof(string));
            DataColumn colDesc = new DataColumn("desc", typeof(string));
            table.Columns.AddRange(new DataColumn[] { colTitle, colUrl, colDesc });

            //「4th.py」という名前のスクリプトファイルを実行
            PythonEngine pe = new PythonEngine();
            pe.Globals.Add("table", table);
            try
            {
              pe.ExecuteFile(@".\..\..\4th.py");
            }
            catch (Exception ex)
            {
              MessageBox.Show(ex.Message, "エラー");
            }

            //スクリプトで設定されたtableをデータソースにセット
            this.lstRss.DataSource = table;
            this.lstRss.ValueMember = "url";
            this.lstRss.DisplayMember = "title";
          }
        }

        /// <summary>
        /// RSSをダブルクリックしたときの処理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void lstRss_DoubleClick(object sender, EventArgs e)
        {
            //ブラウザでページを表示
            System.Diagnostics.Process extProcess = new System.Diagnostics.Process();
            extProcess.StartInfo.FileName = lstRss.SelectedValue.ToString();
            extProcess.Start();
        }

        /// <summary>
        /// 「C#DLL関数をIPを通して呼ぶ （5th.py）」クリック
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button1_Click(object sender, EventArgs e)
        {
          try
          {
            int n = 0;
            int.TryParse(textBox1.Text, out n);

            // Pythonエンジン起動, Python空間のグローバル変数定義, pyファイル実行
            PythonEngine pe = new PythonEngine();
            pe.Globals.Add("value", n);
            pe.ExecuteFile(@".\..\..\6th.py");

            // pyファイル実行後, テキストボックスに反映
            //Form ff = pe.EvaluateAs<Form>("ret");
            //ff.ShowDialog(this);
            int nRet = pe.EvaluateAs<int>("ret");
            textBox1.Text = nRet.ToString();

            //Form ff = pe.EvaluateAs<Form>("f");
            //ff.ShowDialog(this);
          }
          catch (Exception ex)
          {
            System.Diagnostics.Trace.WriteLine(ex.Message);
          }
        }

        private void button3_Click(object sender, EventArgs e)
        {
          try
          {
            PythonEngine pe = new PythonEngine();
            pe.ExecuteFile(@".\..\..\pyProgram.py");

            // pyファイル実行後, 基底クラスで受けてdomodal
            Form ff = pe.EvaluateAs<Form>("ret");
            ff.ShowDialog(this);
          }
          catch (Exception ex)
          {
            System.Diagnostics.Trace.WriteLine(ex.Message);
          }
        }

        /// <summary>
        /// ロード関数
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Form1_Load(object sender, EventArgs e)
        {
          textBox1.Text = "";
        }

        /// <summary>
        /// 「空」ボタン
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button2_Click(object sender, EventArgs e)
        {
          textBox1.Text = "";
        }
    }

}