import requests

def send_audio(audio_path, title="no title", duration=None):
  api_key = get_api_key()
  chat_id = get_chat_id()

  url = f"https://api.telegram.org/bot{api_key}/sendAudio"
  print(url)
  payload = {
    "chat_id": chat_id,
    "title": title
  }

  if duration:
    payload["duration"]=duration

  files = {
    'audio': open(audio_path,'rb')
  }
  response = requests.request("POST", url, data=payload, files=files,stream=True)
  print(response.text)

def load_conf(filename):
  f = open(filename, "r")
  data = f.readline().strip()
  f.close()
  return data

def get_api_key():
  return load_conf("api_key.dat")

def get_chat_id():
  return load_conf("chat_id.dat")
