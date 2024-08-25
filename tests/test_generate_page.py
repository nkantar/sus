from pathlib import Path

from pytest_mock import MockerFixture

from sus.sus import _generate_page


def test_generate_page(mocker: MockerFixture) -> None:
    mocker.patch("sus.sus.OUTPUT_DIR", Path("test_dir"))
    _ensure_dir_mock = mocker.patch("sus.sus._ensure_dir")
    _write_page_mock = mocker.patch("sus.sus._write_page")

    _generate_page("foo", "<html>bar</html>")

    _ensure_dir_mock.assert_called_once_with(Path("test_dir") / "foo")
    _write_page_mock.assert_called_once_with(
        (Path("test_dir") / "foo" / "index").with_suffix(".html"),
        "<html>bar</html>",
    )
