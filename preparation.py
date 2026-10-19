from datetime import datetime

from models import EVARecord


def parse_duration(duration_text):
    hours, minutes = map(int, duration_text.split(":"))
    return hours + minutes / 60


def prepare_records(raw_data, start_year, end_year):
    records = []
    for eva in raw_data:
        date_text = eva.get("date")
        duration_text = eva.get("duration")
        country_text = eva.get("country")
        crew_text = eva.get("crew", "")

        if not date_text or not duration_text or not country_text:
            continue

        date = datetime.fromisoformat(date_text)
        if not (start_year <= date.year <= end_year):
            continue

        records.append(EVARecord(date, parse_duration(duration_text), country_text, crew_text))

    records.sort(key=lambda record: record.date)
    return records
