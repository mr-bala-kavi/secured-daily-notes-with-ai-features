from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel, QListWidget, QMessageBox
)
from storage import save_note, load_note, list_notes
from ai_features import summarize, analyze_sentiment, extract_keywords

class NotesApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Encrypted Notes & Diary")
        self.setGeometry(100, 100, 600, 500)

        layout = QVBoxLayout()

        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter note title")
        layout.addWidget(self.title_input)

        self.note_input = QTextEdit(self)
        layout.addWidget(self.note_input)

        self.save_button = QPushButton("Save Note", self)
        self.save_button.clicked.connect(self.save_note)
        layout.addWidget(self.save_button)

        self.notes_list = QListWidget(self)
        self.notes_list.addItems(list_notes())
        self.notes_list.itemClicked.connect(self.load_note)
        layout.addWidget(self.notes_list)

        self.summarize_button = QPushButton("Summarize", self)
        self.summarize_button.clicked.connect(self.summarize_note)
        layout.addWidget(self.summarize_button)

        self.sentiment_button = QPushButton("Analyze Sentiment", self)
        self.sentiment_button.clicked.connect(self.sentiment_analysis)
        layout.addWidget(self.sentiment_button)

        self.keywords_button = QPushButton("Extract Keywords", self)
        self.keywords_button.clicked.connect(self.extract_keywords)
        layout.addWidget(self.keywords_button)

        self.result_label = QLabel("", self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def save_note(self):
        title = self.title_input.text()
        content = self.note_input.toPlainText()
        if title and content:
            save_note(title, content)
            self.notes_list.addItem(title)
            QMessageBox.information(self, "Success", "Note saved successfully!")
        else:
            QMessageBox.warning(self, "Error", "Title and content cannot be empty.")

    def load_note(self, item):
        title = item.text()
        content = load_note(title)
        if content:
            self.title_input.setText(title)
            self.note_input.setText(content)

    def summarize_note(self):
        content = self.note_input.toPlainText()
        if content:
            summary = summarize(content)
            self.result_label.setText("Summary: " + summary)

    def sentiment_analysis(self):
        content = self.note_input.toPlainText()
        if content:
            sentiment = analyze_sentiment(content)
            self.result_label.setText("Sentiment: " + sentiment)

    def extract_keywords(self):
        content = self.note_input.toPlainText()
        if content:
            keywords = extract_keywords(content)
            self.result_label.setText("Keywords: " + ", ".join(keywords))
