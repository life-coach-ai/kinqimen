# Testing Instructions

## General
- Use **pytest** exclusively
- Avoid command-line test scripts and ad-hoc test runners
- Tests are run from the project root using `pytest`

## Unit Tests
- Unit tests follow a **1:1 mapping** between source files and test files:
src/<module>.py → tests/unit/test_<module>.py


- When adding unit tests, **extend the existing test file** instead of creating new ones
- Do **not** create additional unit test files unless a **new source module** is introduced
- Prefer logical grouping inside a test file (e.g. classes or sections) over splitting files

## Integration Tests
- Integration tests live under: tests/integration/


- Integration tests may span multiple modules and test cross-module behavior or pipelines

## Fixtures and Shared Setup
- Shared test data, helpers, and setup belong in:
- `tests/fixtures/`
- `tests/conftest.py`
- Reuse fixtures instead of duplicating setup logic in individual tests

## Test Evolution (Recommended)
- If functionality changes, **update existing tests** rather than duplicating or parallelizing them
- Tests should assert **behavior and contracts**, not internal implementation details
