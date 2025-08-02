# utils.py

import os
import spacy
import pdfplumber
import docx
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load the transformer model once
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

# Extract text from .pdf, .docx, or .txt
def extract_text(file):
    ext = file.name.split('.')[-1]
    if ext == 'pdf':
        with pdfplumber.open(file) as pdf:
            return '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif ext == 'docx':
        doc = docx.Document(file)
        return '\n'.join(p.text for p in doc.paragraphs)
    elif ext == 'txt':
        return file.read().decode('utf-8')
    return ""

# Extract named entities (Skills, Orgs, Locations)
def extract_entities(text):
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'GPE', 'PERSON', 'NORP', 'SKILL']]
    return list(set(skills))

# Generate embeddings using transformer
def generate_embedding(text):
    return model.encode([text])[0]

# Calculate cosine similarity
def calculate_similarity(resume_emb, jd_emb):
    return round(float(cosine_similarity([resume_emb], [jd_emb])[0][0]) * 100, 2)
