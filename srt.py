def open_srt(file_name, encoding='utf-8'):
    """
    # Opens srt file and read sub lines
    :param file_name:
    :param encoding:
    :return:
    """
    with open(file_name, encoding=encoding) as file:
        lines = file.readlines()
    return lines


def clean_lines(lines):
    """
    Takes srt sub lines raw and format into list of each subtitle element
    each sub element includes:
    [0]number, [1]time stamp, [2]text (with new lines included from original sub)
    :param lines:
    :return:
    """
    # Create list from srt lines by splitting at \n
    line_list = []
    for line in lines:
        text = line.splitlines()
        line_list.append(text)

    # Group and separate each set of subtitles by using last empty line
    # line_group = separate subtitle with number, time stamp, text (is temporary value holder)
    # line_groups = all line_group elements in list separated and formatted
    line_group = []
    line_groups = []
    for line in line_list:
        if len(line[0]) > 0:
            line_group.append(line[0])
        else:
            if len(line_group) > 3:
                line_group[2] = '\n'.join(line_group[2:])
                del line_group[3:]
            line_groups.append(line_group)
            line_group = []

    return line_groups


def get_subs(srt_file, encoding='utf-8'):
    """
    Takes srt file and returns formatted list of subs
    :param srt_file:
    :param encoding:
    :return:
    """
    return clean_lines(open_srt(srt_file, encoding))


def get_subs_text_only(srt_file, encoding='utf-8'):
    """
    Returns list of only text lines from srt file
    :param srt_file:
    :param encoding:
    :return:
    """
    subs = get_subs(srt_file, encoding)
    sub_text_only = []
    for each in subs:
        sub_text_only.append(each[2])

    return sub_text_only
