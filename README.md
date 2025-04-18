---

# 🔒 Encrypted Notes & Diary with AI ✨

A secure, AI-powered diary built with Python and PyQt that encrypts your notes and enhances them with **Summarization**, **Sentiment Analysis**, and **Keyword Extraction** features.

---

## 🌟 Features

- 🛡️ **AES Encryption** — Your notes stay safe and private.
- 📝 **Summarization** — Get short summaries of long entries.
- 😊 **Sentiment Analysis** — Understand the emotional tone of your writing.
- 🔍 **Keyword Extraction** — Highlight important topics in your notes.
- 🎨 **Modern PyQt GUI** — Clean and responsive user interface.

---

## 📦 Installation

### ✅ Prerequisites

- Python **3.8 to 3.11** (Tested on Python 3.10)
- Internet connection (to download required NLP models)

### 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/mr-bala-kavi/secured-daily-notes-with-ai-features.git
   cd encrypted-diary
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy language model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

---

## 🛠 Tech Stack & Dependencies

| Module         | Purpose                                 |
|----------------|------------------------------------------|
| `PyQt6`        | GUI framework                            |
| `textblob`     | Sentiment analysis                       |
| `nltk`         | Natural language processing & summarizing|
| `pycryptodome` | AES encryption                           |
| `spaCy`        | Keyword extraction                       |

---

## 🤖 AI Capabilities

| Feature              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Summarization**     | Uses `nltk` to condense long notes into short summaries                    |
| **Sentiment Analysis**| Uses `textblob` to evaluate emotional tone (positive, negative, neutral)   |
| **Keyword Extraction**| Uses `spaCy` to detect and extract key phrases from your notes              |

---

## 🚀 How to Use

1. 🧑‍💻 Launch the app: `python main.py`  
2. 🗒️ Write your diary entry and click **"Encrypt & Save"**  
3. 🤖 Click on:
   - **Summarize** for a quick overview
   - **Analyze Sentiment** for emotional insight
   - **Extract Keywords** to get key points  
4. 🔓 Access and decrypt saved notes anytime securely.

---

## 🔮 Upcoming Features

- ☁️ **Cloud backup** for your encrypted notes  
- 🎤 **Voice-to-Text input** support  
- 📎 **Image and file attachments**

---

## 🧑‍💻 Author

**Mr-Bala-Kavi**  
📧 [balakavi64@gmail.com](mailto:balakavi64@gmail.com)  
🌐 [GitHub Profile](https://github.com/mr-bala-kavi)

---