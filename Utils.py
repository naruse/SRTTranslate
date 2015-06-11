from SubInfo import SubInfo

class Utils:
    """ This class contains utility methods, this is a static class. """
    @staticmethod
    def IsIndex(string):
        try:
            #print("\n\n" + str(string) + "  " + repr(string) + "\n\n")
            string = str(string)#make sure this is a string
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def IsTime(string):
        string = str(string)#make sure we are working with a string
        if "-->" in string:
            try:
                int(string[:2])#beginning of the line
                int(string[-3:])#end of the line
                return True
            except ValueError:
                return False
        return False

    @staticmethod
    def ParseSRTFile(fileName):
        """ Parses a file and returns a list of SubInfo. """
        result = []
        try:
            with open(fileName, 'r') as file:
                line = file.readline().strip()
                lineBefore = ''
                currentIndex = -1
                currentTime = ""
                currentText = ""
                while line != '':
                    if line != '\n':
                        lineToParse = line.strip()
                        indexFile = file.tell()# save current file index
                        nextLine = file.readline().strip()#move the index to the next line and save it
                        file.seek(indexFile)#revert back index
                        #an index is an index if the current line is an index, the line before is empty and the next line is time
                        if Utils.IsIndex(lineToParse) and lineBefore == '' and Utils.IsTime(nextLine):
                            currentIndex = int(lineToParse)
                            lineBefore = lineToParse
                            #a time line is time if the current line is time and the line before is an index
                        elif Utils.IsTime(lineToParse) and Utils.IsIndex(lineBefore):
                            currentTime = lineToParse
                            lineBefore = lineToParse
                        else:
                            currentText = ""
                            while lineToParse !=  '':
                                currentText = currentText + lineToParse + '\n'
                                lineToParse = file.readline().strip()

                            result.append(SubInfo(currentIndex, currentTime, currentText))

                    lineBefore = lineToParse
                    line = file.readline()
                    #we have a line that only has spaces, so just readline
                    while(len(line) > 0 and len(line.strip()) == 0):
                        lineBefore = line.strip()
                        line = file.readline()
        except FileNotFoundError:
            print("\n", fileName, "was not found.\n did you write correctly the sub name?\n")
            return []

        return result

    @staticmethod
    def WriteSRTFile(fileName, subInfoList):
        file = open(fileName, 'w')
        for subInfo in subInfoList:
            file.write(str(subInfo.GetIndex()) + '\n')
            file.write(subInfo.GetTime() + '\n')
            file.write(subInfo.GetText().strip() + '\n\n')

