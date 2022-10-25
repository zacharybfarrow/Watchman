const siteAddress = document.getElementById("siteAddress");
const minutes = document.getElementById("minutes");
const submitButton = document.getElementById("submit")

let lastCheck = 'the old site data'
let changesFound;

const checkSite = () => {
    console.log("Checking the site")
    // Compile data for POST request
    let data = {}
    data.url = siteAddress.value
    if (lastCheck.length > 0) {
        data.currentSite = lastCheck;
    }
    // Access backend API to check site for differences
    fetch("/check_site", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": 'application/json'
        }
    })
    // Parse data received
    .then((response) => {
        console.log("Receiving data");
        return response.json();
    })
    // Do stuff with our new data
    .then((result) => {
        let changeDetected = result.changeDetected;
        changesFound = result.difference;
        console.log(result)
    })
    .catch(() => {
        console.log("there was an error");
    })
}

submitButton.addEventListener("click", checkSite)