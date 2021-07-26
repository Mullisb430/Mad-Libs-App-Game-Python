import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5 import uic
from madLibs import madLibDictionary, typesOfWords
import random

class MadLib(QMainWindow):
    def __init__(self):
        super(MadLib, self).__init__()
        loadUi('MadLibsTitleScreen.ui', self)
        self.playButton.clicked.connect(self.initialize)
        self.answers = []  
        self.story = ""
        self.wordTypes = []
        self.submissionLst = []
        self.lstOfWords = []
        self.GUIs = ["4wordScreen.ui", "8wordScreen.ui", "10wordScreen.ui", "11wordScreen.ui", "12wordScreen.ui", "14wordScreen.ui", "16wordScreen.ui", "17wordScreen.ui", "18wordScreen.ui", "19wordScreen.ui", "22wordScreen.ui"]

    def saveWords(self):
        count = 0
        while count <= len(self.submissionLst)-1:
            if len(self.submissionLst[count].text()) > 1:
                print(self.submissionLst[count].text())
                self.answers.append(str(self.submissionLst[count].text()))
            count = count + 1

        for word in self.answers:
            self.story = self.story.replace("@@", "|-" + word + "-|", 1)
        self.storyScreen()

    def storyScreen(self):
        loadUi('StoryScreen.ui', self)    
        self.storyLabel.setText(self.story)
        self.playAgainButton.clicked.connect(self.initialize)

    def initialize(self):

        self.answers = []
        self.lstOfWords = []
        self.wordTypes = []
        self.story = random.choice(madLibDictionary)
        self.lstOfWords.append(typesOfWords[madLibDictionary.index(self.story)])

        for item in self.lstOfWords[0]:
            self.wordTypes.append(str(item))
        print("\n" + [x for x in self.GUIs if str(len(self.wordTypes)) in x][0] + "\n")

        print("\n" + [x for x in self.GUIs if str(len(self.wordTypes)) in x][0] + "\n")
        loadUi([x for x in self.GUIs if str(len(self.wordTypes)) in x][0], self)
        self.submissionLst = [self.submission_1, self.submission_2, self.submission_3, self.submission_4, self.submission_5, self.submission_6, self.submission_7, self.submission_8, self.submission_9, self.submission_10, self.submission_11, self.submission_12, self.submission_13, self.submission_14, self.submission_15, self.submission_16, self.submission_17, self.submission_18, self.submission_19, self.submission_20, self.submission_21, self.submission_22]
        self.Labels = [self.typeOfWord_1, self.typeOfWord_2, self.typeOfWord_3, self.typeOfWord_4, self.typeOfWord_5, self.typeOfWord_6, self.typeOfWord_7, self.typeOfWord_8, self.typeOfWord_9, self.typeOfWord_10, self.typeOfWord_11, self.typeOfWord_12, self.typeOfWord_13, self.typeOfWord_14, self.typeOfWord_15, self.typeOfWord_16, self.typeOfWord_17, self.typeOfWord_18, self.typeOfWord_19, self.typeOfWord_20, self.typeOfWord_21, self.typeOfWord_22]

        for x in self.Labels[0:len(self.wordTypes)]:
            print(x)

        for x in self.submissionLst[0:len(self.wordTypes)]:
            print(x)

        count = 0
        while count <= len(self.wordTypes)-1:
            print(self.wordTypes[count])
            self.Labels[count].setText(self.wordTypes[count])
            count += 1

        self.playStory.clicked.connect(self.saveWords)

        self.anotherOne.clicked.connect(self.initialize)

app = QApplication(sys.argv)
window = MadLib()
window.show()
app.exec()


