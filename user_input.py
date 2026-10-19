def read_year(prompt):
    while True:
        text = input(prompt).strip()
        if text.isdigit():
            return int(text)
        print("Please enter a valid year, e.g. 1990.")


def read_year_range():
    while True:
        start_year = read_year("Start year: ")
        end_year = read_year("End year: ")
        if start_year <= end_year:
            return start_year, end_year
        print("Start year must not be after end year.")


def read_country(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Please enter a country name.")
