import http.client

conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

payload = "q=English%20is%20hard%2C%20but%20detectably%20so"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'Accept-Encoding': "application/gzip",
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
    'X-RapidAPI-Host': "google-translate1.p.rapidapi.com"
    }

conn.request("POST", "/language/translate/v2/detect", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))