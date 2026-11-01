import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def analyze_incidents(incidents):

    incident_text = ""

    for fingerprint, frequency in incidents:
        incident_text += (
            f"Error: {fingerprint}\n"
            f"Frequency: {frequency}\n\n"
        )

    prompt = f"""
You are an experienced software debugging assistant.

Analyze the following application incidents.

{incident_text}

Provide the analysis in these sections:

1. Incident Summary
2. Probable Root Cause
3. Suggested Debugging Steps
4. Prevention Recommendations

Important:
- Do not claim a root cause is confirmed.
- Clearly distinguish probable causes from verified facts.
- Give practical debugging steps.
- If information is insufficient, mention what additional logs
  or configuration details are needed.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content