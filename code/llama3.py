import ollama

text = 'President Joe Biden criticized the Supreme Court’s decision on the redistricting of the South Carolina district by issuing a public statement highlighting concerns about racial discrimination.'

prompt = f"I want you to characterize the following text into actors, factors, and mechanisms. Actors can range from governmental bodies to grassroots movements, each playing a distinct role in the narrative construction. Factors encompass the various elements influencing the narrative, such as values, interests, and divergences among stakeholders. Conversely, mechanisms delve into the actors’ actions, strategies, and processes to advance their narratives and agendas. {text}"

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])

print('Narrative Characterization:')
print(response['message']['content'])
