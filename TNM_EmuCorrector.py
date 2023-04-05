
def corrector(txt_name): # this file cleans the shit of EmuCollapser! :)
    import re
    # filename1 = 'E:\Other computers\MyLaptop\FlyDrive\python\Versatile_api\VersatilOut_Out_engineezam.txt'
    filename1 = txt_name
    file1= open(filename1,'r')
    inputEmu=file1.readlines()

    # filename2= 'E:\Other computers\MyLaptop\FlyDrive\python\Versatile_api\VersatilOut_DIAG_uni.txt'
    filename2 = 'Versatil_' + txt_name
    file2 = open(filename2,'w')
    # file2.write(inputEmu)
    firstIndexLast = ''
    fileTxt = ''
    lastLine = ''
    # print(inputEmu)
    for i in inputEmu:
        comList = list(re.finditer(',',i))
        print(i , '>>>>>' , firstIndexLast)
        if( len(comList)>1 ):   # a few initial line for all files are OK and could pass this if condition

            till3 = i[:comList[1].start()+7]    #few chars first of every lines 

            # remove two 0x22 command next to each other
            if (firstIndexLast == i[:i.index(',')] or i=='0X7f,0X22,0X31}\n') and len(i)<18:

                firstCommaIndex = list(re.finditer(',',lastLine))[0].start()
                thirdCommaIndex = list(re.finditer(',',lastLine))[1].start()+4
                additional = ',0X18,0X99,0X18,0X99}    //  -> 4 byte (1899) was added by SRK!\n'
                firstOfLast = '0X62' + lastLine[ firstCommaIndex : thirdCommaIndex+1 ] + additional ####### Warning 
                file2.writelines(firstOfLast)
                print('---mode 1')
                if(firstIndexLast == i[:i.index(',')]): #specially check for 
                    file2.writelines(i)
                    print('---mode 2')


            elif ( till3 in fileTxt ) and len(i)>16: # remove lines which are repetative frame and diffrent answer for same command
                print('---mode 3')
                continue

            elif ( i== '0X7f,0X22,0X78}\n'):        # remove 7f_78 fault 
                print('---mode 4')
                continue

            else:       #otherwise this line is clean! write it!
                file2.writelines(i)
                print('---mode 5')

            firstIndexLast = i[:i.index(',')]  


        else:
            file2.writelines(i)
            firstIndexLast = i
            print('---mode 6')


 
        lastLine = i
            

        fileTxt += i

    file1.close()
    file2.close()

    return 'Versatil_'+txt_name


