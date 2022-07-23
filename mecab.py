import MeCab


tagger = MeCab.Tagger()


def parse(text, include_duplicates=True):
    """
    Gets MeCab segmentation result from text string
    :param include_duplicates: boolean if true returned mecab list will contain original duplicates
    :param text: single text string
    :return: list, each element is segment from MeCab
    """
    parse_result = tagger.parse(text).split('\n')
    mecab_result = []
    for each in parse_result:
        mecab_result.append(each.split('\t'))
    mecab_result.pop()
    mecab_result.pop()

    if include_duplicates is True:
        return mecab_result

    return filter_duplicates(mecab_result)




def get_unique_parts_of_speech(mecab_result):
    """
    Finds and returns all unique parts of speech that occur in MeCab result
    :param mecab_result: Result from parse() function
    :return: returns list with all unique parts of speech simplified
    """
    unique_list = []
    for each in mecab_result:
        speech_type_temp = each[4].split('-', 1)[0]
        if speech_type_temp not in unique_list:
            unique_list.append(speech_type_temp)

    return unique_list


def filter_duplicates(mecab_result):
    """
    Filters out duplicate segments in mecab result from parse()
    :param mecab_result: from parse() function
    :return: filtered Me result list in same format as parse() function
    """
    unique_list = []
    filtered_list = []
    for each in mecab_result:
        if each[3] not in unique_list:
            unique_list.append(each[3])
            filtered_list.append(each)

    return filtered_list

def get_mecab_grouped_by_part_of_speech(mecab_result, option='verbose'):
    parts_of_speech = get_unique_parts_of_speech(mecab_result)

    mecab_dict = {}
    for each in parts_of_speech:
        mecab_dict.update({each: list()})

    if option == 'verbose':
        for each in mecab_result:
            mecab_dict[each[4].split('-', 1)[0]].append(each)
    elif option == 'simple':
        for each in mecab_result:
            mecab_dict[each[4].split('-', 1)[0]].append(each[3])

    return mecab_dict
