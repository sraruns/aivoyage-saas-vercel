from fastapi import FastAPI
from openai import OpenAI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/api", response_class=PlainTextResponse)
def get_idea():
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates ideas for a business."},
        ]
    )
    return response.choices[0].message.content

