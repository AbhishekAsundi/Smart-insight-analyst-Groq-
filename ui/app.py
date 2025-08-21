from dotenv import load_dotenv
import os

load_dotenv() 
import streamlit as st
import pandas as pd
import os
from agents.data_agent import DataAgent
from agents.insight_agent import InsightAgent
from agents.visualization_agent import VisualizationAgent
from agents.summary_agent import SummaryAgent

st.set_page_config(page_title="Smart Insight Analyst", layout="wide")

st.title("📊 Smart Insight Analyst — Groq AI Data Analytics Assistant")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data Preview")
    st.dataframe(df.head())

    if st.button("Run Analysis"):
        data_agent = DataAgent()
        insight_agent = InsightAgent()
        viz_agent = VisualizationAgent()
        summary_agent = SummaryAgent()

        # Data profiling
        profile = data_agent.run(df)

        # AI insights via Groq
        insights = insight_agent.run(profile)

        # Visualizations
        charts = viz_agent.run(df)

        # AI-generated summary via Groq
        summary = summary_agent.run(insights)

        # Display Insights
        st.subheader("🔍 AI Insights")
        st.write(insights)

        # Display Charts with download option
        st.subheader("📈 Visualizations")
        for chart_path in charts:
            st.image(chart_path, caption=os.path.basename(chart_path))
            with open(chart_path, "rb") as f:
                st.download_button(
                    label=f"Download {os.path.basename(chart_path)}",
                    data=f,
                    file_name=os.path.basename(chart_path),
                    mime="image/png"
                )

        # Display Summary
        st.subheader("📝 Executive Summary")
        st.write(summary)
