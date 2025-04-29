<div align="center">

# 🤖 Gemini AI Chatbot

<p>
  <img src="https://img.shields.io/badge/Gemini%201.5-Flash-blue?style=for-the-badge&logo=google&logoColor=white" alt="Gemini 1.5" />
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License: MIT" />
</p>

<br>

<p>
  <a href="#-demo">Demo</a> •
  <a href="#-key-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-usage">Usage</a> •
  <a href="#%EF%B8%8F-security">Security</a> •
  <a href="#-contribute">Contribute</a> •
  <a href="#-license">License</a>
</p>

<br>

<p><strong>🎬 Interactive AI Chat Demo</strong><br>
Experience natural conversations with Google's Gemini 1.5 Flash model!</p>

<br>

<em>An interactive AI chatbot powered by Google's revolutionary Gemini 1.5 Flash LLM and Streamlit!</em>

</div>

---

## ✨ Overview

Engage in natural, flowing conversations with one of the world's most advanced AI systems. Built with Streamlit and Google's Gemini 1.5 Flash model, this chatbot provides a seamless, intuitive interface for asking questions, generating content, and exploring the capabilities of modern AI.

## 🚀 Key Features

<table>
  <tr>
    <td align="center"><h3>💬</h3></td>
    <td><b>Real-time Responses</b><br>Watch the AI generate responses character by character</td>
    <td align="center"><h3>🧠</h3></td>
    <td><b>Advanced AI</b><br>Powered by Google's cutting-edge Gemini 1.5 Flash model</td>
  </tr>
  <tr>
    <td align="center"><h3>🔒</h3></td>
    <td><b>Secure by Design</b><br>Enhanced API key protection with zero hardcoded secrets</td>
    <td align="center"><h3>📜</h3></td>
    <td><b>Conversation History</b><br>Review your entire chat session at a glance</td>
  </tr>
</table>

## 🏃‍♂️ Quick Start

<details open>
<summary><b>Installation Steps</b></summary>
<br>

```bash
# Clone this repository
git clone https://github.com/yourusername/gemini-chatbot.git
cd gemini-chatbot

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up API key (follow the prompts)
python create_env.py

# Launch the application
streamlit run qachat.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

</details>

<details>
<summary><b>Prerequisites</b></summary>
<br>

- Python 3.8 or higher
- Google API key ([Get one here](https://aistudio.google.com/app/apikey))
- Internet connection (required for API calls)

</details>

## 💡 Usage

<ol>
  <li>🔠 <b>Type your question</b> in the input field</li>
  <li>🖱️ <b>Click "Ask the question"</b> button</li>
  <li>⏱️ <b>Watch</b> as the AI responds in real-time</li>
  <li>📋 <b>Review</b> your conversation history below</li>
  <li>🔄 <b>Ask follow-up questions</b> to continue the conversation</li>
</ol>

## 🛡️ Security

We've implemented comprehensive security measures to protect your API key:

<details>
<summary><b>Security Features</b></summary>
<br>

- **Zero Hardcoded Secrets**: No API keys in the code
- **Environment Variables**: Keys stored in `.env` file
- **GitIgnore Protection**: Sensitive files excluded
- **Secure Input**: Hidden password-style key entry
- **Helpful Errors**: Clear messages for missing keys

See [API_SECURITY.md](API_SECURITY.md) for detailed security information.

</details>

## 📁 Project Structure

```
gemini-chatbot/
├── 🐍 qachat.py           # Main application
├── 📝 requirements.txt    # Dependencies
├── 🔑 create_env.py       # Secure API key setup
├── 📋 API_SECURITY.md     # Security guidelines
├── 📄 LICENSE             # MIT license
└── 📘 README.md           # This file
```

## 🤝 Contribute

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin amazing-feature`)
5. Open a Pull Request

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Created with ❤️ by Sourya Sarkar

<p>
  <a href="https://github.com/yourusername"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
</p>

<p>
  ⭐ <b>Star this repo if you found it useful!</b> ⭐
</p>

</div> 