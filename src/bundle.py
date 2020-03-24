import os
import re

INCLUDE_PATTERN = re.compile("(/\\* *include=\"(.*)\" *\\*/)")


def bundle(src_file_path, dst_file_path=None, encoding='utf-8'):
    """Bundle HTML file

    :param str src_file_path: Source file path
    :param str dst_file_path: Destination file path. Output text to this path if this is not None
    :param str encoding: Encoding of all. All files must be encoded with same encoding
    :rtype: str
    :return: HTML text
    """
    html_in: str
    with open(src_file_path, mode="r", encoding=encoding) as file:
        html_in = file.read()

    matched_list = INCLUDE_PATTERN.findall(html_in)
    html_out = html_in
    target_file_dir = os.path.dirname(src_file_path)

    for matched_all, matched_val in matched_list:
        include_path = matched_val if os.path.isabs(matched_val) else os.path.join(target_file_dir, matched_val)
        include_file_text: str
        with open(include_path, mode="r", encoding=encoding) as file:
            include_file_text = file.read()

        html_out = html_out.replace(matched_all, include_file_text)

    if dst_file_path is not None:
        with open(dst_file_path, mode="w", encoding=encoding) as file:
            file.write(html_out)

    return html_out
