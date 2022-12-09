# From https://github.com/alexandrebarachant/muse-lsl/blob/master/examples/startMuseStream.py
from muselsl import stream, list_muses, muse
import multiprocessing as mp
import threading
from gui import GenerateUI
import pandas as pd
import os, sys

def start_stream():
    muses = list_muses()

    if not muses:
        print('No Muses found')
        #persists no connection to GUI
        connectionCSV = pd.DataFrame(['Not Connected'])
        print(connectionCSV.head())
        connectionCSV.to_csv('/home/pi/Desktop/Method2/connection.csv')
    else:
        try:
            #persists connection to GUI
            connectionCSV = pd.DataFrame(['Connected'])
            print(connectionCSV.head())
            connectionCSV.to_csv('/home/pi/Desktop/Method2/connection.csv')
            #calls Muselsl stream
            stream(str(muses[0]['address']))

            # Note: Streaming is synchronous, so code here will not execute until the stream has been closed
        except(KeyboardInterrupt):
            print('Stream has ended')


if __name__ == "__main__":
    #starts the UI process
    t1 = mp.Process(target=GenerateUI, args=())
    t1.start()
    start_stream()
    #appends working directory to path
    sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
    print("Working Directory added to path")

    sys.path.append(os.getcwd())
    sys.path.append('/home/pi/Desktop/MuseAlarm/waveloading.gif')
    sys.path.append('/home/pi/Desktop/MuseAlarm/checklist.png')
    print("Working Directory added to path")

    connectionCSV = pd.DataFrame(['Not Connected'])
    print(connectionCSV.head())
    connectionCSV.to_csv('/home/pi/Desktop/Method2/connection.csv')

    stopAlarmCSV = pd.DataFrame([''])
    stopAlarmCSV.to_csv('/home/pi/Desktop/Method2/alarmStop.csv')

