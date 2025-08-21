# Smart Insight Analyst — Groq AI Data Analytics Assistant

📊 **Smart Insight Analyst** is a Streamlit-based AI-powered data analytics assistant. It provides automated **data profiling**, **AI-driven insights**, **visualizations**, and **executive summaries** for your datasets using **Groq API**.

---

## Features

- **CSV Upload:** Upload your dataset in CSV format directly through the UI.
- **Data Profiling:** Automatic summary of numeric and categorical columns, missing values, and sample data.
- **AI Insights:** Uses Groq API to generate actionable insights from your dataset.
- **Visualizations:** Generates charts (bar and pie) for a quick understanding of data distribution.
- **Executive Summary:** AI-generated summary highlighting key patterns and findings.
- **Download Charts:** Export visualizations as PNG images.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AbhishekAsundi/Smart-insight-analyst-Groq-.git
cd Smart-insight-analyst-Groq-

2. Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt


4. Create a .env file in the project root with your Groq API key:

GROQ_API_KEY=your_groq_api_key_here

5 .Usage

Run the Streamlit app:

streamlit run ui/app.py
