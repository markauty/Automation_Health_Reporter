

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

def Set_Status_String_Parameter(Schema,ProcessString,key,value):
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
