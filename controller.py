from flask import Flask, jsonify, request

import telegram_broadcast as broadcast

app = Flask(__name__)

@app.get('/')
def test(): 
    response = jsonify('Hello world!')
    response.status_code = 200
    return response

@app.post('/broadcast')
async def send_message(): 
    payload = request.get_json()
    if payload.get("message") is None: 
        response = get_error_response()
        response.status_code = 400
    else: 
        message = payload["message"]
        parse_mode = "" if payload.get("message_format") is None else payload["message_format"]
        chat_id = "" if payload.get("chat_id") is None else payload["chat_id"]
        
        await broadcast.send_message(message, parse_mode, chat_id)
        response = jsonify(body="Message sent successfully.")
        response.status_code = 200
    return response

def initialise_endpoint(): 
    app.run(debug=True)

def get_error_response(): 
    return jsonify(body="400 Bad Request. Message not defined.",
                   schema="{'message': 'compulsory','message_format': 'optional',chat_id': 'optional'}")
