import streamlit as st
import pandas as pd
import requests
import time

st.title("🛒 Acme Product Review Analyzer")
uploaded_file = st.file_uploader("Upload CSV file with product reviews", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    results = []
    
    with st.spinner("Analyzing reviews..."):
        for _, row in df.iterrows():
            review_text = row["review_text"]
            try:
                res = requests.post("http://localhost:8000/analyze/", data={"text": review_text})
                res.raise_for_status()  # Raise an exception for HTTP errors
                data = res.json()
                results.append({
                    "product_name": row["product_name"],
                    "review_text": review_text,
                    **data
                })
                # Add a small delay to avoid overwhelming the backend
                time.sleep(0.5)
            except requests.exceptions.RequestException as e:
                st.error(f"Error processing review: {e}")
                st.error("Make sure your backend server is running at http://localhost:8000")
            except ValueError as e:
                st.error(f"Error parsing response: {e}")
    
    if results:
        result_df = pd.DataFrame(results)
        st.success("Analysis complete!")
        st.dataframe(result_df)
        st.download_button("Download Results as CSV", result_df.to_csv(index=False), file_name="analyzed_reviews.csv", mime="text/csv")
        
        st.subheader("📊 Sentiment Distribution")
        st.bar_chart(result_df["sentiment"].value_counts())
        
        st.subheader("📌 Top Topics")
        st.bar_chart(result_df["topic"].value_counts())