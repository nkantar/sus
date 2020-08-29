from pathlib import Path
from unittest.mock import call

from src.sus import sus


def read_input_mock():
    return ["foo|https://example.com/bar", "baz|https://example.com/barf"]


GENERATE_PAGE_PARAMS_MOCK_RETURNS = [
    ["foo", "<html>bar</html>"],
    ["baz", "<html>barf</html>"],
]


def test_sus(mocker):
    mocker.patch("src.sus.OUTPUT_DIR", Path("test_dir"))
    _ensure_dir_mock = mocker.patch("src.sus._ensure_dir")
    _read_input_mock = mocker.patch("src.sus._read_input", side_effect=read_input_mock)
    _generate_page_params_mock = mocker.patch(
        "src.sus._generate_page_params", side_effect=GENERATE_PAGE_PARAMS_MOCK_RETURNS
    )
    _generate_page_mock = mocker.patch("src.sus._generate_page")

    sus()

    _ensure_dir_mock.assert_called_once_with(Path("test_dir"))
    _read_input_mock.assert_called_once()
    assert _generate_page_params_mock.call_count == 2
    _generate_page_params_mock.assert_has_calls(
        [call("foo|https://example.com/bar"), call("baz|https://example.com/barf")]
    )
    assert _generate_page_mock.call_count == 2
    _generate_page_mock.assert_has_calls(
        [call("foo", "<html>bar</html>"), call("baz", "<html>barf</html>")]
    )
