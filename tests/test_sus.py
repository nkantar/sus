from pathlib import Path
from unittest.mock import Mock, call, patch

from sus.sus import sus


@patch("sus.sus.OUTPUT_DIR", Path("test_dir"))
@patch("sus.sus._ensure_dir")
@patch(
    "sus.sus._read_input",
    return_value=[
        "foo|https://example.com/bar",
        "baz |  https://example.com/barf",  # spaces are intentional
    ],
)
@patch(
    "sus.sus._generate_page_params",
    side_effect=[
        ["foo", "<html>bar</html>"],
        ["baz", "<html>barf</html>"],
    ],
)
@patch("sus.sus._generate_page")
def test_sus(
    _generate_page_mock: Mock,
    _generate_page_params_mock: Mock,
    _read_input_mock: Mock,
    _ensure_dir_mock: Mock,
) -> None:
    sus()

    assert _ensure_dir_mock.call_args_list == [call(Path("test_dir"))]
    assert _read_input_mock.call_args_list == [call()]
    assert _generate_page_params_mock.call_args_list == [
        call("foo|https://example.com/bar"),
        call("baz |  https://example.com/barf"),  # spaces are intentional
    ]
    assert _generate_page_mock.call_args_list == [
        call("foo", "<html>bar</html>"),
        call("baz", "<html>barf</html>"),  # note lack of spaces
    ]
