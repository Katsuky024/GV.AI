from gettext import install

pip install openai

import openai

# Configura tu clave API
openai.api_key = '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'

# Ejemplo de cómo hacer una solicitud
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "¿Cómo estás?"}
    ]
)

print(response['choices'][0]['message']['content'])
