import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)

print (response)

#PARAMETERS;

#model, which model is being used
#prompt is a string or array of strings that will be used to generate completion
#max tokens refers to the length of completion
#temperature refers to how random the response will be, between 0 and 0.9
