from fastapi import FastAPI
from openai import OpenAI
from fastapi.responses import PlainTextResponse, StreamingResponse

app = FastAPI()

@app.get("/api", response_class=PlainTextResponse)
def get_idea():
    client = OpenAI()
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user",
         "content": "Reply with a new business idea for AI Agents, formatted with headings, sub-headings and bullet points"}],
        temperature=0.7,
        stream=True
    )

    def event_stream():
        for chunk in stream:
            text = chunk.choices[0].delta.content
            if text:
                lines = text.split("\n")
                for line in lines:
                    yield f"data: {line}\n"
                yield "\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")

