import requests

def send_audio(audio_path, title="no title", duration=None, creds_path="/tmp"):
  api_key = get_api_key(creds_path)
  chat_id = get_chat_id(creds_path)

  url = f"https://api.telegram.org/bot{api_key}/sendAudio"
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

def load_conf(filename):
  f = open(filename, "r")
  data = f.readline().strip()
  f.close()
  return data

def get_api_key(path):
  return load_conf(f"{path}/api_key.dat")

def get_chat_id(path):
  return load_conf(f"{path}/chat_id.dat")
