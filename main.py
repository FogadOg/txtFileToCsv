import csv

class TxtToCsv():
    def __init__(self,txtFilePath,csvSaveFilePath):
        self.txtFilePath=txtFilePath
        self.csvSaveFilePath=csvSaveFilePath
        self.startTxtToCsvConvertion()
    def startTxtToCsvConvertion(self):

        txtFile = open(self.txtFilePath+".txt", 'r')
        linesInTxtFile = txtFile.readlines()
        arrayOfLines=self.joinLinesInToArray(linesInTxtFile)
        self.saveArrayToCsv(arrayOfLines)

    def joinLinesInToArray(self,linesInTxtFile):
        #this method is to join the speaked line with the speaker
        arrayOfLines=[]
        sentance=""
        for idx,line in enumerate(linesInTxtFile):
            if "\n" in line and len(line)>2:
                sentance+=line
            else:
                arrayOfLines.append(sentance.replace("\n",""))
                sentance=""
        return arrayOfLines

    def saveArrayToCsv(self,linesInTxtFile):
        with open(self.csvSaveFilePath,"w") as file:

            csvFile=csv.writer(file)
            csvFile.writerow(["input","target"])


            previousLine=None
            for line in linesInTxtFile:
                if previousLine!=None:
                    csvFile.writerow([previousLine,line])
                    previousLine=line
                previousLine=line

            

TxtToCsv("shakespeare","shakespeareTrainingData.csv")
