from contextlib import redirect_stderr
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        return render_template('index.html')

# route to check site for changes from the front end
@app.route("/check_site", methods=['POST'])
def check_site():
    """Will accept url and optionally a stringified html page for comparison as arguments.
    Will return JSON object with stringified version of webpage. If stringified page was provided as an argument,
    Will return additional data, including any changes to webpage, as well as a boolean to indicate whether changes were found."""

    # Unpack the arguments, deserialize json from front-end

    parameters = request.json
    print(parameters)

    # convert JSON to a dict, later we can use if "currentPage" in keys, then we can make our comparison

    # To visit the url and store the stringified html in a variable

    # If a stringified html page was provided as an argument, compare the new string with the old string

    # Pack up our data: { currentPage: "stringified html", changeDetected: boolean, difference: "portion of the stringified html" }
    data = { 'currentPage': 'the entire old page', 'changeDetected': True, 'difference': 'some new interesting stuff on your page'}

    # Return json data
    print(data);
    return data

# for testing, use: http://www.reddit.com/r/all/new