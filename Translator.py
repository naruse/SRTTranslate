import goslate

class Translator:
    """ This class contains all the translation logic. """
    def __init__(self, subList, fromLang, toLang):
        self._subInfoList = subList
        self._originalLang = fromLang
        self._translatedLang = toLang
        self._gs = goslate.Goslate()
        self._supportedLanguages = self._gs.get_languages()

    def Translate(self):
        """ returns a subInfoList with the subtitles translated. """
        linesPerTranslation = 250 if 250 < len(self._subInfoList)-1 else len(self._subInfoList)-1
        separationToken = "[[[[[]]]]]"#if change token, make sure that the token is not spaced after translation.
        text = ""
        counter = 0
        globCounter = 0
        translatedTexts = [] #contains the translated strings from the srt
        for subInfo in self._subInfoList:
            text = text + subInfo.GetText() + separationToken
            if(counter>=linesPerTranslation) or (linesPerTranslation >= ((len(self._subInfoList)-1)-globCounter) and ((globCounter+1) == len(self._subInfoList))):#we translate by batches
                text = text[:-len(separationToken)]#cut the last token
                translatedSubs = self._gs.translate(text, self._translatedLang, self._originalLang)
                translatedSubsList = translatedSubs.split(separationToken)

                translatedTexts.extend(translatedSubsList)
                counter = 0
                text = ""
            counter += 1
            globCounter += 1

        #print(str(len(self._subInfoList)) + " =? " + str(len(translatedTexts)))
        translatedSubInfoList = self._subInfoList
        i = 0
        for subInfo in translatedSubInfoList:
            subInfo.SetText(translatedTexts[i])
            i += 1

        return translatedSubInfoList

    #@staticmethod better not static so we can cache the supported langs
    def LanguageSupported(self, string):
        if string == u'auto':
            return True
        else:
            return True if string in self._supportedLanguages else False

    #TODO: make _supportedLanguages static
    def PrintSupportedLanguagesText(self, langsPerLine):
        counter = 1
        langs = ""
        for key, value in self._supportedLanguages.items():
            line = str(key).ljust(5) + ": " + str(value).ljust(25)
            langs += line + ('\n' if counter%langsPerLine == 0 else '')
            counter += 1
        print(langs)

