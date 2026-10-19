import analysis
import report
from loader import load_raw
from plot import plot_cumulative
from preparation import filter_by_year, match_country, parse_records
from user_input import read_country, read_year_range

DATA_PATH = "eva-data.json"
PLOT_PATH = "cumulative_duration.png"


def resolve_country(name, known_countries):
    match = match_country(name, known_countries)
    if match is None:
        report.print_unknown_country(name)
        return name
    return match


def main():
    all_records = parse_records(load_raw(DATA_PATH))
    known_countries = analysis.countries(all_records)

    start_year, end_year = read_year_range()
    country_a = resolve_country(read_country("Country A: "), known_countries)
    country_b = resolve_country(read_country("Country B: "), known_countries)

    records = filter_by_year(all_records, start_year, end_year)

    dates, cumulative = analysis.cumulative_hours(records)
    totals = analysis.country_totals(records)

    report.print_categories(analysis.category_counts(records))
    report.print_top_crew(analysis.top_crew(records))

    stats, leader = analysis.compare_countries(records, country_a, country_b)
    report.print_country_comparison(stats, leader, start_year, end_year)

    plot_cumulative(dates, cumulative, totals, PLOT_PATH)


if __name__ == "__main__":
    main()
