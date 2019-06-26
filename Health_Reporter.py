'''
Same functionality as Health_Reporter100 but with health score resolution
only in intervals of 10%
'''

def Generate_Success_Score(MachineString, ProcessString):
    returncode='Will Run'
    rollingProbability=1
    StringPosition=0
    if len(MachineString)!=len(ProcessString):
        returncode='StringLenError'
        Probability='0'
        return returncode, '0'
    else:
        for x in ProcessString:
            #Only work with the functions the process needs
            if int(x,16)!=0:
                if int(x,16)>int(MachineString[StringPosition],16):
                    #if the Process requires a Function score higher than the machine has, Fail
                    returncode='Will not run'
                else:
                    #Calculate a liklihood of success.
                    rollingProbability=rollingProbability*(int(MachineString[StringPosition],16)/10)
            StringPosition += 1
            
        if returncode=='Will not run':
            return returncode, '0'
        if returncode=='Will Run':
            return returncode, str(rollingProbability)
            
 
MachineString1='AAAAAAAA00' #Everything is working except for two functions.
MachineString2='AAA9988776' #This machine has some unhealthy functions.

ProcessString1='000AAA0000' #This process only needs functions 4,5,6
ProcessString2='0000AAA00A' #This process needs 5,6,7 and 10.
ProcessString3='4444444444' #This process needs everything, but we can tolerate some failure

print(Generate_Success_Score(MachineString1, ProcessString1))  #Will Run with 100% expected probability of success.
print(Generate_Success_Score(MachineString1, ProcessString2))  #Will not run
print(Generate_Success_Score(MachineString1, ProcessString3))  #Will not run
print(Generate_Success_Score(MachineString2, ProcessString1))  #Will not run
print(Generate_Success_Score(MachineString2, ProcessString2))  #Will not run
print(Generate_Success_Score(MachineString2, ProcessString3))  #Will run. with 15% expected probability of success.
