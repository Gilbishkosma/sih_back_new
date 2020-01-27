import pytz
from datetime import datetime

def get_date_time():
	tz = pytz.timezone('Asia/Kolkata')
	date = datetime.now(tz=tz)
	return date