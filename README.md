# MiniEval

MiniEval is a lightweight browser based tool to compare and evaluate two AI generated text outputs. It uses TF IDF and cosine similarity to calculate how closely the responses align useful for AI practitioners, researchers, or anyone working with language models.

Live App: [https://minieval.onrender.com](https://minieval.onrender.com)

## Features

- Compare two AI generated outputs side by side
- Generate a similarity score using cosine similarity
- Visual bar for interpreting the score
- Download results as a .txt file

## Tech Stack

- Python, Flask
- scikit learn, nltk
- HTML, CSS (vanilla)
- Deployed on Render

## Local Setup

```bash
# Clone the repository
git clone https://github.com/ShraavaniTople/minieval.git
cd minieval

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python3 app.py
