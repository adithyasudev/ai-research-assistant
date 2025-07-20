import streamlit as st
import requests
from openai import OpenAI

# Load API keys from secrets
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Set page configuration
st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title(" Personal Research Assistant Using  ֎🇦🇮 ")
st.markdown("Enter your research question and let AI do the work!")

# text input 

query = st.text_input("Enter your research question")

if st.button("Search & Summarize"):
    if not query.strip():
        st.warning("Please enter a research question.")
    else:
        st.info("🔎 Searching for sources...")

        #  Step 1: Get 4–5 links from Tavily API 

        search_url = "https://api.tavily.com/search"
        headers = {"Content-Type": "application/json"}
        payload = {
            "api_key": TAVILY_API_KEY,
            "query": query,
            "search_depth": "advanced",
            "max_results": 5
        }

        response = requests.post(search_url, headers=headers, json=payload)
        data = response.json()

        sources = data.get("results", [])

        if not sources:
            st.error("No sources found. Try a different question.")
        else:
            st.success(f" 🤓☝️ Found {len(sources)} relevant sources.")

            # --- Step 2: Summarize each source ---
            summaries = []
            st.subheader("🔗 Sources & Summaries")

            for i, source in enumerate(sources, start=1):
                title = source.get("title", "No Title")
                url = source.get("url", "")
                content = source.get("content", "")

                st.markdown(f"### {i}. [{title}]({url})")

                if content:
                    with st.spinner(f"Summarizing source {i}..."):
                        summary_prompt = (
                            f"Summarize the following content in clear, bullet points:\n\n{content}"
                        )
                        completion = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "You are a helpful research assistant."},
                                {"role": "user", "content": summary_prompt}
                            ],
                            temperature=0.7
                        )

                        summary = completion.choices[0].message.content.strip()
                        summaries.append(summary)
                        st.markdown(summary)
                else:
                    st.warning("No content available for this source.")
                    summaries.append("No content available.")

            # --- Step 3: Final Research Report ---
            st.subheader("📝 Final Research Summary")
            if summaries:
                final_prompt = (
                    f"Based on these summaries:\n\n{summaries}\n\n"
                    f"Create a final research report that is clear, concise, and easy to understand."
                )

                with st.spinner("Generating final research report..."):
                    final_completion = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful research assistant."},
                            {"role": "user", "content": final_prompt}
                        ],
                        temperature=0.5
                    )

                    final_report = final_completion.choices[0].message.content.strip()
                    st.markdown(final_report)
            else:
                st.warning("No summaries to generate final report.")
