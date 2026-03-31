import json

with open("power_shell.json", "r") as file:
    logs = json.load(file)

for log in logs:
    command = log.get("CommandLine", "").lower()
    score = 0

    if "-enc" in command:
        score += 1

    if "invoke-webrequest" in command:
        score += 1

    if "iex" in command:
        score += 1

    if "executionpolicy bypass" in command:
        score += 1

    if "-noprofile" in command:
        score += 1

    if score >= 2:
        print("🚨 Suspicious PowerShell detected:", log["CommandLine"])
