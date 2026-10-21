# Architectural changes for the country comparison FR

Implementing the country comparison required two changes to the structure from ADR 001.

## 1. Preparation split into parsing and filtering

**Before:** `prepare_records(raw, start, end)` parsed records and filtered by year in one step.

**After:** `parse_records(raw)` and `filter_by_year(records, start, end)`.

**Why:** Detecting an unknown country needs every country in the dataset, not only those in the selected years. Parsing once and filtering afterwards avoids loading the data twice or hardcoding a country list.

## 2. New `user_input.py` module

**Why:** Invalid years, a start year after the end year, and blank country names must not crash the program. Putting this validation in `main.py` would mix input handling with coordination.

