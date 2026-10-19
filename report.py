def print_categories(counts):
    total_evas = sum(counts.values())
    print(f"\nEVA duration categories ({total_evas} EVAs):")
    for category, count in counts.items():
        percentage = (count / total_evas * 100) if total_evas else 0
        print(f"  {category} {count}  ({percentage:.1f}%)")


def print_top_crew(top):
    print("\nTop 5 astronauts by EVA time:")
    for name, hours in top:
        print(f"  {name} {hours:.1f} hours")


def print_unknown_country(name):
    print(f"Warning: '{name}' was not found in the data.")


def print_country_comparison(stats, leader, start_year, end_year):
    print(f"\nCountry comparison ({start_year}-{end_year}):")
    for country, values in stats.items():
        average = values["average_hours"]
        average_text = f"{average:.1f} hours" if average is not None else "unavailable"
        print(f"  {country}: {values['count']} EVAs, {values['total_hours']:.1f} hours, average {average_text}")
    if leader is None:
        print("  Result: tie")
    else:
        print(f"  Result: {leader} has the greater total EVA duration")
