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
         self.ciphertextLabel.setText(user_text)

   def plaintextBoxInputChanged(self):
      """
      Plaintext Text Box Text Changed Handler
      """
      user_text = self.plaintextBox.toPlainText()
      phrase = self.phraseBox.toPlainText()
      if len(user_text) == 0 or len(phrase) == 0:
         self.ciphertextLabel.setText("Ciphertext should appear here....")
      else:
         self.ciphertextLabel.setText(user_text)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()