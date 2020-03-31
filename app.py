import os, sys, string
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from custom import *

class Ui(QtWidgets.QMainWindow):
   def __init__(self):
      super(Ui, self).__init__()
      uic.loadUi('vigenere_cipher.ui', self)

      # Key Phrase Box
      self.phraseBox = self.findChild(QtWidgets.QTextEdit, 'KeyPhraseBox')
      self.phraseBox.textChanged.connect(self.phraseBoxInputChanged)
      self.key = None

      # Plaintext Box
      self.plaintextBox = self.findChild(QtWidgets.QTextEdit, 'PlaintextBox')
      self.plaintextBox.textChanged.connect(self.plaintextBoxInputChanged)

      # Ciphertext Output Label
      self.ciphertextLabel = self.findChild(QtWidgets.QLabel, 'CiphertextLabel')

      # Upload Button
      self.uploadTxtFileButton = self.findChild(QtWidgets.QPushButton, 'UploadTxtFileButton')
      self.uploadTxtFileButton.clicked.connect(self.uploadHandler)

      # Download Button
      self.downloadTxtFileButton = self.findChild(QtWidgets.QPushButton, 'DownloadTxtFileButton')
      self.downloadTxtFileButton.clicked.connect(self.downloadHandler)

      # Show the app dialog
      self.show()
   
   # ############################# UI CONTROL METHODS #############################
   def phraseBoxInputChanged(self):
      """
      Phrase Box Input Changed Handler
      """
      user_text = self.plaintextBox.toPlainText()
      phrase = self.phraseBox.toPlainText()
      if len(user_text) == 0 or len(phrase) == 0:
         self.ciphertextLabel.setText("Ciphertext should appear here....")
      else:
         self.ciphertextLabel.setText(vigenereEncrypt(user_text, generateKey(user_text, phrase)))

   def plaintextBoxInputChanged(self):
      """
      Plaintext Text Box Text Changed Handler
      """
      user_text = self.plaintextBox.toPlainText()
      phrase = self.phraseBox.toPlainText()
      if len(user_text) == 0 or len(phrase) == 0:
         self.ciphertextLabel.setText("Ciphertext should appear here....")
      else:
         self.ciphertextLabel.setText(vigenereEncrypt(user_text, generateKey(user_text, phrase)))
   
   def uploadHandler(self):
      """
      Upload Button Handler
      """
      # Open file explorer
      currentDir = os.getcwd()
      # Open txt file and read contents
      fpath, filters = QFileDialog.getOpenFileName(self, 'Open file', currentDir, "Text files (*.txt)")
      # Put contents in the 'UserText' textbox
      file = open(fpath, 'r')
      self.plaintextBox.setText(str())
      for line in file:
         self.plaintextBox.setText(self.plaintextBox.toPlainText()+line)
      
      file.close()
   
   def downloadHandler(self):
      """
      Download Button Handler
      """
      # Write to a new file named 'ciphertext.txt'
      # in the current directory
      file = open(os.getcwd() + "\\ciphertext.txt", "w")
      file.write(self.ciphertextLabel.text())
      file.close()
      # Tell the user the download is complete
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)
      msg.setText("Your ciphertext is ready!")
      msg.setWindowTitle("Success!")
      msg.setStandardButtons(QMessageBox.Ok)
      msg.exec_()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()