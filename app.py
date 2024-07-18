# # IMport Flask for this project
# from flask import Flask

# # constructor
# app = Flask(__name__)

# #   Routing
# @app.route('/')

# # methods1
# def hello_world():
#     return 'Hello World!!!'

# # routing,method2
# @app.route('/hello')
# def hello():
#     return "Hello Welcome to the Training!!!"

# # Routing3,method3 with value
# @app.route('/login/<username>')
# def login(username):
#     return f'The username is{username}'

# # Routing4, Method 4 with values ID
# @app.route('/login/<int:id>')
# def login_id(id):
#     return f'The is of the user is {id}'


# # Run
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask,render_template 

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
























