import os
import re

INCLUDE_PATTERN = re.compile("(/\\* *include=(.*) *\\*/)")


def bundle(html_file_path):
    """Bundle HTML file

    :param str html_file_path:
    :rtype: str
    :return: HTML text
    """
    html_in: str
    with open(html_file_path) as file:
        html_in = file.read()

    matched_list = INCLUDE_PATTERN.findall(html_in)
    html_out = html_in
    target_file_dir = os.path.dirname(html_file_path)

    for matched_all, matched_val in matched_list:
        include_path = matched_val if os.path.isabs(matched_val) else os.path.join(target_file_dir, matched_val)
        include_file_text: str
        with open(include_path) as file:
            include_file_text = file.read()

        html_out = html_out.replace(matched_all, include_file_text)

    return html_out
