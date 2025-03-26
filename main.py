from PyQt6.QtWidgets import QApplication
from gui import NotesApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotesApp()
    window.show()
    sys.exit(app.exec())
