# ADR 002: Test analysis as pure functions with unittest

**Context:** The analysis needs automated tests with known results. The original code could only be checked by running it by hand.

**Alternatives:**
1. Test the whole program by feeding it input and comparing its printed output.
2. Use `pytest`.
3. Use the standard library's `unittest` on the analysis functions, with in-memory records.

**Decision:** Option 3.

**Rationale:** The restructuring made the calculations pure functions, so they can be tested directly with exact expected values. `unittest` needs no install, which follows the "no unnecessary dependencies" rule.

**Consequences:** The tests are fast and don't depend on the JSON data or matplotlib. They don't check the plot output or the full input flow, and `unittest` is a bit more verbose than `pytest`.
