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
