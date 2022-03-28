from flask import Flask

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = "You will never guess"
)

@app.route('/')
def home():
    name = "Nicholas"
    city_names = ["Paris", "London", "Rome", "Thaiti"]
    return ''' <html>
                <head>
                    <title>HW Q1</title>
                </head>
                <body>
                    <h1>Hello, ''' +  name + '''!</h1>
                    <a href="www.google.com">not google</a>
                    <ul>
                        <li>'''+city_names[0] + '''</li>
                        <li>'''+city_names[1] + '''</li>
                        <li>'''+city_names[2] + '''</li>
                        <li>'''+city_names[3] + '''</li>
                    </ul>
                </body>
            </html> '''

if __name__ == "__main__":
    app.run()