import unirest
import json



response = unirest.post("https://community-sentiment.p.mashape.com/text/",
  headers={
    "X-Mashape-Key": "jkJXw4Wg4lmshEpfSjVN3fj71XFVp1P3a9wjsntQP4BkpzBIO4",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "txt": "The appearance & location of the Hotel was best suited for me. The room was very clean & best decorated like shown in photographs. AC, TV, 24 Hrs electricity facilities. The Food quality was very good and overall service was very very good. Staff was also very good and they provided us very good service."
  }
)

json_text=json.loads(response.raw_body)
print(json_text)
