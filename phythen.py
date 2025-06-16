from flask import Flask, render_template, request, redirect

app = Flask(__name__)
articles = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        articles.append({'title': title, 'content': content})
        return redirect('/')
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)