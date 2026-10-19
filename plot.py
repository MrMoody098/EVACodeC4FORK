import matplotlib.pyplot as plt


def plot_cumulative(dates, cumulative, totals, out_path):
    plt.plot(dates, cumulative)
    plt.title(f"USA: {totals['USA']:.1f} Hours      Russia: {totals['Russia']:.1f} Hours")
    plt.xlabel("Year")
    plt.ylabel("Cumulative EVA duration (hours)")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.show()
