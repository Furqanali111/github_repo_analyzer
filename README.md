# GitHub Repo Analyzer Tool (AI-Powered 🚀)

## 📌 Project Overview

This project is a Python-based AI tool that takes a **GitHub repository link** as input and generates:

- 📄 **A new, custom README.md**
- 📑 **A PDF summary report**
- 🗂️ **A technical walkthrough** (explaining the folder structure, key files, and how to run the project)

The tool uses **local Large Language Models (LLMs)** such as **DeepSeek Coder** running via **Ollama**, ensuring **zero API costs** and **full data privacy**.

---

## ✅ Features

- Clone any public GitHub repository
- Parse project folder structure and important source files
- Generate:
  - AI-written README.md (ignores existing README)
  - PDF summary
  - Technical walkthrough
- Works entirely offline (with local LLM like DeepSeek)
- Optional web UI (coming later)

---

## ✅ How It Works

1. Clone the target GitHub repo into a temp folder.
2. Parse file structure and sample important files.
3. Generate text outputs by sending prompts to your **local DeepSeek LLM via Ollama**.
4. Save generated outputs (Markdown, PDF, Text files) into `/output/` folder.

---

## ✅ Setup Instructions

### 1. Clone this Analyzer Tool

```bash
git clone https://github.com/yourusername/github_repo_analyzer.git
cd github_repo_analyzer
```

### 2. Create Virtual Environment & Install Python Packages

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set Up Ollama + DeepSeek Locally

```bash
curl https://ollama.com/install.sh | sh
ollama pull deepseek-coder:7b
ollama serve
```

---

## ✅ Running the Tool

```bash
ollama serve
```
```bash

python main.py --repo=https://github.com/someuser/somerepo --option=readme
```

Available `--option` values:

- `readme`
- `summary`
- `walkthrough`

---

## ✅ Future Plans

- Add web UI with Flask or FastAPI
- Allow summarizing private repos using GitHub API token
- Add support for multiple LLM backends (DeepSeek, LLaMA, etc.)

---

