import requests as rq
url = "http://localhost:5000/api/transcribe"
f = open("audio.mp3","rb")
data = f.read()
f.close()
res = rq.post(url,data=data)
print(res.text)