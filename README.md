# Autoclicker_Pro

Autoclicker_Pro is an advanced autoclicking tool developed in Python, designed to automate clicking tasks with both preset and randomized intervals. It's built with a user-friendly interface and provides a range of customization options to suit different user needs.

## Features

- **Set Intervals**: Users can specify exact clicking intervals in minutes, seconds, and milliseconds.
- **Random Intervals**: Introduces variability with normally distributed random delays between clicks.
- **Click Duration**: Allows users to set the duration of the clicking session.
- **Start/Stop Button**: Easy control with dedicated start and stop buttons in the GUI.
- **Key Configuration for Start/Stop**: Users can configure specific keys to start and stop the clicker.
- **Right/Left Click Configuration**: Option to choose between right and left mouse clicks.
- **User-friendly GUI**: Built with a clean and straightforward interface for ease of use, see screenshot below.

<img width="425" alt="Screenshot" src="https://user-images.githubusercontent.com/55693360/216151295-429a6177-333f-498e-af85-efca0ce8711d.PNG">

## Dependencies

Autoclicker_Pro depends on several Python libraries for its functionality. Before running the application, ensure you have the following libraries installed:

- **tkinter**: For creating the graphical user interface.
- **threading**: For managing concurrent operations.
- **pyautogui**: To control the mouse and simulate mouse clicks.
- **pynput**: To listen to and control keyboard inputs.
- **random**: To generate random numbers (used for random intervals).
- **pickle**: For saving and loading application data.

To install these dependencies, you can use the following command:

```
pip install pyautogui pynput
```

Note: `tkinter` is usually included in standard Python installations. If not present, it may need to be installed separately depending on your Python setup.

## Installation

To use Autoclicker_Pro, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/AntonGole/Autoclicker_Pro
   ```
2. Navigate to the cloned directory:
   ```
   cd Autoclicker_Pro
   ```

## Usage

To start using Autoclicker_Pro:

1. Run the `main.py` script:
   ```
   python main.py
   ```
2. Configure your preferences in the application interface.
3. Use the Start/Stop buttons or the configured keys to control the clicker.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the LICENSE file for details.
