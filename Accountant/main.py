import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


def main():
    time_now = datetime.datetime.now()
    date_now = time_now.strftime("%x")
    print(f"Сегодня хороший день {date_now}")
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    main()

