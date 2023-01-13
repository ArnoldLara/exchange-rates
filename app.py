from flask import *
import requests

#Function to make conversion using API Layer exchangerates. Return the value of converstion
def ExchangeRate(rate_to,rate_from,amount):

    url = "https://api.apilayer.com/exchangerates_data/convert?to="+rate_to+"&from="+rate_from+"&amount="+amount
    #url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=COP&amount=10"
    payload = {}
    headers= {
    "apikey": "C1phjF8m5yNHjpbeArtukNzcW6CG6J32"
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    jsonResponse = response.json()

    status_code = response.status_code
    result = response.text

    print(jsonResponse)
    return jsonResponse["result"]


app = Flask(__name__)

# Allow GET and POST Method for consults to root directory
@app.route("/", methods=["GET", "POST"])

def home():
    value = "0"
    #If request is for POST Method return a render of HTML with the result
    if request.method == "POST":
        amount = str(request.form["amount"])
        from_rate = request.form["from"]
        to_rate = request.form["to"]
        value = str(ExchangeRate(to_rate,from_rate,amount))
        print("Amount "+ amount)
        print("From: "+ from_rate)
        print("To: "+ str(to_rate))      
        print("Value: " + value)
        return render_template("index.html",value=value)

    #If resquest is for GET method return a render of HTML
    return render_template("index.html")
   

#Allow listen on all interfaces of the server in 5000 port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)