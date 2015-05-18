#!/usr/bin/env python
usage_text = """
LPIRC Powermeter Driver
=======================
@2015 - HELPS, Purdue University


Main Tasks:
-----------
1. Authenticate user and provide time limited token for the session.
     - Timeout is set to 5 minutes by default. 
     - If multiple attempts are made to login, all the previous data will be overwritten.

Requirements:
-------------
1. Python v2.7.3

Usage:
------
referee.py [OPTION]...
Options:
         -w, --pmip
                IP address of the powermeter in format <xxx.xxx.xxx.xxx>
                Default: 192.168.1.3

         --pmexe
                Powermeter driver executable
                Default: ./WT310.exe

         --pminf
                Powermeter interface [ETHERNET | USB]
                Default: ETHERNET

         --pmcsv
                Powermeter poll log
                Default: ./wt310.csv

         --pmmode
                Powermeter mode [RMS | DC]
                Default: DC

         --pminterval
                Powermeter update interval
                Default: 1 second

         --pmtimeout
                Powermeter session timeout in seconds
                Default: 300 seconds (5 Minutes)

         -h, --help
                Displays all the available option
"""

import getopt, sys, re, glob, os                                          # Parser for command-line options
from datetime import datetime,date,time                                   # Python datetime for session timeout
import shlex                                                              # For constructing popen shell arguments
from subprocess import Popen, PIPE                                        # Non-blocking program execution
import time                                                               # For sleep


#++++++++++++++++++++++++++++++++ Global Variables +++++++++++++++++++++++++++++++++++
this_file_path = os.path.dirname(os.path.abspath(__file__))

# WT310 Powermeter related
pm_executable = os.path.join(this_file_path, 'WT310.exe')
# WT310 Powermeter driver commands
pm_cmd_interface = '--interface'
pm_cmd_ipaddress = '--ip'
pm_cmd_timeout = '--timeout'
pm_cmd_csv = '--csv'
pm_cmd_update_interval = '--interval'
pm_cmd_mode = '--mode'
pm_cmd_hard_reset = '--init'
pm_cmd_start_integration = '--integrate'
# WT310 Powermeter driver arguments
pm_ipaddress = '192.168.1.3'
pm_interface = 'ETHERNET' #ETHERNET | USB    
pm_timeout = 300 #Seconds
pm_csv = os.path.join(this_file_path, 'wt310.csv')
pm_update_interval = 1 #Seconds
pm_mode = 'DC' # DC | RMS


# Powermeter Driver
def powermeter_driver():
    
    pm_command_line = pm_executable + "\t" + \
                      pm_cmd_interface + "\t" + pm_interface + "\t" + \
                      pm_cmd_ipaddress + "\t" + pm_ipaddress + "\t" + \
                      pm_cmd_mode + "\t" + pm_mode + "\t" + \
                      pm_cmd_timeout + "\t" + str(pm_timeout) + "\t" + \
                      pm_cmd_update_interval + "\t" + str(pm_update_interval) 


    if sys.platform == 'win32':
        pm_args = pm_command_line.split()
        print "Executing PM Command:{}\n".format(pm_args)
    else:
        pm_args = shlex.split(pm_command_line)
        print "Executing PM Command:{}\n".format(pm_args)

    # Execute command
    try:
        p = Popen(pm_args, stdin = None, stdout = PIPE, stderr = PIPE, shell = False)
    except:
        print "Power meter communication error\n"
        sys.exit(2) # Abnormal termination

    output = p.communicate()[0]
    print(p.returncode)


    return p.returncode

    

# Script usage function
def usage():
    print usage_text


#++++++++++++++++++++++++++++++++ Parse Command-line Input +++++++++++++++++++++++++++++++
# Main function to parse command-line input and run server
def parse_cmd_line():

    global pm_executable
    global pm_ipaddress
    global pm_interface
    global pm_timeout
    global pm_csv
    global pm_update_interval
    global pm_mode
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hw:", ["help", "pmip=", "pmexe=", "pminf=", "pmcsv=", \
                                                         "pminterval=", "pmmode=", "pmtimeout="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) 
        usage()
        sys.exit(2)
    for switch, val in opts:
        if switch in ("-h", "--help"):
            usage()
            sys.exit()
        elif switch in ("-w", "--pmip"):
            pm_ipaddress = val
        elif switch == "--pmexe":
            pm_executable = os.path.join(this_file_path, val)
        elif switch == "--pminf":
            pm_interface = val
        elif switch == "--pmcsv":
            pm_csv = os.path.join(this_file_path, val)
        elif switch == "--pminterval":
            pm_update_interval = int(val)
        elif switch == "--pmmode":
            pm_mode = val
        elif switch == "--pmtimeout":
            pm_timeout = int(val)
        else:
            assert False, "unhandled option"

    print "\npm_exe = "+pm_executable+\
        "\npm_ipaddress = "+pm_ipaddress+\
        "\npm_interface = "+pm_interface+\
        "\npm_csv = "+pm_csv+\
        "\npm_mode = "+pm_mode+\
        "\npm_update_interval (seconds) = "+str(pm_update_interval)+\
        "\npm_timeout (seconds) = "+str(pm_timeout)+\
        "\n"


#++++++++++++++++++++++++++++++++ Script enters here at beginning +++++++++++++++++++++++++++++++++++
if __name__ == "__main__":
    # Parse Command-line
    parse_cmd_line()
    # Call powermeter driver
    powermeter_driver()
    sys.exit() # Successful termination: Default 0
else:
    # Parse XML Config file
    print "XML Parsing not found\n"
    # parse_xml_config()
    # # Initialize global variables
    # init_global_vars()
    sys.exit() # Successful termination: Default 0
