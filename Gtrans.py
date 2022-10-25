import pandas as pd
import googletrans
from googletrans import Translator

lang = googletrans.LANGUAGES
langData = pd.DataFrame(list(lang.keys()), columns=["ShortName"])
langData['LanguageName'] = langData['ShortName'].apply(lambda x: lang[x])

laShort = [(i) for i,j in lang.items()]
laFull = [(j) for i,j in lang.items()]

def GetLanguages():
    finalLangDict = {}
    cnt = 1
    langdict = dict(langData.values)
    for x, y in langdict.items():
        a1 = {'ShortName':x, 'LanguageName':y}
        finalLangDict[cnt] = a1
        cnt+=1
    return finalLangDict


# Creating an instance
translator = Translator()

# translator.translate('This is so nice!', src='en', dest='mr').text

def translation(SourceEng):
    source = SourceEng.sourceLang
    dest = SourceEng.destLang
    Sentence = SourceEng.Sentence
    if dest not in laShort:
        aa = [i for i in laFull if dest in i ][0]
        dest = laShort[laFull.index(aa)]
    tansSentencs = translator.translate(Sentence, src=source, dest=dest).text
    return {
        "TranslateFrom":source,
        "TranslateTo":dest,
        "Sentence":Sentence,
        "TranslatedSentencs":tansSentencs}

# def translation(source):
#     source = source.sourceLang
#     dest = source.destLang
#     Sentence = source.Sentence
#     tansSentencs = translator.translate(Sentence, src=source, dest=dest).text
#     return {'tansSentencs':tansSentencs}

# langData.head()