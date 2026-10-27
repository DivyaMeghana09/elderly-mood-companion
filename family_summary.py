from openai import OpenAI


def generate_family_summary(client, memories):
    if not memories:
        return "No care observations have been recorded yet."

    recent_memories = memories[-10:]

    timeline_text = "\n".join(
        f"- {item.get('date', 'Unknown date')} "
        f"{item.get('time', '')}: "
        f"{item.get('observation', '')} "
        f"(Mood: {item.get('mood', 'unknown')})"
        for item in recent_memories
        if item.get("observation")
    )

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-super-120b-a12b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are CareFlow AI, an elderly-care coordination assistant. "
                    "Create a short family care summary from the observations provided. "
                    "Only mention people and observations that actually appear in the data. "
                    "Do not invent names, events, symptoms, or details. "
                    "If only one observation exists, summarize only that observation. "
                    "Do not diagnose medical conditions or prescribe treatment. "
                    "Use simple caregiver-friendly language. "
                    "Return exactly 2 to 3 concise bullet points. "
                    "Each bullet should be no more than 20 words. "
                    "Prioritize the most recent observations and follow-up needs. "
                    "Do not include unnecessary historical details."
                    "If observations mention a fall with new or sudden confusion, "
                    "unresponsiveness, difficulty breathing, or another potentially "
                    "serious event, clearly state that urgent human attention is needed. "
                    "Never describe such an event as merely something to monitor. "
                    "A later positive mood or normal activity does not cancel out an "
                    "earlier serious event. "
                    "Keep the summary factual and do not invent events or diagnoses. "
                    "Remind readers that the summary does not replace emergency medical assessment."
                )
            },
            {
                "role": "user",
                "content": (
                    "Create a family care summary from these observations:\n\n"
                    + timeline_text
                )
            }
        ],
        temperature=0,
        max_tokens=800
    )

    content = response.choices[0].message.content

    if not content:
        return "Family summary could not be generated right now. Please try again."

    return content.strip()
