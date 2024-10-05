pip install Flask

from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configura tu clave API de OpenAI
openai.api_key = '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'

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Envía el mensaje del usuario a la IA
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    
    # Obtén la respuesta de la IA
    ai_response = response['choices'][0]['message']['content']
    
    # Retorna la respuesta en formato JSON
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)
