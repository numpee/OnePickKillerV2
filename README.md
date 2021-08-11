# One Pick Killer V2 

![](https://img.shields.io/badge/python-3.6+-blue.svg)

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

Create a new python virtual environment and install the requirements. Virtualenv is preferred, but Anaconda works as well.

```
pip install -r requirements.txt
```


## Run 

Set the time with command-line parameters, and run the program!
For example, if the Sugang time is 9:00:00 AM, then:

```
python main.py --hour 9 --minute 0 --second 0
```

**You may have to run python with Administrator priveledges on Windows. On MacOS (Mojave +), you need to run python with sudo permissions**

```
sudo python main.py ...
```

Good luck :smile:
