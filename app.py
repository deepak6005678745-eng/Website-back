import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

# Google Gemini Client automatically GOOGLE_API_KEY environment variable utha lega
client = genai.Client()

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get('prompt')
    
    if not user_input:
        return jsonify({'error': 'Prompt chahiye boss!'}), 400

    try:
        # Model call
        response = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents=user_input
        )
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Cloud platforms PORT variable dete hain, agar na mile toh 5000 use hoga
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Server port {port} par live hai!")
    app.run(host='0.0.0.0', port=port)
