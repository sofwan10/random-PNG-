from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Get a list of all PNG files in the static folder
    static_folder = os.path.join(app.root_path, 'static')
    png_files = [f for f in os.listdir(static_folder) if f.endswith('.png')]

    # Select a random PNG file
    random_png = random.choice(png_files)

    # Render the index.html template and pass in the random PNG file as a variable
    return render_template('index.html', random_png=random_png)

@app.route('/static/<path:path>')
def serve_static(path):
    # Serve the static files from the static
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run()
