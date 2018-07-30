# TODO open file in webbrowser when finished
# TODO give it a Gooey GUI
# TODO use the variable of the html file to convert to get the path to that file so images work

import sys
from re import sub
from lxml.html.clean import Cleaner

def cleanup_html(html_to_clean):

    cleaner = Cleaner(
        page_structure=False,
        meta=False,
        style=True,
        inline_style=True,
        annoying_tags=True,
        remove_unknown_tags=True,
        safe_attrs_only=True,
        safe_attrs=frozenset(["src", "href", "content", "http-equiv"]),
        remove_tags=("span", "body"),
        # kill_tags=("title",)
        # processing_instructions=True,
        # embedded=True,
        # links=True,
        # scripts=True,
        # javascript=True,
        # comments=True,
        # frames=True,
        # forms=True,
    )

    html_to_clean = cleaner.clean_html(html_to_clean)
    return html_to_clean


def regex_cleanups(html_to_clean):
    html_to_clean = sub(r"&nbsp;", "", html_to_clean)
    html_to_clean = sub(r"<p>(\s*)</p>", "", html_to_clean)
    html_to_clean = sub(r"\n", "", html_to_clean)
    html_to_clean = sub(r"\s\s+", " ", html_to_clean)
    html_to_clean = sub(r" <", "<", html_to_clean)
    return html_to_clean


if __name__ == "__main__":

    with open(sys.argv[1]) as html:
        html = html.read()

    html = cleanup_html(html)
    html = regex_cleanups(html)

    with open("cleaned_html.html", "w") as output_file:
        output_file.write(html)
