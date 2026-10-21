import unittest
from datetime import datetime
from unittest.mock import patch

import analysis
from models import EVARecord
from preparation import filter_by_year, match_country, parse_records
from user_input import read_year, read_year_range


def make_record(year, hours, country, crew=""):
    return EVARecord(datetime(year, 1, 1), hours, country, crew)


RECORDS = [
    make_record(1990, 2.0, "USA", "Alice;Bob"),
    make_record(1995, 6.0, "USA", "Alice"),
    make_record(2000, 4.0, "Russia", "Carol"),
    make_record(2005, 8.0, "Russia", "Carol;Bob"),
    make_record(2010, 3.0, "USA", "Dave"),
]


class CompareCountriesTests(unittest.TestCase):
    def test_counts_totals_averages_and_leader(self):
        stats, leader = analysis.compare_countries(RECORDS, "USA", "Russia")
        self.assertEqual(stats["USA"], {"count": 3, "total_hours": 11.0, "average_hours": 11.0 / 3})
        self.assertEqual(stats["Russia"], {"count": 2, "total_hours": 12.0, "average_hours": 6.0})
        self.assertEqual(leader, "Russia")

    def test_tie_when_totals_equal(self):
        records = [make_record(2000, 5.0, "USA"), make_record(2000, 5.0, "Russia")]
        _, leader = analysis.compare_countries(records, "USA", "Russia")
        self.assertIsNone(leader)

    def test_country_with_no_evas_has_zero_and_no_average(self):
        stats, leader = analysis.compare_countries(RECORDS, "USA", "China")
        self.assertEqual(stats["China"], {"count": 0, "total_hours": 0, "average_hours": None})
        self.assertEqual(leader, "USA")

    def test_start_and_end_years_are_included(self):
        records = filter_by_year(RECORDS, 1995, 2005)
        stats, _ = analysis.compare_countries(records, "USA", "Russia")
        self.assertEqual(stats["USA"]["count"], 1)
        self.assertEqual(stats["Russia"]["count"], 2)

    def test_empty_period_is_a_tie_with_zeros(self):
        records = filter_by_year(RECORDS, 1960, 1964)
        stats, leader = analysis.compare_countries(records, "USA", "Russia")
        self.assertEqual(stats["USA"]["count"], 0)
        self.assertIsNone(stats["Russia"]["average_hours"])
        self.assertIsNone(leader)


class ExistingAnalysisTests(unittest.TestCase):
    def test_classify_duration_boundaries(self):
        self.assertEqual(analysis.classify_duration(3.99), "Short")
        self.assertEqual(analysis.classify_duration(4.0), "Standard")
        self.assertEqual(analysis.classify_duration(6.99), "Standard")
        self.assertEqual(analysis.classify_duration(7.0), "Long")

    def test_category_counts(self):
        self.assertEqual(analysis.category_counts(RECORDS), {"Short": 2, "Standard": 2, "Long": 1})

    def test_top_crew(self):
        self.assertEqual(analysis.top_crew(RECORDS, 2), [("Carol", 12.0), ("Bob", 10.0)])

    def test_cumulative_hours(self):
        _, totals = analysis.cumulative_hours(RECORDS)
        self.assertEqual(totals, [2.0, 8.0, 12.0, 20.0, 23.0])


class InvalidInputTests(unittest.TestCase):
    def test_parse_records_skips_incomplete_records(self):
        raw = [
            {"date": "2000-01-01T00:00:00", "duration": "1:30", "country": "USA"},
            {"date": "2000-01-02T00:00:00", "duration": "", "country": "USA"},
            {"duration": "2:00", "country": "Russia"},
        ]
        records = parse_records(raw)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].duration_hours, 1.5)

    def test_unknown_country_is_not_matched(self):
        self.assertIsNone(match_country("Atlantis", ["Russia", "USA"]))
        self.assertEqual(match_country(" usa ", ["Russia", "USA"]), "USA")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["abc", "", "1999"])
    def test_read_year_retries_until_valid(self, mock_input, mock_print):
        self.assertEqual(read_year("Year: "), 1999)
        self.assertEqual(mock_input.call_count, 3)

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["2010", "2000", "2000", "2010"])
    def test_read_year_range_rejects_start_after_end(self, mock_input, mock_print):
        self.assertEqual(read_year_range(), (2000, 2010))
        mock_print.assert_called_with("Start year must not be after end year.")


if __name__ == "__main__":
    unittest.main()
