from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {
          current_date.strftime('%Y-%m-%d %H:%M:%S')}")


def calculate_future_date():
    future_date = int(
        input('Enter the number of days to add to the current date: '))
    ft = datetime.now() + timedelta(days=future_date)
    print(f'Future date: {ft.strftime("%Y-%m-%d")}')
