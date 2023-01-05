import os
import openai
from dotenv import load_dotenv

#environment variable

load_dotenv()

API_KEY = os.getenv("API_KEY")

def generate_text(prompt):
  openai.api_key = API_KEY
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    temperature=0.1
  )

  return response.choices[0].text

#query = "What is your name?"
#response = gpt3(query)
#print(response)

#PARAMETERS;

#model, which model is being used
#prompt is a string or array of strings that will be used to generate completion
#max tokens refers to the length of completion
#temperature refers to how random the response will be, between 0 and 0.9
