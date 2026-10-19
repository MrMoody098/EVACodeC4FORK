def cumulative_hours(records):
    dates = []
    totals = []
    total_hours = 0
    for record in records:
        total_hours += record.duration_hours
        dates.append(record.date)
        totals.append(total_hours)
    return dates, totals


def country_totals(records, countries=("USA", "Russia")):
    totals = {country: 0 for country in countries}
    for record in records:
        if record.country in totals:
            totals[record.country] += record.duration_hours
    return totals


def classify_duration(duration_hours):
    if duration_hours < 4:
        return "Short"
    elif duration_hours < 7:
        return "Standard"
    return "Long"


def category_counts(records):
    counts = {"Short": 0, "Standard": 0, "Long": 0}
    for record in records:
        counts[classify_duration(record.duration_hours)] += 1
    return counts


def crew_hours(records):
    hours_by_name = {}
    for record in records:
        for name in record.crew.split(";"):
            name = name.strip()
            if name:
                hours_by_name[name] = hours_by_name.get(name, 0) + record.duration_hours
    return hours_by_name


def top_crew(records, n=5):
    return sorted(crew_hours(records).items(), key=lambda item: item[1], reverse=True)[:n]
