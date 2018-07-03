# Infinity Gauntlet

Bans 50% of usernames found in threads and brings balance to the subreddit. Ban duration is days until release of Avengers 4 (26th Apr, 2019) when all banned souls will be unbanned.

# Requirements
* Python 3.6 and above
* Strongest of wills

## Installing Python3

The very first requirement is having python3 installed in
your local machine, send thanks to awesome developers such that
installing python in any kind of OS is easy as breeze, let's
figure our options of installing python. In case you have python already
installed in your machine, navigate to [check if python already installed](#check_if_installed).

### Installing via Anaconda (Recommended)

[Anaconda](https://www.continuum.io/downloads) is a package-manager and does all of the nasty work
for you to install python in your local machine using good 'ol
.exe setup distribution (just like how you install any game/software)

> A small tip: Don't mess with the settings of the installer just
let it install at C: drive or whatever it chooses according to your OS as well as let it set environment variable just don't mess with it.

To install python3 just go to this link : [https://www.continuum.io/downloads](https://www.continuum.io/downloads)
and download the correct installer in accordance to your operating system,
and install python in your local machine. (remember to install python 3.6+ and not python 2.7, in short install the most latest version that they are distributing).

##### Via Python.org

Alternatively, you may also install Python from their official website at
[python.org](https://www.python.org/downloads/) and just downloading the correct installer
in accordance to your OS and installing it from there (remember to install python 3.6 and not python 2.7).


> A small tip: Don't mess with the settings of the installer just
let it install at C: drive or whatever it chooses according to your OS.

<hr>

<a name="check_if_installed"></a>
###### Checking if python was installed correctly

Once installed, you can check whether everything went correctly or not
by going to start menu and typing cmd in it and the command

    python

which would return you some information about your system and python
, looking somewhat like this indicating python is installed properly:

    Python 3.6+ |Anaconda custom (32-bit)| (default, Jul  5 2016, 11:45:57) [MSC v.1900 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Make sure it says Python 3.6+ and especially not python 2.7! In order to exit, you can press CTRL+Z and then enter.
<hr>

# Setup
* Put your username-password in `config.ini`
* [Create an app](https://ssl.reddit.com/prefs/apps/) (script) and copy the `id` & `secret` into `app_key` and `app_secret` respectively.
* add the bot which you're gonna use to do the task at bot_name in config.ini file as well
* Run `pip install -r requirements.txt` to install all dependencies

# Usage
* Run `python scraper.py` to scrape all usernames. This might take some time. (change search_limit to 1000 (max) in config.ini file)
* Run `python main.py` to snap all the ill fated out of existence
* Watch the sun rise on a grateful subreddit.

# Contributors:
* [Arion Miles (Author)](https://github.com/ArionMiles)
* [Slapbot (Author)](https://github.com/SlapBot)
* [Ali Abdoli (xXAlligatorXx)](https://github.com/xXAligatorXx)

# License
MIT License. See [LICENSE](LICENSE) file to know more.
