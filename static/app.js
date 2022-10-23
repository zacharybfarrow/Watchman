const siteAddress = document.getElementById("siteAddress");
const minutes = document.getElementById("minutes");
const submitButton = document.getElementById("submit")

let lastCheck = 'the old site data'
let changesFound;

const checkSite = () => {
    console.log("Checking the site")
    let data = {}
    data.url = siteAddress.value
    if (lastCheck.length > 0) {
        data.currentSite = lastCheck;
    }
    //if (lastCheck.length > 0) {
    //    data.currentSite = lastCheck;
    //}
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
    .then((result) => {
        let changeDetected = result.changeDetected;
        changesFound = result.difference;
        console.log(result)
    })
}

submitButton.addEventListener("click", checkSite)