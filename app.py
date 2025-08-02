# app.py

import os
import streamlit as st
import pandas as pd
from utils import extract_text, extract_entities, generate_embedding, calculate_similarity

# Load job descriptions
job_df = pd.read_csv("job_data/data.csv")

# Streamlit UI
st.set_page_config(page_title="Resume Ranker", layout="wide")
st.title("📄 Resume Screening & Ranking System")

uploaded_files = st.file_uploader("Upload Resumes (.pdf/.docx/.txt)", type=["pdf", "docx", "txt"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧠 Processing...")

    job_descriptions = job_df[['Job Title', 'Description']].dropna().reset_index(drop=True)
    results = []

    for file in uploaded_files:
        resume_text = extract_text(file)
        resume_emb = generate_embedding(resume_text)
        resume_entities = extract_entities(resume_text)

        for _, row in job_descriptions.iterrows():
            job_title = row['Job Title']
            job_desc = row['Description']
            jd_emb = generate_embedding(job_desc)

            score = calculate_similarity(resume_emb, jd_emb)
            matched_skills = [skill for skill in resume_entities if skill.lower() in job_desc.lower()]

            results.append({
                "Resume": file.name,
                "Job Role": job_title,
                "Match Score": score,
                "Matched Skills": ", ".join(matched_skills)
            })

    result_df = pd.DataFrame(results)
    top_scores = result_df.sort_values(by="Match Score", ascending=False).reset_index(drop=True)

    st.success("✅ Matching Completed!")
    st.markdown("### 🏆 Ranked Leaderboard of Resumes")
    st.dataframe(top_scores.style.highlight_max(axis=0))

    # Show best match summary
    best_match = top_scores.iloc[0]
    st.markdown("---")
    st.markdown("### 🔍 Best Match Summary")
    st.markdown(f"✅ **Match Score:** {best_match['Match Score']}%")
    st.markdown(f"💼 **Strong Match For:** {best_match['Job Role']}")
    st.markdown(f"🧩 **Matched Skills:** {best_match['Matched Skills'] or 'None Detected'}")
