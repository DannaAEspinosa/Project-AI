import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QSpacerItem, QSizePolicy, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
from main import ClassifierGenre  

#This class is the GUI of the music genre classifier
class GenreClassifierGUI(QWidget):
    #Constructor of the class
    def __init__(self):
        super().__init__()
        self.initUI()
        self.classifier = ClassifierGenre()

    #Method that initializes the GUI
    def initUI(self):
        self.setWindowTitle('Music Genre Classifier')
        self.setFixedSize(600, 240)  

        # Change the background of the window
        pixmap = QPixmap("img/fondo.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(pixmap.scaled(self.size(), Qt.IgnoreAspectRatio)))
        self.setPalette(palette)

        # Layout 
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # input label
        self.label = QLabel('Ingrese el nombre de una canción:')
        self.label.setFont(QFont('Arial', 12, QFont.Bold))
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)

        # Input field
        self.song_entry = QLineEdit()
        self.song_entry.setFont(QFont('Arial', 10))
        self.song_entry.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.song_entry)

        # predict button
        self.predict_button = QPushButton('Clasificar')
        self.predict_button.setFont(QFont('Arial', 12))
        self.predict_button.setStyleSheet("QPushButton { color: white; background-color: #333; border: 1px solid #555; text-align: center; }"
                                          "QPushButton:hover { background-color: #555; }")
        self.predict_button.clicked.connect(self.predict_genre)
        main_layout.addWidget(self.predict_button)

        # result label
        self.result_label = QLabel()
        self.result_label.setFont(QFont('Arial', 12, QFont.Bold))
        self.result_label.setStyleSheet("color: white;")
        self.result_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.result_label)

        # Spaces
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Set the layout
        self.setLayout(main_layout)

    #Method that predicts the genre of a song. Conect with the classifier (class)
    def predict_genre(self):
        song_name = self.song_entry.text().strip()
        if song_name:
            try:
                features_df = self.classifier.get_features(song_name)
                if features_df is not None:
                    processed_features = self.classifier.process_data(features_df)
                    genre_tree, prob_tree = self.classifier.tree_predict(processed_features)
                    genre_log, prob_log = self.classifier.logistic_predict(processed_features)

                    result_text = f"Árbol de decisión: {genre_tree[0]}, Probabilidad: {max(prob_tree[0]):.2f}\n"
                    result_text += f"Regresión logística: {genre_log[0]}, Probabilidad: {max(prob_log[0]):.2f}"
                    self.result_label.setText(result_text)
                else:
                    QMessageBox.information(self, "Resultado", "Canción no encontrada.")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese el nombre de una canción.")

#Main method. Execute the GUI
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GenreClassifierGUI()
    ex.show()
    sys.exit(app.exec_())