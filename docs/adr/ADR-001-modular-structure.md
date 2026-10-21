# ADR 001: Split the script into responsibility-based modules

**Context:** All the code was in one script. It mixed reading, validation, analysis, presentation and control, its sections shared global variables and tuples, and importing it ran everything, so nothing could be tested.

**Alternatives:**
1. Keep one file and wrap the code in functions.
2. Split it into modules by responsibility.
3. Use a single `EVADataset` class.

**Decision:** Option 2.

**Rationale:** Option 1 still breaks the "no single file" rule. Option 3 would put loading, analysis and display back together in one class. Option 2 separates the five concerns and makes each part testable.

**Consequences:** The code is easier to test and extend. The trade-offs are more files to manage and the fact that several modules depend on `models.py`.
