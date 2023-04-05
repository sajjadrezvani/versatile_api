def remover(fileNameExel):
    inputFile = open(fileNameExel,'r')
    outFile = open('Out_'+fileNameExel[:-5]+'.txt' ,'w')

    lines = inputFile.readlines()

    for line in lines:
        find = line.find('t')-3
        if find>0:
            line = line[: line.find('t')-3]
            line += '\n'
        outFile.write(line)


    inputFile.close()
    outFile.close()
    
    return 'Out_'+fileNameExel[:-5]+'.txt'