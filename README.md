# JARVIS
---

# Jarvis: Personal Desktop AI Assistant

Jarvis is a modern, customizable desktop assistant that combines voice and text interaction with a beautiful web-based interface. It leverages Python, Eel, JavaScript, and SQLite to provide a seamless assistant experience, including chatbot capabilities, custom command management, and database-driven automation.

---

## 🚀 Features

- **Voice & Text Chat:**  
  Interact with Jarvis using your voice (mic button) or by typing in the chatbox. Jarvis responds in both text and speech.

- **Custom Commands:**  
  Easily add or delete system commands (to launch apps), web commands (to open websites), and contacts (for calls/messages) via a user-friendly settings panel.

- **Chatbot Integration:**  
  Jarvis uses HugChat for conversational AI, providing smart and context-aware responses.

- **Modern Web UI:**  
  Responsive and stylish interface built with HTML, CSS, Bootstrap, and JavaScript. Includes chat panel, Siri-like wave animations, and a settings modal.

- **Database Management:**  
  All commands and contacts are stored in a local SQLite database (jarvis.db). The backend exposes database operations to the frontend using Eel.

- **Notifications & Feedback:**  
  Visual and audio feedback for user actions, including chat responses, system notifications, and animated effects.

- **Extensible:**  
  Easily add new features, commands, or integrations thanks to the modular Python and JavaScript codebase.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap, JavaScript, jQuery
- **Backend:** Python, Eel, SQLite
- **AI/Chat:** HugChat
- **Other:** Lottie animations, Textillate.js for text effects

---

## 📦 Folder Structure

```
jarvis/
├── engine/
│   ├── features.py
│   ├── db.py
│   └── ...
├── www/
│   ├── index.html
│   ├── controller.js
│   ├── main.js
│   ├── style.css
│   └── assets/
│       └── ...
├── jarvis.db
├── contacts.csv
└── ...
```

---

## ⚙️ How It Works

1. **Start Jarvis:**  
   Launch the Python app. The web UI opens in your browser.

2. **Interact:**  
   Type or speak your queries. Jarvis responds in the chat panel and with voice.

3. **Custom Actions:**  
   Use the settings button (gear icon) to add or remove system commands, web commands, and contacts.

4. **Database:**  
   All commands and contacts are managed in jarvis.db and can be updated from the frontend.

---

## 📝 Usage

- **Add/Remove Commands & Contacts:**  
  Open the settings panel (gear icon) and use the forms to add or delete entries.
- **Chat:**  
  Use the chatbox or mic button to interact with Jarvis.
- **Assistant Actions:**  
  Jarvis can open apps, launch websites, make calls, send messages, and answer questions.

---

## 📚 Requirements

- Python 3.x
- Node.js (for some advanced integrations, optional)
- All Python dependencies in `requirements.txt`
- Chrome/Edge browser recommended for best UI experience

---

## 🧑‍💻 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or add.

---

## 📄 License

This project is for educational and personal use.  
Feel free to fork and modify!

---

## 🙏 Acknowledgements

- [Eel](https://github.com/ChrisKnott/Eel)
- [HugChat](https://github.com/huggingface/hugchat)
- [Bootstrap](https://getbootstrap.com/)
- [LottieFiles](https://lottiefiles.com/)
- [Textillate.js](http://textillate.js.org/)

---

**Enjoy your personal Jarvis assistant!**




