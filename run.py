from flask import Flask, request, render_template
from model import predict, get_info_by_model

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', form=request.form)

@app.context_processor
def inject_load_predict():
    text = request.form.get("text_field_1")
    return {"text_field_2": "Result: "+str(predict(text))}

@app.context_processor    
def inject_load_model():
    return {"text_field_4": "Result: "+str(get_info_by_model())}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)