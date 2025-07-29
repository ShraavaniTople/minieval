from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

print("Setting up Flask app...")  # DEBUG line

# Download NLTK data (only runs once)
nltk.download('punkt')

app = Flask(__name__)
print("App created")  # DEBUG line

def basic_eval(text1, text2):
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    return round(score * 100, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Rendering page...")  # DEBUG line
    score = None
    output1 = ""
    output2 = ""
    if request.method == 'POST':
        output1 = request.form['output1']
        output2 = request.form['output2']
        score = basic_eval(output1, output2)

    return render_template('index.html', score=score, output1=output1, output2=output2)

if __name__ == '__main__':
    print("About to run app...")  # DEBUG line
    app.run(debug=True, port=5000)
