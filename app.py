import streamlit as st
import pandas as pd

from resume_parser import extract_text_from_pdf

from analyzer import (
    extract_skills,
    calculate_match,
    get_missing_skills
)


# -------------------------
# PAGE CONFIGURATION
# -------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# -------------------------
# TITLE
# -------------------------

st.title("📄 AI Resume Analyzer")

st.write(
    "Analyze your resume against a job description "
    "and find missing skills."
)


# -------------------------
# INPUTS
# -------------------------

uploaded_file = st.file_uploader(
    "Upload your Resume PDF",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the job description here..."
)


# -------------------------
# ANALYZE BUTTON
# -------------------------

if st.button("🔍 Analyze Resume"):

    if uploaded_file is None:

        st.warning(
            "Please upload your resume."
        )

    elif job_description.strip() == "":

        st.warning(
            "Please enter the job description."
        )

    else:

        # Load skills database
        skills_data = pd.read_csv(
            "skills.csv"
        )


        # Extract resume text
        resume_text = extract_text_from_pdf(
            uploaded_file
        )


        # Extract resume skills
        resume_skills = extract_skills(
            resume_text,
            skills_data
        )


        # Extract job skills
        job_skills = extract_skills(
            job_description,
            skills_data
        )


        # Calculate match
        match_score = calculate_match(
            resume_skills,
            job_skills
        )


        # Find missing skills
        missing_skills = get_missing_skills(
            resume_skills,
            job_skills
        )


        # -------------------------
        # RESULTS
        # -------------------------

        st.divider()

        st.subheader(
            "📊 Resume Analysis"
        )


        # Match score
        st.metric(
            "Job Match Score",
            f"{match_score}%"
        )


        # -------------------------
        # COLUMNS
        # -------------------------

        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "✅ Matching Skills"
            )

            matching_skills = set(
                resume_skills
            ).intersection(
                set(job_skills)
            )

            if matching_skills:

                for skill in matching_skills:

                    st.success(
                        f"✓ {skill}"
                    )

            else:

                st.info(
                    "No matching skills found."
                )


        with col2:

            st.subheader(
                "❌ Missing Skills"
            )

            if missing_skills:

                for skill in missing_skills:

                    st.error(
                        f"✗ {skill}"
                    )

            else:

                st.success(
                    "No important skills missing!"
                )