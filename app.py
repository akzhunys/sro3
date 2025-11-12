from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="kk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Нұржан Ақжүніс</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #f0f8ff, #add8e6);
                font-family: 'Arial', sans-serif;
            }
            h1 {
                font-size: 3em;
                color: #333;
                text-shadow: 2px 2px #aaa;
            }
        </style>
    </head>
    <body>
        <h1>Нұржан Ақжүніс ИС-22</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
