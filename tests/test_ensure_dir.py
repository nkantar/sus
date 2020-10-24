from pathlib import Path

from src import sus
from src.sus import _ensure_dir


def test_ensure_dir_not_found(mocker):
    mock_rmtree = mocker.patch("src.sus.rmtree")
    mock_path_mkdir = mocker.patch.object(sus.Path, "mkdir")

    _ensure_dir(Path("foo"))

    mock_rmtree.assert_called_once_with(Path("foo"))
    mock_path_mkdir.assert_called_once()


def test_ensure_dir_exists(mocker):
    mock_rmtree = mocker.patch("src.sus.rmtree", side_effect=FileNotFoundError())
    mock_path_mkdir = mocker.patch.object(sus.Path, "mkdir")

    _ensure_dir(Path("foo"))

    mock_rmtree.assert_called_once_with(Path("foo"))
    mock_path_mkdir.assert_called_once()
