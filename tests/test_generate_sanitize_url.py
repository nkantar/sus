from sus.sus import _sanitize_url


def test_sanitize_url_nothing() -> None:
    url = "https://example.com/foo"
    sanitized_url = _sanitize_url(url)

    assert sanitized_url == "https://example.com/foo"


def test_sanitize_url_single_quote() -> None:
    url = "https://example.com/foo'bar"
    sanitized_url = _sanitize_url(url)

    assert sanitized_url == "https://example.com/foo%27bar"
