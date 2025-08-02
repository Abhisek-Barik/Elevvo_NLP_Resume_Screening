# 🧠 NLP Task 8 – Resume Screening + Named Entity Extraction System

## 🚀 ELEVVO Internship | Abhisek Barik  
### 🌟 Industry Level → NLP Task 8 ✅ + Bonus 💡 Completed  

---

## 📌 Task Overview  
Built an advanced **AI-powered Resume Screening System** that:
- 📤 Allows users to upload multiple resumes and job descriptions
- 🎯 Matches resumes to JD using **semantic similarity**
- 📊 Displays leaderboard with **match scores**, **matched roles**, and **skills**
- 🔍 Extracts **Named Entities** like skills, experience, location using **spaCy NER**

---

## 🧠 What’s Inside  
- ✅ Used **Sentence Transformers** for semantic matching (Cosine Similarity)
- 📄 Upload multiple resumes (`.pdf`, `.docx`, `.txt`) and compare with JD
- 💼 Job Description file input via `.csv` (auto-selected top JD)
- 🏆 Leaderboard and detailed matching insights
- 🧩 Extracted Skills using spaCy NLP  
- 🌐 Streamlit UI for interaction with real-time processing

---

## 🧰 Tech Stack  

| Tool / Library         | Purpose                                  |
|------------------------|------------------------------------------|
| 🐍 Python              | Core programming language                |
| 🤗 Sentence Transformers | Semantic Embeddings for matching       |
| 📄 Pandas              | Data handling and manipulation           |
| 🔍 spaCy               | Named Entity Recognition (NER)           |
| 🧠 scikit-learn        | Cosine similarity + preprocessing         |
| 📊 Streamlit           | Front-end Web App                        |
| 📑 python-docx / PyMuPDF | Resume text extraction (DOCX, PDF)     |

---

## 🔄 Workflow  

### ✅ 1. Resume Upload & JD Selection  
- Upload multiple resumes  
- Upload job descriptions via CSV  
- Preprocess and extract text from resumes + JD

### 🧠 2. Semantic Similarity  
- Convert resume + JD into embeddings  
- Use **cosine similarity** to compute match score  
- Generate a leaderboard with highest matches  

### 🔍 3. Named Entity Recognition  
- Use spaCy to extract entities:
  - `SKILL`, `EXPERIENCE`, `ORG`, `GPE`, `DATE`, etc.  
- Highlight most relevant skills and experience  

### 🖥️ 4. Streamlit Interface  
- Upload files with ease  
- Display results with scores, matched skills  
- View extracted named entities per resume

---
