from PyQt5.QtWidgets import *
from GrademainwindowVIEW import *


QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_submit.clicked.connect(lambda: self.score_finder())

    def score_finder(self) -> None:
        """
        This Function finds the score for the GUI as well as handles exceptions for inputs
        :return: Scores and Grades of Students to the GUI
        """
        try:
            numb_of_students: int = (self.line_numbstudents.text())
            scorez = self.input_grades.text()
            scores = scorez.split()
            #retrieving the highest score
            highest_score = max(scores)
            new_scores = []
            for item in scores:
                new_scores.append(float(item))

            score_average = (sum(new_scores) / len(new_scores))

            A = 90
            B = 80
            C = 70
            D = 60
            answers = []

            if score_average >= A:
                answers.append(f"Your average score is {score_average:.2f} Final Grade: A")
            elif score_average >= B:
                answers.append(f"Your average score is {score_average:.2f} Final Grade: B")
            elif score_average >= C:
                answers.append(f"Your average score is {score_average:.2f} Final Grade: C")
            elif score_average >= D:
                answers.append(f"Your average score is {score_average:.2f} Final Grade: D")
            else:
                answers.append(f"Your average score is {score_average:.2f} Final Grade:F")





            #for i in scores:
                #key = scores.index(i) + 1
                #if int(i) >= A:
                    #answers.append(f"Student {key} score is {i} and grade is A \n")
                #elif int(i) >= B:
                    #answers.append(f"Student {key} score is {i} and grade is B \n")
                #elif int(i) >= C:
                    #answers.append(f"Student {key} score is {i} and grade is C \n")
                #elif int(i) >= D:
                    #answers.append(f"Student {key} score is {i} and grade is D \n")
                #else:
                    #answers.append(f"Student {key} score is {i} and grade is F \n")


            #answerz = ''.join([str(elem) for elem in answers])
            answerz = ''.join([str(elem) for elem in answers])


            #self.label_output.setText(answerz)
            if len(scores) != int(self.line_numbstudents.text()):
                self.label_output.setText("please enter the correct amount of grades")
            else:
                self.label_output.setText(answerz)
                #self.label_output.setText(answerz)
            self.clear()
        except ValueError:   #handling any value errors
            self.label_output.setText("please enter inputs correctly")

    def clear(self) -> None: #clears the GUI
        """
        This function clears the inputs in the GUI
        """
        self.line_numbstudents.setText("")
        self.input_grades.setText("")