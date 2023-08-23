from flask import Flask, request, render_template
from model import predict, get_info_by_model

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', form=request.form)

def inject_load_predict():
    input = request.form.get("text_field_1")
    try:
        return {"text_field_2": "Result: "+str(predict(input))}
    except:
        return {"text_field_2": 'Wrong format: need 24 values to unpack'}

@app.context_processor    
def inject_load_model():
    return {"text_field_4": "Result: "+str(get_info_by_model())}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)