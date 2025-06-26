# 🤖 Simple Chatbot using NLP (Python + NLTK)

This is a basic rule-based chatbot developed using Python and the NLTK library. It uses predefined intents and simple natural language processing techniques to interact with users in casual conversation.

---

## 🎯 Aim

Develop a simple chatbot that can engage in basic conversations with users.

---

## 📄 Description

This chatbot is powered by Natural Language Processing (NLP) using **Python** and **NLTK**. It reads user input, processes the text using tokenization and lemmatization, and finds the best matching intent based on word overlap. Responses are randomly selected from the matched intent's responses to simulate a human-like chat experience.

It can:
- Greet users
- Tell jokes or fun facts
- Share motivational quotes
- Answer questions about itself, AI, or tech
- Give basic career advice

---

## 🛠️ Technologies Used

- Python
- NLTK (Natural Language Toolkit)
- JSON for storing intents
- Basic NLP: tokenization, lemmatization

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/chatbot-project.git
cd chatbot-project
```

### 2️⃣ Install Required Packages
```bash
pip install nltk
```

> 📌 Note: On first run, NLTK will download required resources like punkt and wordnet. If not, add this to your script:
```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

### 3️⃣ Ensure Project Structure Looks Like This
```
chatbot-project/
├── chatbot.py
├── intents.json
└── README.md
```

### 4️⃣ Run the Chatbot
```bash
python chatbot.py
```

---

## 📦 Project Structure

```
chatbot-project/
├── chatbot.py          # Main script to run the chatbot
├── intents.json        # Predefined intents with patterns and responses
└── README.md           # Project documentation
```

---

## 🔮 Future Enhancements

- Integrate with a GUI (Tkinter) or Web App (Flask)
- Add contextual memory
- Improve matching using ML models (e.g., scikit-learn, spaCy)
- Add voice support or text-to-speech

---

## 📜 License

This project is open-source and free to use under the MIT License.
