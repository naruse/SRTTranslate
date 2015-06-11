class SubInfo:
    """ This class contains info of the subtitle like the time and the text to display"""
    # E.G
    # 906
    # 00:59:15,789 --> 00:59:18,789
    # Mike's married?

    def __init__(self, index, time, text):
        self._index = index
        self._time = time
        self._text = text

    def GetIndex(self):
        return self._index

    def GetTime(self):
        return self._time

    def GetText(self):
        return self._text
    def SetText(self, newText):
        self._text = newText
