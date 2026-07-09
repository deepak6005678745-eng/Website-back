from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

# Google Gemini Client
client = genai.Client()

@app.route('/api/ask', methods=['POST'])
def ask():
    user_input = request.json.get('prompt')
    
    if not user_input:
        return jsonify({'error': 'Prompt chahiye boss!'}), 400

    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents=user_input
        )
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 Server ab port 5000 par chal raha hai!")
    app.run(port=5000, debug=True)

