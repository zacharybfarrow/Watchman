from urllib.error import URLError
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
from urllib.request import urlopen
from difflib import HtmlDiff

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

    payload = {}
    # Unpack the arguments, deserialize json from front-end
    data = request.json
    print(f"Data Received: {data}")
    url = data["url"]
    if "currentSite" in data.keys():
        print("Found old site data")
        ### oldSite = data["currentSite"]
        ### replacing pull from json data with dummy data
        try:
            with urlopen("https://en.wikipedia.org/w/index.php?title=Lorem_ipsum&direction=next&oldid=1099356353") as response:
                dummy_html = response.read()
        except Exception as e:
            return "URL Error: " + str(e)
        dummy_soup = BeautifulSoup(dummy_html, "html.parser")
        dummy_oldSite = dummy_soup.get_text()
        ### print(oldSite)

    # Go to url and get the html content
    try:
        with urlopen(url) as response:
            html = response.read()
    except Exception as e:
        return "URL Error: " + str(e)
    
    soup = BeautifulSoup(html, "html.parser")
    currentSite = soup.get_text()
    print("New site data collected")
    payload["currentSite"] = currentSite
    # print(currentSite)

    if dummy_oldSite == currentSite:
        payload["changeDetected"] = False
        print("no changes detected")
    else:
        payload["changesDetected"] = True
        print("changes found")
    
    html_diff = HtmlDiff()
    payload["changesFound"] = html_diff.make_table(dummy_oldSite, currentSite)

    #print(payload["changesFound"])

    # Return json data
    # print(f"Sending payload: {payload}"); # Debug
    return payload

# for testing, use: https://en.wikipedia.org/wiki/Lorem_ipsum for new
# and this one for old: https://en.wikipedia.org/w/index.php?title=Lorem_ipsum&direction=next&oldid=1099356353
# write the old one to a dummy_oldSite.py and import it
# then work on how to do the diff formatting by writing to another file and viewing there