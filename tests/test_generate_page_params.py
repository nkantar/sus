from sus.sus import _generate_page_params


def test_generate_page_params_easy() -> None:
    line = "foo|https://example.com/foo"
    slug, html = _generate_page_params(line)

    assert slug == "foo"
    assert (
        html == "<meta http-equiv='refresh' content='0;url=https://example.com/foo' />"
    )


def test_generate_page_params_pipe() -> None:
    line = "foo|https://example.com/foo|bar"
    slug, html = _generate_page_params(line)

    assert slug == "foo"
    assert (
        html
        == "<meta http-equiv='refresh' content='0;url=https://example.com/foo|bar' />"
    )


def test_generate_page_params_quote() -> None:
    line = "foo|https://example.com/foo'bar"
    slug, html = _generate_page_params(line)

    assert slug == "foo"
    assert (
        html
        == "<meta http-equiv='refresh' content='0;url=https://example.com/foo%27bar' />"
    )


def test_generate_page_params_whitespace() -> None:
    line = "\tfoo  |\nhttps://example.com/foo "
    slug, html = _generate_page_params(line)

    assert slug == "foo"
    assert (
        html == "<meta http-equiv='refresh' content='0;url=https://example.com/foo' />"
    )
