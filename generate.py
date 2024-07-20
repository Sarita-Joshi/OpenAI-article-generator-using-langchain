import openai

openai.api_key = 'OPENAI_API_Key'


def generate_article(params):

    return 'What is Lorem Ipsum?\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

    prompt = f'Write an article about {params["title"]}'

    if 'keywords' in params:
        prompt += f" Include keywords: {','.join(params['keywords'])}."

    if 'outline' in params:
        prompt += f" Follow this outline: {','.join(params['outline'])}."

    if 'purpose' in params:
        prompt += f" The article is intended for: {params['purpose']}."
        
    
    prompt += f" Tone Should be: {params['tone']}"
    prompt += f" Target audience is: {params['audience']}"

    response = openai.Completion.create(
        engine = 'text-danvici-003',
        prompt = prompt,
        max_tokens = params['length'] // 5,
        temperature = 0.7,
    )

    return response.choices[0].text


        
