#Actividad 07 
#Create by chequito
#Todo usuario puede modificarlo 
ippriv=$(hostname -I)
ippub=$(curl ifconfig.me) 

nmap --script imap-brute  $ippriv >Actividad07.txt
nmap --script resolveall $ippub>>Actividad07.txt
nmap --script http-cookie-flags.nse scanme.nmap.org >>Actividad07.txt
base64 < Actividad07.txt > Actividad07_encode.txt

~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                      

