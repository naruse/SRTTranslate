#
# SubTranslate Simple tool that translates subtitles.
#
# NAME:
#    SubTranslate - quickly translate subtitles from any language
#
# SYNOPSIS:
#    python main.py [sub.srt] [desired sub lang] [original sub lang]
#
#    For auto language detection:
#    python main.py [sub.srt] [desired sub lang]
#
# Notes:
#   Avoid lines with spaces in the sub
#
#   *******************************************************
#   ***** Make sure your srt file encoding is in UTF8 *****
#   *******************************************************

import sys
from enum import Enum
from Utils import Utils
from Translator import Translator


## MAIN ##
#make sure we have the correct number of args
if len(sys.argv) == 3 or len(sys.argv) == 4:
    desiredSubLang = sys.argv[2]
    originalSubLang = sys.argv[3] if len(sys.argv) == 4 else u'auto'

    parsedSubInfoList = Utils.ParseSRTFile(sys.argv[1])
    if len(parsedSubInfoList) != 0:#make sure the srt file was correctly translated
        subTranslator = Translator(parsedSubInfoList, originalSubLang, desiredSubLang)

        if(subTranslator.LanguageSupported(desiredSubLang) and subTranslator.LanguageSupported(originalSubLang)):
            print("Translating...")
            translatedSubInfo = subTranslator.Translate()
            print("Writing file to: " + desiredSubLang.upper()  + "_" + sys.argv[1] + "...")
            Utils.WriteSRTFile(desiredSubLang.upper() + "_" + sys.argv[1], translatedSubInfo)
            print("Done!")
        else:
            langs = desiredSubLang if not subTranslator.LanguageSupported(desiredSubLang) else ""
            langs += " " + originalSubLang if not subTranslator.LanguageSupported(originalSubLang) else ""
            print("ERROR: Unrecognized language(s): " + langs)
            print("""Supported languages:""")
            subTranslator.PrintSupportedLanguagesText(4)


else:
    print("""\nERROR: wrong on arguments, try:\n
      python main.py [sub.srt] [desired sub lang] [original sub lang]\n
      or for auto detect:\n
      python main.py [sub.srt] [desired sub lang]\n""")



