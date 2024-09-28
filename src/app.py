from flask import Flask, request, jsonify 
import joblib 

app = Flask(__name__)

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


@app.route('/',methods=['GET'])
def index():
    return {"status": True}


@app.route('/detect-spam', methods=['POST'])
def detect_spam():
    data = request.get_json()
    if 'message' not in data:
        return jsonify({'error': 'Le champ "message" est requis.'}), 400

    message = data['message']
    message_transformed = vectorizer.transform([message])
    prediction = model.predict(message_transformed)
    result = 'Spam' if prediction[0] == 1 else 'Ham'
    return jsonify({'prediction': result})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8000,debug=True)
