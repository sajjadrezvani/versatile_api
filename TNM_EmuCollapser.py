import os , time , shutil


def collapser(txt_name , add1='' , add2='' , rate='\n' , isExel=True):

    print("Hi! welcome to TNM emulator collapser by Sajjad Rezvani.K ... \n   watting...   \n   ....\n   .....\n\n")


    filename1=txt_name
    folderName = os.getcwd()
    oldAddress = os.path.join(folderName , filename1)
    newAddress = os.path.join(folderName , 'copy'+filename1)
    print('\n----', newAddress,oldAddress)
    shutil.copyfile(oldAddress , newAddress )

    file1= open(filename1,'r+')
    inputEmu=file1.read()

    inputEmu=inputEmu+"\n"

    filename2='api_'+txt_name
    file2 = open(filename2,'w')

    if isExel==True:
        file2.write('1\n')
        file2.write(rate)
        file2.write(add1)
        file2.write(add2)
        file2.write('1\n1\n2000\n10\n7\n0\n0\n0\n')
    else:
        kwp_rate = inputEmu.split('\n')[1]
        firstX = inputEmu.find('0x')
        initCodes = inputEmu[:firstX-2]
        inputEmu = inputEmu[firstX:]     
        file1.write(inputEmu)
        print(initCodes)

        file2.write(initCodes)
    
    file1.close()

    while len(inputEmu)!=0:
        file1= open(filename1,'r' )
        line=file1.readline()
        file2.write(line)  # every time we put a the first line of file1 in file2
        file1.close()

        # if line!="0x7f,0x22,0x31}\n" :
        
        nextEnter=inputEmu.find("\n",0)
        while inputEmu.find(line)==0:
            inputEmu=inputEmu[nextEnter+1::]    # remove countinuously repeated line 
                
            if len(inputEmu)==0:
                break

        start= 0

        while(inputEmu.find(line,start)!=-1 and inputEmu[inputEmu.find(line,start)-1]=="\n"): # and line!="0X7f,0X22,0X31}\n"):
            lastChr=inputEmu.find(line,start)-1    
            nextEnter=inputEmu.find("\n",lastChr+1)
            inputEmu=inputEmu[0:lastChr+1:]+inputEmu[nextEnter+1::]      # remove repeated line in whole txt
            start=0


    #   inputEmu=inputEmu.replace(line,'')
    #     elif line=="0x7f,0x22,0x31}\n" :
    #         while inputEmu.find(line)==0:
    #             inputEmu=inputEmu[16::]  

        file1=open(filename1,'w')
        file1.write(inputEmu)   # update the whole file1 by inputEmu str that changes every times
        file1.close()

    file2.close()
    os.remove(filename1)
    
    print("\ngood luck! enjoy of it...\n ")
    time.sleep(5)
    
    
    
    return 'api_'+txt_name , kwp_rate

if __name__ == '__main__':
    txt_name = 'Out_diag.txt'
    collapser(txt_name )