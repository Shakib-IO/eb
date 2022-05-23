from flask import Flask
from flask import jsonify

# EB looks for an 'application' callable by default.
app = Flask(__name__)

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
    
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
    
home_link = '<p><a href="/">Back</a></p>\n'

footer_text = '</body>\n</html>'

# add a rule for the index page.
app.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# print a name on the page by passing /echo/name
@app.route("/echo/<name>")
def echo(name):
    print(f"This is the URL placed: new-{name}")
    val = {"New-Name is": name}
    return jsonify(val)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run(host='0.0.0.0', port=8081)