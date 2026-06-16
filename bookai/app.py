import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'bookai2026'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    import PyPDF2
    
    # Step 1 - Get uploaded file
    book = request.files['book']
    
    # Step 2 - Extract text from ALL pages
    reader = PyPDF2.PdfReader(book)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    
    # Smart chunking - take intro + middle + end for better coverage
    total = len(text)
    if total > 9000:
        chunk1 = text[:3000]          # beginning
        chunk2 = text[total//2:total//2+3000]  # middle
        chunk3 = text[-3000:]         # end
        text = chunk1 + "\n...\n" + chunk2 + "\n...\n" + chunk3
    
    # Step 3 - Send to Gemini with quiz request
    api_key = os.environ.get('GEMINI_API_KEY', '')
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={api_key}"
    
    prompt = f"""You are an expert teacher and learning designer. Analyze this text from a technical book.

PART 1 - KEY CONCEPTS:
Extract the 7 most critical concepts someone must understand to apply this book's knowledge.
For each concept:
**Concept [number]: [Title]**
Explanation: [2 clear sentences]
Real example: [1 practical example]

PART 2 - STUDY PLAN:
For each concept create a 3-step action plan to actually master it:
Step 1: [Understand - what to read or watch]
Step 2: [Practice - a specific exercise to do]
Step 3: [Apply - a real project or task to complete]

PART 3 - QUIZ:
Create 5 multiple choice questions to test understanding.
Format each question as:
Q[number]: [Question]
A) [option]
B) [option]
C) [option]
D) [option]
Answer: [correct letter]

Book text:
{text}"""
    
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    response = requests.post(url, json=data)
    result = response.json()
    
    if 'candidates' not in result:
        return "Error connecting to AI. Please try again."
    
    content = result['candidates'][0]['content']['parts'][0]['text']
    
    return render_template('results.html', content=content)
if __name__ == '__main__':
    app.run(debug=True, port=5002)
