# 🧠 OpenAI GPT-3.5 Turbo: First API Call

This script demonstrates a simple call to the OpenAI API using the `gpt-3.5-turbo` model. It interacts with the user via the command line, sends their input along with a system message to the model, and displays the assistant's response along with the total tokens used.

---

## 🔍 What the Script Does

- Loads your OpenAI API key from a `.env` file.
- Sends a fixed **system message** and user **input prompt** to OpenAI's GPT-3.5 Turbo model.
- Prints:
  - The assistant’s response.
  - Total token usage for the request.

---

## ⚙️ How to Run It

### 1. ✅ Install Dependencies

You’ll need:

- Python 3.7+
- `openai` (version ≥ 1.0.0)
- `python-dotenv`

Install with pip:

```bash
pip install openai python-dotenv
