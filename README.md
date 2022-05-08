# PDR-Booking

## Project Description

This project aims to book Project Discussion Room (PDR) from NTU student portal automatically.

The project uses selenium and python.

## Demo

*Note: The demo is recorded while the project is in development. Hence, there are errors shown in the demo video, but the errors have been fixed.*

https://user-images.githubusercontent.com/43754454/167301789-477cef8f-1a6d-4247-976e-0aea06f2f6b4.mp4

## Project Setup

1. Clone this project
2. Install Python '(preferably version 3.7)'
3. Install Selenium module '(Version 3.141.0)' via:
```
pip install -r requirements.txt
```

4. Install web driver file of your browser from the relevant official website and place it in the 'main' directory of this project.

> Currently, the project supports only ['Chrome'](https://chromedriver.chromium.org/) browser.

5. Once the web driver is downloaded and added to the directory, make the relevant changes to the 'Bookingdetails.py' file.

An example of the 'Bookingdetails.py':
```
# Path to chromedriver.exe
cdpath = "PATH TO CHROMEDRIVER.EXE" # e.g. "C:\\Users\elvinlim96\PDRbooking\chromedriver"

# Enter username & Password
username = "USERNAME"
password = "PASSWORD"

# Enter domain
# Values to put: STAFF, STUDENT, ASSOC, NIESTUDENT, NIESTAFF
domain = "STUDENT"

# Enter date to book (Manual or Auto mode) [DO NOT CHANGE]
# If Auto mode, booking date is 2 days from the current date
date_mode = "auto"   # auto or manual (currently only auto mode is working)

# Start & end time (in 24-hours format, max booking of 2 hours per day)
starttime = "START TIME"
endtime = "END TIME"


# Venue
venue = "VENUE NUMBER"    # 1 to 13

# Booking details
booking_purpose = "PURPOSE OF BOOKING" # E.g. "project discussion"
no_of_users = "VALUE"   # In numeric
```

## Executing program

1. Run the following command to start the web scalper:
```
python PDRbooking.py
```

## Note

* As the project is created in March 2020, the code is outdated and may have issues running it.
* Feel free to provide feedback or any issues encourtered by opening an issue in the respository.

## Version History

* 0.1
    * Initial Release
