from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import os
from anthropic import Anthropic
import logging

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

anthropic = Anthropic()

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    def generate():
        try:
            app.logger.info(f"Sending message to Claude: {user_message}")
            with anthropic.messages.stream(
                max_tokens=1000,
                messages=[{"role": "user", "content": user_message}],
                model="claude-3-5-sonnet-20240620"
            ) as stream:
                for text in stream.text_stream:
                    yield text
                    
        except Exception as e:
            app.logger.error(f"Error in /api/chat: {str(e)}", exc_info=True)
            yield str(e)

    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)