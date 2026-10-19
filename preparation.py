from datetime import datetime

from models import EVARecord


def parse_duration(duration_text):
    hours, minutes = map(int, duration_text.split(":"))
    return hours + minutes / 60


def parse_records(raw_data):
    records = []
    for eva in raw_data:
        date_text = eva.get("date")
        duration_text = eva.get("duration")
        country_text = eva.get("country")
        crew_text = eva.get("crew", "")

        if not date_text or not duration_text or not country_text:
            continue

        date = datetime.fromisoformat(date_text)
        records.append(EVARecord(date, parse_duration(duration_text), country_text, crew_text))

    records.sort(key=lambda record: record.date)
    return records


def filter_by_year(records, start_year, end_year):
    return [record for record in records if start_year <= record.date.year <= end_year]


def match_country(name, known_countries):
    for country in known_countries:
        if country.lower() == name.strip().lower():
            return country
    return None
