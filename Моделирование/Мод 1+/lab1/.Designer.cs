namespace lab1
{
    partial class fmLab1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dgvData = new System.Windows.Forms.DataGridView();
            this.oneDigit = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.twoDigits = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.threeDigits = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.generated = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.btnGenerate = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.nudMin = new System.Windows.Forms.NumericUpDown();
            this.nudMax = new System.Windows.Forms.NumericUpDown();
            this.nudCount = new System.Windows.Forms.NumericUpDown();
            this.tbSeq = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.btnCalculate = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.lbEntropy = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.lbDiffEntropy = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dgvData)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudMin)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudMax)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudCount)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvData
            // 
            this.dgvData.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvData.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.oneDigit,
            this.twoDigits,
            this.threeDigits,
            this.generated});
            this.dgvData.Location = new System.Drawing.Point(24, 18);
            this.dgvData.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.dgvData.Name = "dgvData";
            this.dgvData.RowHeadersWidth = 62;
            this.dgvData.Size = new System.Drawing.Size(953, 317);
            this.dgvData.TabIndex = 0;
            this.dgvData.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgvData_CellContentClick);
            // 
            // oneDigit
            // 
            this.oneDigit.HeaderText = "0-9";
            this.oneDigit.MinimumWidth = 8;
            this.oneDigit.Name = "oneDigit";
            this.oneDigit.ReadOnly = true;
            this.oneDigit.Width = 125;
            // 
            // twoDigits
            // 
            this.twoDigits.HeaderText = "10-99";
            this.twoDigits.MinimumWidth = 8;
            this.twoDigits.Name = "twoDigits";
            this.twoDigits.ReadOnly = true;
            this.twoDigits.Width = 125;
            // 
            // threeDigits
            // 
            this.threeDigits.HeaderText = "100-999";
            this.threeDigits.MinimumWidth = 8;
            this.threeDigits.Name = "threeDigits";
            this.threeDigits.ReadOnly = true;
            this.threeDigits.Width = 125;
            // 
            // generated
            // 
            this.generated.HeaderText = "Сгенерированные";
            this.generated.MinimumWidth = 8;
            this.generated.Name = "generated";
            this.generated.ReadOnly = true;
            this.generated.Width = 125;
            // 
            // btnGenerate
            // 
            this.btnGenerate.Location = new System.Drawing.Point(24, 345);
            this.btnGenerate.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.btnGenerate.Name = "btnGenerate";
            this.btnGenerate.Size = new System.Drawing.Size(152, 35);
            this.btnGenerate.TabIndex = 2;
            this.btnGenerate.Text = "Сгенерировать";
            this.btnGenerate.UseVisualStyleBackColor = true;
            this.btnGenerate.Click += new System.EventHandler(this.btnGenerate_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(202, 352);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(82, 20);
            this.label1.TabIndex = 3;
            this.label1.Text = "Минимум:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(202, 389);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(89, 20);
            this.label2.TabIndex = 4;
            this.label2.Text = "Максимум:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(202, 428);
            this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(61, 20);
            this.label3.TabIndex = 5;
            this.label3.Text = "Чисел:";
            // 
            // nudMin
            // 
            this.nudMin.Location = new System.Drawing.Point(300, 348);
            this.nudMin.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.nudMin.Maximum = new decimal(new int[] {
            999,
            0,
            0,
            0});
            this.nudMin.Name = "nudMin";
            this.nudMin.Size = new System.Drawing.Size(180, 26);
            this.nudMin.TabIndex = 6;
            // 
            // nudMax
            // 
            this.nudMax.Location = new System.Drawing.Point(300, 389);
            this.nudMax.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.nudMax.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nudMax.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.nudMax.Name = "nudMax";
            this.nudMax.Size = new System.Drawing.Size(180, 26);
            this.nudMax.TabIndex = 7;
            this.nudMax.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // nudCount
            // 
            this.nudCount.Location = new System.Drawing.Point(300, 431);
            this.nudCount.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.nudCount.Maximum = new decimal(new int[] {
            10000,
            0,
            0,
            0});
            this.nudCount.Minimum = new decimal(new int[] {
            2,
            0,
            0,
            0});
            this.nudCount.Name = "nudCount";
            this.nudCount.Size = new System.Drawing.Size(180, 26);
            this.nudCount.TabIndex = 8;
            this.nudCount.Value = new decimal(new int[] {
            2,
            0,
            0,
            0});
            // 
            // tbSeq
            // 
            this.tbSeq.Location = new System.Drawing.Point(206, 505);
            this.tbSeq.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.tbSeq.Name = "tbSeq";
            this.tbSeq.Size = new System.Drawing.Size(366, 26);
            this.tbSeq.TabIndex = 9;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(24, 505);
            this.label4.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(180, 20);
            this.label4.TabIndex = 10;
            this.label4.Text = "Последовательность:";
            // 
            // btnCalculate
            // 
            this.btnCalculate.Location = new System.Drawing.Point(583, 497);
            this.btnCalculate.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.btnCalculate.Name = "btnCalculate";
            this.btnCalculate.Size = new System.Drawing.Size(112, 35);
            this.btnCalculate.TabIndex = 11;
            this.btnCalculate.Text = "Рассчитать энтропию";
            this.btnCalculate.UseVisualStyleBackColor = true;
            this.btnCalculate.Click += new System.EventHandler(this.btnCalculate_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(24, 551);
            this.label5.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(88, 20);
            this.label5.TabIndex = 12;
            this.label5.Text = "Энтропия:";
            // 
            // lbEntropy
            // 
            this.lbEntropy.AutoSize = true;
            this.lbEntropy.Location = new System.Drawing.Point(121, 551);
            this.lbEntropy.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lbEntropy.Name = "lbEntropy";
            this.lbEntropy.Size = new System.Drawing.Size(0, 20);
            this.lbEntropy.TabIndex = 13;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(300, 551);
            this.label6.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(171, 20);
            this.label6.TabIndex = 14;
            this.label6.Text = "Энтропия разностей:";
            // 
            // lbDiffEntropy
            // 
            this.lbDiffEntropy.AutoSize = true;
            this.lbDiffEntropy.Location = new System.Drawing.Point(470, 551);
            this.lbDiffEntropy.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lbDiffEntropy.Name = "lbDiffEntropy";
            this.lbDiffEntropy.Size = new System.Drawing.Size(0, 20);
            this.lbDiffEntropy.TabIndex = 15;
            // 
            // fmLab1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1132, 620);
            this.Controls.Add(this.lbDiffEntropy);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.lbEntropy);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.btnCalculate);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.tbSeq);
            this.Controls.Add(this.nudCount);
            this.Controls.Add(this.nudMax);
            this.Controls.Add(this.nudMin);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnGenerate);
            this.Controls.Add(this.dgvData);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "fmLab1";
            this.Text = "lab1";
            this.Load += new System.EventHandler(this.fmLab1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dgvData)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudMin)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudMax)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudCount)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dgvData;
        private System.Windows.Forms.Button btnGenerate;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.NumericUpDown nudMin;
        private System.Windows.Forms.NumericUpDown nudMax;
        private System.Windows.Forms.NumericUpDown nudCount;
        private System.Windows.Forms.TextBox tbSeq;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button btnCalculate;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label lbEntropy;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label lbDiffEntropy;
        private System.Windows.Forms.DataGridViewTextBoxColumn oneDigit;
        private System.Windows.Forms.DataGridViewTextBoxColumn twoDigits;
        private System.Windows.Forms.DataGridViewTextBoxColumn threeDigits;
        private System.Windows.Forms.DataGridViewTextBoxColumn generated;
    }
}

