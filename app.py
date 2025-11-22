import streamlit as st
# Mock version (comment/uncomment to switch)
from src.helper_mock import extract_text_from_pdf, ask_openai
# Real OpenAI version (comment/uncomment to switch)
# from src.helper_no_mock import extract_text_from_pdf, ask_openai
from src.jobs_api import fetch_naukri_jobs

# page config
st.set_page_config(page_title="prk-ai-recommender-v1", layout="wide")
st.title("prk-ai-recommender")

st.markdown("upload your resume and get job recommendations based on your skills and experience from naukri")

uploaded_file = st.file_uploader("upload your resume (pdf)", type=["pdf"])
if uploaded_file:
    with st.spinner("extracting text from resume..."):
       resume_text = extract_text_from_pdf(uploaded_file)
    
    with st.spinner("summarizing your resume..."):
        summary = ask_openai(f"summarize this resume in 100 words highlighting the skills, education, and experience: \n\n {resume_text}", max_tokens=500)

    with st.spinner("finding the skill gaps..."):
        gaps = ask_openai(f"analyze this resume and highlight missing skills, certifications and experiences needed for better job opportunities: \n\n {resume_text}", max_tokens=500)
    
    with st.spinner("creating future roadmap..."):
        roadmap = ask_openai(f"based on this resume, suggest a future roadmap to improve this person's career prospects (skills to learn, certifications to obtain, industry exposure): \n\n {resume_text}", max_tokens=500)
    
    #display nicely formatted results
    st.markdown("---")
    st.header("Resume Summary")
    st.markdown(f"<div sytle=background-color: #000000; padding: 15 px, border-radius: 10px;>{summary}</div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("---")
    st.header("Skills gaps and missing areas")
    st.markdown(f"<div sytle=background-color: #000000; padding: 15 px, border-radius: 10px;>{gaps}</div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("---")
    st.header("Future roadmap and preparation strategy")
    st.markdown(f"<div sytle=background-color: #000000; padding: 15 px, border-radius: 10px;>{roadmap}</div>", unsafe_allow_html=True)
    st.markdown("---")

    st.success("Analysis completed successfully!")

    if st.button("get job recommendation"):
        with st.spinner("finding job recommendations..."):
            keywords = ask_openai(f"based on this resume summary, suggest the best job titles and keywords for searching jobs.  Give a comma-separated list only, no explanations.\n\n: {resume_text}", max_tokens=100)
            
            search_keywords_clean= keywords.replace("\n","").strip()
         
        st.success(f"extracted job keywords: {search_keywords_clean}")

        #with st.spinner("fetching jobs from linkedin"):
           #linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, rows=60)

        st.markdown("---")
        st.header("top linkedin jobs")

        # if linkedin_jobs:
        #     for job in linkedin_jobs:
        #         st.markdown(f"**{job['title']}**")
        #         st.markdown(f"**Company:** {job['companyName']}")
        #         st.markdown(f"**Location:** {job['location']}")
        #         st.markdown(f"**Apply Link:** {job['applyLink']}")
        #         st.markdown("---")
        # else:
        st.warning("No linkedin jobs found.")

        with st.spinner("fetching jobs from naukri"):
            naukri_jobs = fetch_naukri_jobs(search_keywords_clean,rows=60)

        st.markdown("---")
        st.header("top naukri jobs")

        if naukri_jobs:
            for job in naukri_jobs:
                st.markdown(f"**{job.get('title', 'N/A')}**")
                st.markdown(f"**Company:** {job.get('companyName', 'N/A')}")
                st.markdown(f"**Location:** {job.get('location', 'N/A')}")
                st.markdown(f"**Apply Link:** {job.get('applyLink', job.get('jobUrl', 'N/A'))}")
                st.markdown("---")
        else:
            st.warning("No naukri jobs found.")





