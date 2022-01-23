from datetime import datetime

DATE = datetime.today()

def getTime() -> str:
    return f"{DATE.year}/{DATE.month}/{DATE.day}-{DATE.hour}:{DATE.minute}"