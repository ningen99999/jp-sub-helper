import mecab
import srt
import pprint

subs = "".join(srt.get_subs_text_only('[HorribleSubs] Deca-Dence - 01 [720p].srt'))

mecab_result = mecab.parse(subs, include_duplicates=False)
mecab_dict = mecab.get_mecab_grouped_by_part_of_speech(mecab_result, option='simple')


pprint.pprint(mecab_dict)
print(len(mecab_dict['名詞']))

pprint.pprint(mecab_dict['名詞'])