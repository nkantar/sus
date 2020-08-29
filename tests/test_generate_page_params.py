from src.sus import _generate_page_params


def test_generate_page_params_easy():
    line = "foo|https://example.com/foo"
    slug, html = _generate_page_params(line)

    assert slug == "foo"
    assert (
        html == "<meta http-equiv='refresh' content='0;url=https://example.com/foo' />"
    )


def test_generate_page_params_pipe():
    line = "foo|https://example.com/foo|bar"
    slug, html = _generate_page_params(line)

    assert slug == "foo"
    assert (
        html
        == "<meta http-equiv='refresh' content='0;url=https://example.com/foo|bar' />"
    )


def test_generate_page_params_quote():
    line = "foo|https://example.com/foo'bar"
    slug, html = _generate_page_params(line)

    assert slug == "foo"
    assert (
        html
        == "<meta http-equiv='refresh' content='0;url=https://example.com/foo%27bar' />"
    )
