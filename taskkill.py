import subprocess

subprocess.call("TASKKILL /f /T /IM  msedge.exe")
subprocess.call("TASKKILL /f /T /IM  msedgedriver.exe")
# subprocess.call("TASKKILL /f /T  /IM conda.exe") #終わらdない
# subprocess.call("TASKKILL /f /T /IM  cmd.exe")
subprocess.call("TASKKILL /f /T /IM  conhost.exe")

# subprocess.call("TASKKILL /f /T /IM  svchost.exe")#10システムエラーになる危険



# import subprocess
# subprocess.call("TASKKILL /f  /IM  firefox.exe")
