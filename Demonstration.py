import Health_Reporter100 as HR100

#Define the schema for the machine
Machine_String_Schema=['Robot','Scanner','Instrument1','Instrument2']
#Define a health string for the machine based on this schema
#'Robot': 0, 'Scanner': 99, 'Instrument1': 99, 'Instrument2': 99
MachineString1='00636363'

#Define two different processes to run on the machine
#'Robot': 0, 'Scanner': 100, 'Instrument1': 96, 'Instrument2': 0
ProcessString1='00646000'
#'Robot': 0, 'Scanner': 96, 'Instrument1': 96, 'Instrument2': 48
ProcessString2='00606030'

#Decode the current health of the machine
print('Machine 1: ' + str(HR100.Decode_Status_String(Machine_String_Schema,MachineString1)))

#Determine the overall health of the machine
print('Machine1 Health: ' + str(HR100.Average_Machine_Health(MachineString1)))

#Update the health value of a single machine component
print('Changing Process String1: ' + HR100.Set_Status_String_Parameter(Machine_String_Schema, ProcessString1,'Robot',100))

#Show the health of the machine for two different processes.
print('Process1: '+ str(HR100.Generate_Success_Score(MachineString1, ProcessString1)))
print('Process2: '+ str(HR100.Generate_Success_Score(MachineString1, ProcessString2)))

