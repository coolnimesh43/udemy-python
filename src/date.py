from datetime import datetime
delta = datetime.now() - datetime(1990, 1, 1)
print(delta)
date_from_str = datetime.strptime("2018-12-26 12:20:00", "%Y-%m-%d %H:%M:%S")
print(date_from_str)
print(date_from_str.month)
