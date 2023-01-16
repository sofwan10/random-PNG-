# random-PNG-
- This project is a simple Flask server that serves a randomly selected PNG image from a static folder when a user makes a request to the root route ('/'). The server uses the Flask render_template function to insert the image into an HTML template and return the rendered template as the response.
- The project has the following file structure:
```your_project/
    templates/
        index.html
    static/
        your_image1.png
        your_image2.png
        your_image3.png
    app.py
```
- The index.html file contains the HTML code that will be displayed on the page when the user makes a request. It uses the img tag to display the image. The url_for function is used to generate the URL for the image file, so that the image will be served from the static folder.
- The app.py file contains the server code that handles requests, selects a random image from the static folder, and renders the template. The code also includes error handling for the case when the static folder is empty or no PNG files are present in the folder.
- To run this project, you'll need to have Python and Flask installed on your machine. Then, you can start the server by running the app.py file, and make a request to http://localhost:5000/ in your browser to see the random image.
