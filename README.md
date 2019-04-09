# IoT-behavior-Dataset
IoT behavior data set creation using splunk 

the structure for creation of this data set is based on the research "N-BaIoT-Network-Based Detection of IoT Botnets Attacks Using Deep Autoencoders" to create the possibility of an incrementation data set

all the information was processed using Splunk , the information was extracted in a standardized way for the future possible training of an IDS based on behavior as done in the aforementioned research

in the previous commented research 23 different features were extracted from the network packages in the network, in order to obtain in some way a standardized method and provide the possibility of an incremental data sets and training available for IDS devices based on behavior, these same 23 features were taken as a basis to be extracted, the specific extraction method is described below, as well as the use of the Splunk queries used for this.

The extraction was based on 5 different time frames which are divided into 100ms, 500ms, 1.5s, 10s and 1m, this was originally selected by the computational speed that can be given for these ranges in real-time detection methods, by the same reason these were not modified.

For each packet, these features were obtained based on the size of bytes transmitted per network packet, number of hosts observed and the mean of the packets bytes transmitted in a given period of time, taking into account the source IP, source Mac address, source IP and destination IP, the jit between the packet sent from source IP to destination IP in where the jit is the difference in time between transaction with the same IP values, the source IP and source port together with destination IP and destination port,

Splunk provides certain functions that facilitate the obtention of this type of data, the functions used for this are described below

bin: this function allows to specify the time windows to be used for the analysis of the information where it is only necessary to specify the field where the window will be used where will be applied and the time: bin _time span = 100ms

eval: this function allows the evaluation of subfunctions

len: function to calculate the length that was used, needs to be used together with the eval function to obtain the length of the sent packets: eval M=len(_raw)

Mean : function that calculates the mean of the variable that is specified: mean (M)

stdev : function that calculates the standard variation of the variable that is specified: stdev(M)

transaction: calculate the time between different events giving the opportunity to specify what to take into account to obtain these times: transaction src_ip dst_ip maxevents=2

By: statistical function that allows obtaining statistical data taking into account specific fields within the data: By _time src_ip






