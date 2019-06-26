System Health Reporter

This idea is intended for use in laboratory automation, however it may be
apliccable in other contexts.

It is difficult to clearly state the health of complex automation systems
when they have the capability to conduct a variety of tasks. This is because
all the functions may be in working order to conduct one task, but another task
on the same system may be impossible due to an element of the required 
functionality being broken.
The machine is therefore simultaneously 100% available, and 0% available,
depending on who needs to use it.

this is a proposed system to allow automated systems to fingerprint
their health and report it. It also allows processes to fingerprint their
requirements, and a success 'probablility' can be reported.

Health scores are a string of hex characters, 0= broken, 0A=10% ... 64=100%
Requirements are similarly scored, 0= not needed, 1-64 gives minimum
acceptable pereformance level. Eg if a machine function has redundancy, or
we could accept a failure rate, then this would be scored at less than '64'.

Converting the values to percentages and multiplying would give a guideline
'probability of success' score.

Each machine can have a uniquely defined set of parameters, so long as it is
consistently referenced in all processes on it according to its schema.


Eg:
Function     Health     Code
Robot        100%       64
Storage      100%       64
Instrument1      50%        32
Instrument2      0%         0     DEAD!!

would give a health code of 64643200

A process requiring health of 64000016  would not run as Instrument2 is not healthy enough.

There should be no practical limit to the number of components in a machine,
however pragmatism and an overall understanding of the system should be a guide.
It is even possible to combine strings for machines to apply this method to a multi-system
workflow.

This system could be applied in a variety of ways, either from a central repository, or
from the machine itself via an API. If machine learning is employed to provide failure 
prediction, or predictive maintenance, then this could automatically change the health
scores for the functions, Potentially on a time sensitive basis, eg this week Robot is 100%
healthy, next week it is predicted to be 75%, and the week after 50% healthy.

