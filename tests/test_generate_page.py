from pathlib import Path

from src.sus import _generate_page


def test_generate_page(mocker):
    mocker.patch("src.sus.OUTPUT_DIR", Path("test_dir"))
    _ensure_dir_mock = mocker.patch("src.sus._ensure_dir")
    _write_page_mock = mocker.patch("src.sus._write_page")

    _generate_page("foo", "<html>bar</html>")

    _ensure_dir_mock.assert_called_once_with(Path("test_dir") / "foo")
    _write_page_mock.assert_called_once_with(
        (Path("test_dir") / "foo" / "index").with_suffix(".html"), "<html>bar</html>"
    )
