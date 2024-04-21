from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        old_date_obj = datetime.strptime(date, "%Y.%m.%d")
        current_date = datetime.today()
        numbers_day = current_date - old_date_obj
        return numbers_day.days
    except ValueError:
        return "Неправильний формат дати. Будь ласка, введіть дату у форматі 'YYYY.MM.DD'."

print(f"Difference in days is: {get_days_from_today('2020.10.09')}")