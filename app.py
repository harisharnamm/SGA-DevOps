from flask import Flask, render_template_string
import os

app = Flask(__name__)

HOME_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Docker Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 50px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        h1 {
            font-size: 3em;
            margin-bottom: 20px;
            animation: fadeIn 1s;
        }
        p {
            font-size: 1.2em;
            margin: 10px 0;
        }
        .badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            padding: 10px 20px;
            border-radius: 25px;
            margin: 10px 5px;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 DevOps Docker Demo</h1>
        <p>🎉 <strong>Hello World from Docker Container!</strong></p>
        <p>This Flask application is running inside a Docker container</p>
        <div>
            <span class="badge">🐍 Python</span>
            <span class="badge">🌶️ Flask</span>
            <span class="badge">🐳 Docker</span>
        </div>
        <p style="margin-top: 30px;">
            <strong>Container Status:</strong> ✅ Running Successfully
        </p>
        <p><strong>Port:</strong> 8080</p>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HOME_TEMPLATE)

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Container is running properly'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
