from datetime import datetime as d
from send_audio import send_audio
import subprocess
import sys

args = sys.argv
print(args)
print(len(args))

if len(args)!=2:
  print(f"{d.now()} - ERROR - Wrong parameter count. Only one needed: time in seconds")
  sys.exit(-1)

def download_audio(file_name, timeout):
  bin_file = "ffmpeg"
  china_fm_url = "https://radioserver12.profesionalhosting.com/proxy/pkg152387/stream"
  command_line = [bin_file, "-i", china_fm_url, "-t", timeout, "-c", "copy", "-y", file_name]
  print(command_line)

  try:
    ret = subprocess.run(command_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if (ret.returncode==0):
      print(f"{d.now()} - INFO - Recording completed successfully to {file_name}")
    else:
      print(f"{d.now()} - ERROR - Recording failed! {ret.stderr.decode('utf-8')}")
      sys.exit(-2)

  except Exception as e:
    print(f"{d.now()} - EXCEPTION - {e}")
    sys.exit(-3)

now = d.now().strftime('%Y_%m_%d__%H_%M_%S')
recording_name = f"china_fm_{now}"
file_name = f"{recording_name}.aac"
timeout = args[1]

download_audio(file_name, timeout)
send_audio(file_name, recording_name, timeout)
