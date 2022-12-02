from PyQt5.QtWidgets import *
from Votemainwindow_View import *
voterID = []
score = {"UNO": 0 , "UNL": 0}


QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Add_button.clicked.connect(lambda: self.store())
        self.button_submit.clicked.connect(lambda: self.vote_counter())
        #self.button_submit.clicked.connect(lambda: self.clear())


    def store(self):
        try:
            NUID = int(self.input_collegeID.text())
            if self.No_button.isChecked() == True:
                self.label_output.setText("You Must Be A UNO OR UNL Student")

            elif type(NUID) == int and NUID not in voterID:
                self.label_output.setText("")
                voterID.append(NUID)
                if self.Uno_button.isChecked() == True:
                    score["UNO"] += 1
                elif self.UNL_button.isChecked() == True:
                    score["UNL"] += 1


                self.input_collegeID.setText("")



            elif NUID in voterID:
                self.input_collegeID.setText("")
                self.label_output.setText("This ID Has Already Voted")
            else:
                self.label_output.setText("")
            print(voterID)
            print(score)


        except ValueError:
            self.label_output.setText("Please Enter A Valid ID")


    def vote_counter(self):
        UNO = score["UNO"]
        UNL = score["UNL"]

        self.label_output.setText(f"Voting Results UNO: {UNO} UNL: {UNL}")

    def clear(self) -> None: #clears the GUI
        """
        This function clears the inputs in the GUI
        """
        self.label_output.setText("")
