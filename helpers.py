from datetime import datetime, date

from config import PYTHON_TECHNOLOGIES

UA_MONTHS_TO_NUMS = {
    "січня": "1",
    "лютого": "2",
    "березня": "3",
    "квітня": "4",
    "травня": "5",
    "червня": "6",
    "липня": "7",
    "серпня": "8",
    "вересня": "9",
    "жовтня": "10",
    "листопада": "11",
    "грудня": "12",
}

SAME_TECHNOLOGIES = {
    "django rest framework": "drf",
    "machine learning": "ml",
    "javascript": "js",
    "circleci": "cci",
    "firebase realtime database": "frd"
}


def convert_month_name_to_month_num(ua_date: str) -> date:

    date_segments = ua_date.split()
    date_segments[1] = UA_MONTHS_TO_NUMS[date_segments[1]]

    return datetime.strptime(" ".join(date_segments), "%d %m %Y").date()


def find_technologies(description: str) -> list:

    technologies_in_description = []

    for tech in PYTHON_TECHNOLOGIES:
        if tech in description.lower():
            if tech in SAME_TECHNOLOGIES.keys():
                technologies_in_description.append(SAME_TECHNOLOGIES[tech])
            else:
                technologies_in_description.append(tech)

    return technologies_in_description
