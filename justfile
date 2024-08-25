############################################################
# All commands are to be run inside a virtual environment. #
# E.g.,                                                    #
#     uv run just lint                                     #
############################################################


# check formatting via ruff
formatcheck:
    ruff format --check .

# check docstring formatting via pydocstyle
docstylecheck:
    pydocstyle .

# check type hints via mypy
typecheck:
    mypy --strict .

# run linter via ruff
lint:
    ruff check .

# run tests via pytest
test:
    pytest -svv .

# run all checks
checkall:
    just formatcheck
    just docstylecheck
    just typecheck
    just lint
    just test
