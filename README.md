# One Pick Killer V2

New and improved One Pick Killer. Automatically syncs with time server (time2.kriss.re.kr)
and doesn't need manual time-syncing.

Tested on Windows and MacOS

## Setup
Clone repository. Use the Download button (green) or clone by
```
git clone https://github.com/numpee/OnePickKillerV2
```
If you used download, unzip into any folder of your choice.

On terminal (or Command or Anaconda Prompt on Windows), change directory to the source folder. 
```
cd path_to_directory
```

Create a new virtual environment and install the requirements.

```
pip install -r requirements.txt
```


## Run 

Set the time with command-line parameters, and run the program!
For example, if the Sugang time is 9:00:00 AM, then:

```
python main.py --hour 9 --minute 0 --second 0
```

**On MacOS Mojave, you may need to run with sudo permissions**

Good luck~~