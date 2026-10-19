import analysis
import report
from loader import load_raw
from plot import plot_cumulative
from preparation import prepare_records

DATA_PATH = "eva-data.json"
PLOT_PATH = "cumulative_duration.png"


def main():
    start_year = int(input("Start year: "))
    end_year = int(input("End year: "))

    records = prepare_records(load_raw(DATA_PATH), start_year, end_year)

    dates, cumulative = analysis.cumulative_hours(records)
    totals = analysis.country_totals(records)

    report.print_categories(analysis.category_counts(records))
    report.print_top_crew(analysis.top_crew(records))

    plot_cumulative(dates, cumulative, totals, PLOT_PATH)


if __name__ == "__main__":
    main()
