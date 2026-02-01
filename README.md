# File Counter - Testing Exercise

This repository contains a small Python utility and a testing exercise.
The goal is to write blackbox tests that verify the behavior of the system under test(SUT).

## System Under Test (SUT)

The SUT is `file_counter/file_counter.py`, which exposes a function `count_lines(file_path)` that lines in a file.

Tests should be written to uncover and verify correct behavior.

## Task
\- Fork the repo

\- Add tests using `pytest` that treat `file_counter` as a blackbox (do not inspect or import internal implementation details beyond the public API).

\- Create tests in `tests/test_file_counter.py` that verify

\- Create a branch in the forked repo

\- Create a PR

\- Invite Malik to the review


## How to run

Install dependencies and run tests:

`pip install -r requirements.txt`  
`pytest`

## Notes

\- Keep tests focused on observable behavior of `count_lines`.  
\- The exercise is intended to practice blackbox testing and to reveal the known bug.