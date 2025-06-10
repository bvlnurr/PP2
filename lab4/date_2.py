from datetime import datetime, timedelta

today = datetime.now().date()
yestoday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

print("Yestoday: ", yestoday)
print("Today: ", today)
print("Tomorrow: ", tomorrow)