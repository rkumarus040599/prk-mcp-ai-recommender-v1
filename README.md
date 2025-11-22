# AI Resume Recommender

A Streamlit application that analyzes resumes and provides job recommendations from Naukri.com using AI-powered insights.

## Features

- PDF resume upload and text extraction
- AI-powered resume analysis (summary, skill gaps, career roadmap)
- Job keyword extraction
- Real-time job fetching from Naukri.com
- Clean, user-friendly interface

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
APIFY_API_TOKEN=your_apify_token_here
```

3. Run the application:
```bash
streamlit run app.py
```

## Mock to No-Mock Switching

The application supports both mock responses (for testing) and real OpenAI API calls.

### Current Status: MOCK MODE
The app currently uses mock responses to avoid OpenAI API costs during development.

### To Switch from Mock to Real OpenAI:

1. Open `app.py`
2. Find lines 2-5:
```python
# Mock version (comment/uncomment to switch)
from src.helper_mock import extract_text_from_pdf, ask_openai
# Real OpenAI version (comment/uncomment to switch)
# from src.helper_no_mock import extract_text_from_pdf, ask_openai
```

3. Make these 2 changes:
   - **Comment out** line 3: Add `#` before `from src.helper_mock...`
   - **Uncomment** line 5: Remove `#` from `from src.helper_no_mock...`

4. Result should look like:
```python
# Mock version (comment/uncomment to switch)
# from src.helper_mock import extract_text_from_pdf, ask_openai
# Real OpenAI version (comment/uncomment to switch)
from src.helper_no_mock import extract_text_from_pdf, ask_openai
```

### Prerequisites for Real OpenAI Mode:
- Valid OpenAI API key in `.env` file
- Sufficient OpenAI credits/quota
- Internet connection

### To Switch Back to Mock Mode:

1. Open `app.py`
2. Find lines 2-5 (which should now look like this in no-mock mode):
```python
# Mock version (comment/uncomment to switch)
# from src.helper_mock import extract_text_from_pdf, ask_openai
# Real OpenAI version (comment/uncomment to switch)
from src.helper_no_mock import extract_text_from_pdf, ask_openai
```

3. Make these 2 changes:
   - **Uncomment** line 3: Remove `#` from `from src.helper_mock...`
   - **Comment out** line 5: Add `#` before `from src.helper_no_mock...`

4. Result should look like:
```python
# Mock version (comment/uncomment to switch)
from src.helper_mock import extract_text_from_pdf, ask_openai
# Real OpenAI version (comment/uncomment to switch)
# from src.helper_no_mock import extract_text_from_pdf, ask_openai
```

**Note:** Only one import line should be active at a time - either mock OR no-mock, never both.

## File Structure

```
├── app.py                 # Main Streamlit application
├── src/
│   ├── helper_mock.py     # Mock OpenAI responses
│   ├── helper_no_mock.py  # Real OpenAI API calls
│   └── jobs_api.py        # Naukri job fetching
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## Troubleshooting

### If you get OpenAI quota errors in Mock Mode:

The GitHub version may have an issue with `helper_mock.py`. If you see `openai.RateLimitError` even in mock mode:

1. Open `src/helper_mock.py`
2. Replace the `ask_openai` function with:
```python
def ask_openai(prompt, max_tokens=500):
    # Mock response for testing
    if "summarize" in prompt.lower():
        return "Mock Summary: Experienced software developer with skills in Python, JavaScript, and cloud technologies."
    elif "missing skills" in prompt.lower() or "skill gaps" in prompt.lower():
        return "Mock Skills Gap: Consider learning Docker, Kubernetes, and advanced machine learning frameworks."
    elif "roadmap" in prompt.lower() or "future roadmap" in prompt.lower():
        return "Mock Roadmap: 1. Complete cloud certifications 2. Build portfolio projects 3. Contribute to open source."
    elif "job titles" in prompt.lower():
        return "Mock Keywords: Senior Software Engineer, Backend Developer, Cloud Solutions Architect, DevOps Engineer"
    else:
        return "Mock response for testing purposes."
```
3. Save the file and restart the app

## Dependencies

- streamlit
- openai
- PyPDF2
- python-dotenv
- apify-client