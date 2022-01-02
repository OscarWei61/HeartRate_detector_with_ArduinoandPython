# HeartRate_detector_with_ArduinoandPython
Use Arduino and Python create a heartrate detector.

## Installation

#### 1.install Matplotib
```
  conda install -c conda-forge matplotlib
```
*	 We are using version = 3.5.1
#### 2.install Serial
```
  conda install -c anaconda pyserial
```
*	 We are using version = 3.4
#### 3.install Scipy
```
  conda install -c anaconda scipy
```
*	 We are using version = 1.7.1

## Python code introduction
#### 1.Pulse_plot.py
We create a signal process code to handle arduino heart rate data.
Since the data readed from Arduino is not the correct heart rate number.
We use filter to deal with noise and turn the data into correct Heart rate.
After all to math function and filter , we print out the instant heart rate and use Maplotib to show the user their Electrocardiography.

#### 2.HeartRate_detector with tkinter.py
We think the most of people do not have the professional knowlegde to understand how Electrocardiography word.People only know what Electrocardiography look like when someone is dead.So we create a small UI program with promptly showing your heartrat and serval buttons.The button with "Analyse" is able to compare your heartrate with standard data.There will be a small windows pop up after you click the "Analyse" buttom.Show how is your heartrate and Is there anything you should notice.After seeing the result，you can just close the small windows and click the "Quit" buttom.After that the program will automatically close.
