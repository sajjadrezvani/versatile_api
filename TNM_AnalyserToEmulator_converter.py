import pandas as pd

def converter(fileNameExel):

    print(fileNameExel)

    mypanda = pd.read_excel(fileNameExel, sheet_name=0 ,engine='openpyxl')
    print(mypanda.head(),'\n')

    print(' Waiting...\n        ....\n        .....\n')

    colID ='ID' 
    colData ='Data'

    fileNameTxt = 'Out_' + fileNameExel[:-5] + '.txt' 
    print( fileNameExel[:-5])
    txtFile = open(d, 'w')

    add1 = str(mypanda.loc[0,colID])+'\n'
    
    add2 = str(mypanda.loc[1,colID])+'\n'
    # txtFile.write('1\n14\n')
    # txtFile.write( str(mypanda.loc[1,colID]) +'\n')
    # txtFile.write( str(mypanda.loc[2,colID]) +'\n')
    # txtFile.write('1\n1\n2000\n10\n7\n0\n0\n0\n')

    for i in range(mypanda.shape[0]):
        cell = str(mypanda.loc[i,colData])

        isSpace = cell[-1].isspace()
        if isSpace:
            cell = '0X' + cell[:-1]
        else:
            cell = '0X' + cell
        output = cell.replace(' ',',0X')
        txtFile.write( output + '}\n')

    print(mypanda.info(),'\n')
    print(mypanda.describe(),'\n\n')

    print('Have a nice day! See you soon :)) ')

    return 'Out_'+fileNameExel[:-5]+'.txt' , add1 , add2

if __name__ == '__main__':
    print(converter('diag.xlsx'))