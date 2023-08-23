"""
WorldKey
Dev: Surgat

                                                     @#@@@@@@@#@
                                                &@@,@           @,@@&
                                             @@.                     ,@@
                                           @&                           @@
                                         %@
                                        &@
                                        @
                                       &@
                @@@@@@                 &@
            .@@*      @@&              &@
          *@             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         /@                            &@
         &@                            &@
         .@                            &@
           @&           .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
             #@@%,   @@@               &@
                  @@@@                 &@
                                       &@
                                       &@                                     %@@
                                       &@                  @@                    @*
                                       &@                 @. @*                  #@
                                       &@               ,@.   @#                .@,
                                       &@@@@@@@@@@@@@@@/@@@@@@@@&@@@@@@@@@@@@@@@@#
                                                      #@        @@
                                                     @@          &@
                                                    @@            (@
                                                    @%@@@@@@@@@@@@@@@
"""
import sys
import os
import subprocess
import signal

#globals
interface = subprocess.getoutput(["ip a | grep wlp| awk '{print $9}'|grep wlp"])

'''
--Description--
This part of the program will run an automated exploit output recived from survey

--Return--
This function will return an 1 if an error is encountered and a 0 for successful output 

--Parameters--

'''
def SetUp():
    ret = 0
    global interface
    try:
        os.system("airmon-ng start "+ interface)
    except:
        print("Could not open Airmon")
        ret = 1
'''
--Description--
This part of the program will run an automated wireless survey 

--Return--
This function will return an 1 if an error is encountered and a 0 for successful output 

--Parameters--

'''
def Survey():
    ret = 0
    global interface
    try:
        overwatch = subprocess.Popen(['/bin/xterm','-e','airodump-ng','--gpsd','--band','abg','-w','worldkeyscan.csv','--output-format','csv',interface+"mon"])
        hold = input("Survey In progress press enter to complete:")
        os.kill(overwatch.pid, signal.SIGINT)
        os.system("airmon-ng stop "+ interface+"mon")
    except:
        print("Could not open Airodump")
        os.system("airmon-ng stop "+ interface+"mon")
        ret = 1
    return ret

'''
--Description--
This part of the program will run an automated exploit output recived from survey

--Return--
This function will return an 1 if an error is encountered and a 0 for successful output 

--Parameters--

'''
def Exploit():
    print ("Exploit")

def main():
    SetUp()
    Survey()

if __name__ == '__main__':
    main()