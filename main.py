
import os
import sys
import openai
from git import Repo
import subprocess

# Replace with your actual OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def clone_repo(repo_url, dest_dir='cloned_repo'):
    if os.path.exists(dest_dir):
        subprocess.run(["rm", "-rf", dest_dir])
    Repo.clone_from(repo_url, dest_dir)
    print(f"Repository cloned to {dest_dir}")
    return dest_dir

def analyze_code_with_radon(path):
    print("\nAnalyzing complexity with radon...")
    subprocess.run(["radon", "cc", path, "-s", "-a"])

def analyze_security_with_bandit(path):
    print("\nAnalyzing security with bandit...")
    subprocess.run(["bandit", "-r", path])

def get_code_files(path, ext=".py"):
    code_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                code_files.append(os.path.join(root, file))
    return code_files

def read_code(file_path):
    with open(file_path, "r") as f:
        return f.read()

def suggest_improvements(code):
    print("\nGenerating improvement suggestions via OpenAI API...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert AI developer that analyzes code for code smells, security vulnerabilities, and performance bottlenecks. For any input code, you provide an improved version with detailed reasoning."},
                {"role": "user", "content": f"Analyze the following Python code. Identify issues (e.g., code smells, performance bottlenecks, security risks), suggest refactorings with explanation, and provide the updated code:\n\n{code}"}
            ],
            temperature=0.3
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print("Error during OpenAI API call:", e)
        return None

def save_refactored_suggestion(original_path, suggestion):
    output_path = original_path.replace(".py", "_analysis_and_patch.md")
    with open(output_path, "w") as f:
        f.write(suggestion)
    print(f"Analysis and patch saved: {output_path}")

def main(repo_url):
    repo_path = clone_repo(repo_url)
    analyze_code_with_radon(repo_path)
    analyze_security_with_bandit(repo_path)

    code_files = get_code_files(repo_path)
    for file in code_files:
        print(f"\nProcessing: {file}")
        original_code = read_code(file)
        suggestion = suggest_improvements(original_code)
        if suggestion:
            save_refactored_suggestion(file, suggestion)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <GitHub Repository URL>")
        sys.exit(1)

    github_url = sys.argv[1]
    main(github_url)
