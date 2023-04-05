from TNM_EmuCollapser import collapser
from TNM_AnalyserToEmulator_converter import converter
from TNM_TimeRemover import remover
from TNM_EmuCorrector import corrector

def collector(inputName,checkbox , firstBox='' , secBox='\n'):

    ''' 
    txt -> exel
    14 -> 500
    13 -> 250
    11 -> 125
    191 -> 104000 
    '''

    exelToTxt = {'500':'14', '250':'13', '125':'11' , '104000':'191' }

    add1 = ''
    add2 = ''
    fileFormat = inputName.split('.')[1]
    fileFormat = fileFormat.lower()
    
    if fileFormat == 'xlsx':
        isExel = True
        inputName, add1 , add2 = converter(inputName)
    elif fileFormat == 'txt':
        isExel = False
        if checkbox == 'on':
            inputName = remover(inputName)

    if not firstBox=='' :
        comma = firstBox.index(',')
        firstCode = firstBox[:comma]
        secondCode = firstBox[comma+1:]
        add1 = firstCode+'\n'
        add2 = secondCode+'\n'
    else:
        firstCode = ''
        secondCode = ''
        

    if not secBox=='\n':
        try:
            rate = exelToTxt[secBox]+'\n'
        except:
            rate = '14    // you should set this number by baudrate: (500:14, 250:13, 125:11 , 104000:191) \n'

    # print(int(exelToTxt[secBox]),'>>>>>>>>>>' , inputName,'-------',rate,firstCode,secondCode)
    outName , kwp_rate = collapser(inputName, add1 , add2 , rate ,isExel)
    print('################' , kwp_rate)
    if int(kwp_rate) < 20:
        outName = corrector(outName)
        
    print(outName)
    return outName

if __name__ == '__main__':
    collector('diag.xlsx')