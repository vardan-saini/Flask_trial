from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [{
    'author': 'vardan saini',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'March 17, 2021'
},
    {
    'author': 'Tai',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'March 17, 2021'
},
    {

    'author': 'Kartik',
        'title': 'Blog Post 3',
        'content': 'First post content',
        'date_posted': 'March 17, 2021'
},
    {

    'author': 'aish',
        'title': 'Blog Post 4',
        'content': 'First post content',
        'date_posted': 'March 17, 2021'
},
    {

    'author': 'Mehar',
        'title': 'Blog Post 5',
        'content': 'First post content',
        'date_posted': 'March 17, 2021'
}
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
