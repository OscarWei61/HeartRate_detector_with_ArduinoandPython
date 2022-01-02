<div id="top"></div>


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

</div>


## Syllabus of Contents

- [Syllabus of Contents](#syllabus-of-contents)
- [Introduction Of Project](#introduction-of-project)
  - [Features](#features)
  - [Develop With](#develop-with)
- [Python code introduction](#python-code-introduction)
- [Installation](#installation)
- [License](#license)
- [Developer Contact](#developer-contact)


## Introduction Of Project

Use Arduino and Python create a heartrate detector.

### Features

- Read Arduino signal
- use filter to deal with noise
- Calculate heartrate
- Show Electrocardiography


### Develop With

* [Python](https://www.python.org/)
* [Arduino](https://www.arduino.cc/)

<p align="right">(<a href="#top">back to top</a>)</p>


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
#### 4.install tkinter
```
  conda install -c anaconda tk
```
*  We are using verion = 8.6.11

<p align="right">(<a href="#top">back to top</a>)</p>


## Python code introduction
#### 1.Pulse_plot.py
We create a signal process code to handle arduino heart rate data.
Since the data readed from Arduino is not the correct heart rate number.
We use filter to deal with noise and turn the data into correct Heart rate.
After all to math function and filter , we print out the instant heart rate and use Maplotib to show the user their Electrocardiography.

#### 2.HeartRate_detector with tkinter.py
We think the most of people do not have the professional knowlegde to understand how Electrocardiography word.People only know what Electrocardiography look like when someone is dead.So we create a small UI program with promptly showing your heartrat and serval buttons.The button with "Analyse" is able to compare your heartrate with standard data.There will be a small windows pop up after you click the "Analyse" buttom.Show how is your heartrate and Is there anything you should notice.After seeing the result，you can just close the small windows and click the "Quit" buttom.After that the program will automatically close.

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


## Developer Contact

MING-YI WEI - wei573434@gmail.com
XUAN-YIN CHEN - B10832039@gapps.ntust.edu.tw

Project Link: [https://github.com/Cwei61/HeartRate_detector_with_ArduinoandPython](https://github.com/Cwei61/HeartRate_detector_with_ArduinoandPython)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Cwei61/HeartRate_detector_with_ArduinoandPython.svg?style=for-the-badge
[contributors-url]: https://github.com/Cwei61/HeartRate_detector_with_ArduinoandPython/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Cwei61/HeartRate_detector_with_ArduinoandPython.svg?style=for-the-badge
[forks-url]: https://github.com/Cwei61/HeartRate_detector_with_ArduinoandPython/network/members
[stars-shield]: https://img.shields.io/github/stars/Cwei61/HeartRate_detector_with_ArduinoandPython.svg?style=for-the-badge
[stars-url]: https://github.com/Cwei61/HeartRate_detector_with_ArduinoandPython/stargazers
[issues-shield]: https://img.shields.io/github/issues/Cwei61/HeartRate_detector_with_ArduinoandPython.svg?style=for-the-badge
[issues-url]: https://github.com/Cwei61/HeartRate_detector_with_ArduinoandPython/issues
[license-shield]: https://img.shields.io/github/license/Cwei61/HeartRate_detector_with_ArduinoandPython.svg?style=for-the-badge
[license-url]: https://github.com/Cwei61/HeartRate_detector_with_ArduinoandPython/blob/master/LICENSE
