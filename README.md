# Generative Code Refactoring and Vulnerability Detection Assistant

This tool analyzes a GitHub Python repository for code smells, performance issues, and security vulnerabilities, then uses GPT-4o to suggest and explain improvements.

## 🔧 Features
- Clone GitHub repos
- Analyze code complexity (Radon)
- Detect security issues (Bandit)
- Suggest AI-generated improvements (GPT-4o)
- Save patch recommendations in `.md` files

## 🚀 How to Use

### 1. Clone this repository

git clone https://github.com/Piyush94G/ai-code-refactor-assistant.git
cd ai-code-refactor-assistant

### 2. Set up your environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 3. Set your OpenAI API key

export OPENAI_API_KEY="your-openai-api-key"

### 4. Run the tool on any Python GitHub repo

python main.py https://github.com/psf/requests.git


## 📁 Output

cloned_repo/: the GitHub repo you analyzed

*_analysis_and_patch.md: generated patch 


## 📄 Example Tested Repo

python main.py https://github.com/psf/requests.git


## 📦 Requirements

openai
gitpython
radon
bandit

### Install with

pip install -r requirements.txt

