import os
import csv
import psutil
import subprocess
from time import sleep
from threading import Thread
from datetime import datetime


PID = ...
INTERVAL = ...
PATH_TO_LOG_FILE = ...
PATH_TO_PROC_FILE = ...


def run() -> int:
    proc = subprocess.Popen(PATH_TO_PROC_FILE)
    print('Process started..')
    return proc.pid


def checker():
    if psutil.pid_exists(PID):
        process_check = psutil.Process(PID)
        print('Process data received!')
        while True:
            if psutil.pid_exists(PID):
                cpu = process_check.cpu_percent()
                mem = process_check.memory_info().wset
                private_mem = process_check.memory_info().private
                with open(PATH_TO_LOG_FILE, 'a+', newline='') as log:
                    wr = csv.writer(log, quoting=csv.QUOTE_ALL)
                    wr.writerow([datetime.now().isoformat(), cpu, mem, private_mem])
                sleep(INTERVAL)
            else:
                break
    print('Process has been close!')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='+', type=str, help='Path to process file')
    parser.add_argument('process', nargs='+', type=str, help='Name of process')
    parser.add_argument('interval', nargs='+', type=float, help='Query interval in seconds')
    parser.add_argument('--log', nargs='?', type=str, help='path to log')
    args = parser.parse_args()

    path_to_process = args.path[0]
    name_process = args.process[0]

    path_to_log = '' if args.log is None else args.log[0]
    name_log = f"{name_process[:-4]} - {datetime.now().strftime('%Y-%m-%d %H-%M-%S.%f')[:-3]}.csv"

    PATH_TO_PROC_FILE = os.path.join(path_to_process, name_process)
    PATH_TO_LOG_FILE = os.path.join(path_to_log, name_log)
    INTERVAL = args.interval[0]
    PID = run()

    thread_checker = Thread(target=checker, daemon=True)
    thread_checker.start()

    input('Press enter to stop..')

    exit()
