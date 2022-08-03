#!/usr/bin/env python
# The script must be run on a machine with python version 3.10+

import glob
import shutil
import os
import time
import datetime
import argparse


# get command line arguments
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s" ,"--source", help="Insert source path")
    parser.add_argument("-r", "--replica", help="Insert replica path")
    parser.add_argument("-l", "--log", help="Insert log path")
    parser.add_argument("-i", "--interval", help="Please insert sync interval in seconds", type=int)
    args = parser.parse_args()
    if not args.source:
        parser.error("[-] Please specify the path to the source folder")
    elif not args.replica:
        parser.error("[-] Please specify the path to the replica folder")
    elif not args.log:
        parser.error("[-] Please specify the path to the log folder")
    elif not args.interval:
        parser.error("[-] Please specify the sync interval")
    return args


# get timestamp for the log
def get_timestamp():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S %d-%m-%Y")
    return current_time


def backup():
    arguments = get_arguments()
    log_file_path = os.path.join(arguments.log, 'log_file.txt')
    log_file = open(log_file_path, 'a')  # creates the log file at the specified location
    for source_file in glob.glob('*', root_dir=arguments.source):  # iterates through the source folder's files
        if source_file not in glob.glob('*', root_dir=arguments.replica):  # verify the file existence in replica folder
            file_name_source = arguments.source + "/" + source_file
            file_name_replica = arguments.replica + "/" + source_file
            shutil.copyfile(file_name_source, file_name_replica)  # copy file to replica folder
            print(get_timestamp() + " >> File " + source_file + " was added to destination folder")
            log_file.writelines(get_timestamp() + " >> File " + source_file + " was added to destination folder" + "\n")

    for replica_file in glob.glob('*', root_dir=arguments.replica):
        if replica_file not in glob.glob('*', root_dir=arguments.source):
            remove_replica_file = arguments.replica + "/" + replica_file  # create replica file path
            os.remove(remove_replica_file)
            print(get_timestamp() + " >> File " + replica_file + " was removed from replica folder")
            log_file.writelines(get_timestamp() + " >> File " + replica_file + " was removed from replica folder" + "\n")
    log_file.close()
    time.sleep(arguments.interval)


while True:
    backup()