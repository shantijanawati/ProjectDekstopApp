import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QStackedWidget, QFormLayout
)
from PyQt5.QtCore import Qt

class GradeCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Create stacked widget for pages
        self.stackedWidget = QStackedWidget()
        
        # Page 1: Penjelasan
        self.page1 = QWidget()
        self.initPage1()
        
        # Page 2: Pengisian Nilai
        self.page2 = QWidget()
        self.initPage2()
        
        # Page 3: Hasil
        self.page3 = QWidget()
        self.initPage3()
        
        # Add pages to stacked widget
        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)
        self.stackedWidget.addWidget(self.page3)
        
        # Set initial page
        self.stackedWidget.setCurrentIndex(0)
        
        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.stackedWidget)
        self.setLayout(mainLayout)
        
        self.setWindowTitle('Aplikasi Penghitung Nilai Siswa')
        self.setGeometry(300, 300, 600, 400)
        
    def initPage1(self):
        layout = QVBoxLayout()
        infoLabel = QLabel(
            "Aplikasi ini digunakan untuk menghitung kekurangan nilai siswa.\n"
            "Masukkan nilai untuk setiap mata pelajaran yang dipisahkan dengan spasi pada halaman berikut.\n"
            "Kemudian, lihat hasil perhitungan di halaman hasil.",
            self
        )
        layout.addWidget(infoLabel)
        
        nextButton = QPushButton('Lanjutkan', self)
        nextButton.clicked.connect(self.goToPage2)
        layout.addWidget(nextButton)
        
        self.page1.setLayout(layout)
    
    def initPage2(self):
        layout = QVBoxLayout()
        
        self.valuesInput = QLineEdit(self)
        self.valuesInput.setPlaceholderText("Masukkan nilai mata pelajaran (pisahkan dengan spasi)")
        
        self.submitButton = QPushButton('Submit', self)
        self.submitButton.clicked.connect(self.processValues)
        
        self.valuesLabel = QLabel('Nilai Anda', self)
        self.kkmInput = QLineEdit(self)
        self.kkmInput.setPlaceholderText("Masukkan nilai KKM")
        
        self.calculateButton = QPushButton('Hitung dan Lanjutkan', self)
        self.calculateButton.clicked.connect(self.goToPage3)
        
        layout.addWidget(self.valuesInput)
        layout.addWidget(self.submitButton)
        layout.addWidget(self.valuesLabel)
        layout.addWidget(QLabel('Nilai KKM:'))
        layout.addWidget(self.kkmInput)
        layout.addWidget(self.calculateButton)
        
        self.page2.setLayout(layout)
    
    def initPage3(self):
        layout = QVBoxLayout()
        
        self.resultLabel = QLabel('Rata-Rata Nilai:', self)
        self.resultOutput = QLineEdit(self)
        self.resultOutput.setReadOnly(True)
        
        self.missingLabel = QLabel('Kekurangan Nilai:', self)
        self.missingOutput = QLineEdit(self)
        self.missingOutput.setReadOnly(True)
        
        finishButton = QPushButton('Selesai', self)
        finishButton.clicked.connect(self.close)
        
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.resultOutput)
        layout.addWidget(self.missingLabel)
        layout.addWidget(self.missingOutput)
        layout.addWidget(finishButton)
        
        self.page3.setLayout(layout)
    
    def goToPage2(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def processValues(self):
        try:
            values_str = self.valuesInput.text()
            values = list(map(float, values_str.split()))
            self.valuesLabel.setText(f'Nilai yang dimasukkan: {values}')
            self.values = values
        except ValueError:
            self.valuesLabel.setText('Masukkan nilai yang valid!')
    
    def goToPage3(self):
        try:
            kkm = float(self.kkmInput.text())
            avg_value = sum(self.values) / len(self.values) if self.values else 0
            missing_value = max(0, kkm - avg_value)
            
            self.resultOutput.setText(f'{avg_value:.2f}')
            self.missingOutput.setText(f'{missing_value:.2f}')
            
        except ValueError:
            self.resultOutput.setText('Input tidak valid')
            self.missingOutput.setText('Input tidak valid')
        
        self.stackedWidget.setCurrentIndex(2)

def main():
    app = QApplication(sys.argv)
    ex = GradeCalculatorApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
