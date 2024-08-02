from flask import Flask, request, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload_file():
    file=request.files['file']
    if file:
        data=pd.read_csv(file)
        model=LinearRegression()
        model.fit(data[['feature1']], data['target'])
        prediction=model.predict(data[['feature1']])
        return render_template('results.html', prediction=prediction)
    return "No file uploaded"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
