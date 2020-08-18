import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
ye=int(input("Enter year"))
da=int(input("Enter date"))
la=float(input("enter la"))
data = {
    "Inputs": {
          "WebServiceInput0":
          [
              {
                    'usaf': "999999",
                    'wban': "03759",
                    'datetime': "2020-07-14T14:00:00Z",
                    'latitude': la,
                    'longitude': "-78.466",
                    'elevation': "359",
                    'windAngle': "",
                    'windSpeed': "1.3",
                    'temperature': "26.3",
                    'seaLvlPressure': "",
                    'cloudCoverage': "",
                    'presentWeatherIndicator': "",
                    'pastWeatherIndicator': "",
                    'precipTime': "1",
                    'precipDepth': "0",
                    'snowDepth': "",
                    'stationName': "CHARLOTTESVILLE 2 SSE",
                    'countryOrRegion': "US",
                    'p_k': "999999-03759",
                    'year': ye,
                    'day': da,
                    'version': "1",
              },
          ],
    },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'http://23.99.112.112:80/api/v1/service/noa/score'
api_key = '1aYLDyNWtMddz6fu7gSDwF8R17waZuBs' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
