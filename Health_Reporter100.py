'''
this is a proposed system to allow automated systems to fingerprint
their health and report it. It also allows processes to fingerprint their
requirements, and a success probablility can be reported.

Health scores are a string of hex characters, 0= broken, 1=10% ... A=100%
Requirements are similarly scored, 0= not needed, 1-A gives minimum
acceptable pereformance level. Eg if a machine function has redundancy, or
we could accept a failure rate, then this would be scored at less than 'A'.

Converting the values to percentages and multiplying would give a 'probability
of success score.

Each machine can have a uniquely defined set of parameters, so long as it is
consistently referenced in all processes on it.

Could even combine strings for machines to apply this method to a workflow.

Eg:
Function     Health     Code
Robot        100%       A
Heaters      100%       A
Chiller      50%        5
Scanner      0%         0     DEAD!!

would give a health code of AA50

A process requiring health of AA42  would not run as the scanner is not healthy enough.

'''

def Generate_Success_Score(MachineString, ProcessString):
    rollingProbability=1
    returncode='Will Run'
    
    if len(MachineString)!=len(ProcessString):
        returncode='StringLenError'
        Probability='0'
        return returncode, '0'
    
    for x in range(0,(len(ProcessString)),2):
        processFunction=int(ProcessString[x:x+2],16)
        if processFunction!=0:
            machineFunction=int(MachineString[x:x+2],16)
            if machineFunction<processFunction:
                returncode="Will Not Run"
                rollingProbability=0
            else:
                rollingProbability=rollingProbability*(int(machineFunction)/100)
    return returncode , str(rollingProbability)

def Set_Status_String(Schema,ProcessString,key,value):
    try:
        if  0<=value <=100:
            if key in Schema:
                key_position=Schema.index(key)
                HexValue=format(value,'x')
                if len(HexValue)<2:
                    HexValue='0'+ HexValue
                    
                String_as_List=list(ProcessString)
                String_as_List[key_position]=HexValue[0]
                String_as_List[key_position+1]=HexValue[1]
                return "".join(String_as_List)
            else:
                return 'Key Error'
        else:
            return 'Value Error'
    except:
        return 'Error'
        
def Decode_Status_String(Schema,Status_String):
    Decoded_Dict={}
    n=0
    for x in range(0,(len(Status_String)),2):
        Function=int(Status_String[x:x+2],16)
        Function_Name=Schema[n]
        Decoded_Dict[Function_Name]=Function
        n+=1
    return Decoded_Dict
    

def Average_Machine_Health(Machine_String):
    Function_Sum=0
    for x in range(0,(len(Machine_String)),2):
        Function=int(Machine_String[x:x+2],16)
        Function_Sum=Function_Sum+(int(Function)/100)
    return Function_Sum / (len(Machine_String)/2)

    
Machine_String_Schema=['Robot','Scanner','Instrument1','Instrument2']    
MachineString1='00636363'

ProcessString1='00646000'
ProcessString2='00606030'

print(Decode_Status_String(Machine_String_Schema,MachineString1))
print(Average_Machine_Health(MachineString1))
print(Set_Status_String(Machine_String_Schema, ProcessString1,'Robot',11))
print(Generate_Success_Score(MachineString1, ProcessString1))
print(Generate_Success_Score(MachineString1, ProcessString2))
