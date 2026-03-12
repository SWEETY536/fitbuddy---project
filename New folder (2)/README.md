# FitBuddy - AI Fitness Plan Generator

FitBuddy is a web-based application that uses AI to generate personalized 7-day workout plans and nutrition tips. It is built with FastAPI and integrates with Google's Gemini AI.

## Features
- Generates localized 7-day fitness plans based on user profiles.
- Provides daily nutrition and recovery tips.
- Accepts user feedback to modify and regenerate the AI plan dynamically.
- Clean and responsive UI using Bootstrap and Jinja2 templates.
- SQLite database for persistent tracking.

## Local Deployment Instructions

### Prerequisites
- Python 3.8+ installed
- A Google Gemini API Key

### Setup Steps

1. **Clone the repository / Navigate to the folder**:
   Ensure you are in the application directory.

2. **Create a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Open the `.env` file and replace the placeholder API key with your actual Google Gemini API Key.
   ```
   GEMINI_API_KEY=your_google_gemini_api_key_here
   ```

5. **Run the Application**:
   You can run the application directly using the included `run.py` script:
   ```bash
   python run.py
   ```
   Alternatively, use Uvicorn directly:
   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

6. **Access the App**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

### Database
A local SQLite database file named `fitbuddy.db` will be created automatically upon the first run.
