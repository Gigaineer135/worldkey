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
'''
--Description--
This part of the program will run an automated exploit output recived from survey

--Return--
This function will return an 1 if an error is encountered and a 0 for successful output 

--Parameters--

'''
def SetUp():
    print ("SetUP")


'''
--Description--
This part of the program will run an automated wireless survey 

--Return--
This function will return an 1 if an error is encountered and a 0 for successful output 

--Parameters--

'''
def Survey():
    ret = 0
    try:
        overwatch = subprocess.Popen(['/bin/xterm','top'])
        hold = input("Survey In progress press enter to complete:")
        os.kill(overwatch.pid, signal.SIGINT)
    except:
        print("Could not open Airodump")
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
    print(Survey())
    Exploit()

if __name__ == '__main__':
    main()