def fileToString(fileName):
    file = open(fileName, "r")
    fileContent = file.read()
    return fileContent

def parser(fileName):
    fileContent = fileToString(fileName)
    filesNamesList = []
    contentByLinesLines = fileContent.splitlines()
    for line in contentByLinesLines:
       if "<a href" in line:
           fileName = line.split('"')[1]
           filesNamesList.append(fileName)
    return filesNamesList

def crawler(dic, fileName):
    fileNamesList = parser(fileName)
    dic[fileName] = parser(fileName)
    if(fileNamesList == []):
        return
    for file in fileNamesList:
        if file not in dic:
            crawler(dic, file)

def makeFile(dic):
    with open('results.csv', 'w') as f:
        for key in dic.keys():
            f.write("%s" % (key))
            for value in dic[key]:
                f.write("," + value)
            f.write("\n")


print("Enter source file")
fileName = input()
dic = {}
crawler(dic, fileName)
makeFile(dic)
print("Enter file name")
fileName = input()
sortedList = dic[fileName]
sortedList.sort()
print(sortedList)


