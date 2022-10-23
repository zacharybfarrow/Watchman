from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        return render_template('index.html')

# Route to check site for changes from the front end
@app.route("/check_site", methods=['POST'])
def check_site():
    """Will accept url and optionally a stringified html page for comparison as JSON data along with POST request.
    Will return JSON object with stringified version of webpage. If stringified page was provided as an argument,
    Will return additional data, including any changes to webpage, as well as a boolean to indicate whether changes were found."""

    # Unpack the arguments, deserialize json from front-end
    data = request.json
    print(f"Data Received: {data}")

    # TODO: convert JSON to a dict, later we can use 'if "currentPage" in keys', then we can make our comparison

    # TODO: Visit the url and store the stringified html in a variable

    # TODO: If a stringified html page was provided as an argument, compare the new string with the old string

    # TODO: Pack up our data: { currentPage: "stringified html", changeDetected: boolean, difference: "portion of the stringified html" }
    # Dummy Data:
    payload = { 'currentSite': 'the webpage as it is right now', 'changeDetected': True, 'changesFound': 'some new interesting stuff on your page'}

    # Return json data
    print(f"Sending payload: {payload}"); # Debug
    return payload

# for testing, use: http://www.reddit.com/r/all/new