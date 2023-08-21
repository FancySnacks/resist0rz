# resist0rz

Console program that calculates the value of any color-coded carbon resistor or any SMD resistor.

## Features
***

- Calculate Resistance: Input the color bands of a resistor **or** the printed value on surface of SMD resistor, and the app will calculate and display the resistance value in ohms (or convert to other multiples of uni) as well as it's upper and lower ends of tolerance range.

- Color Code Guide: Display a color table to lookup values.

- Simple and Small: Easy to use and no unnecessary features.


## Installation
***

### Prerequisites
```Python >= 3.11```  

### Package Installation


1. Open the command line tool (console) and enter the following commands

2. Clone the repository to your local machine:
   ```console
   git clone https://github.com/FancySnacks/resist0rz.git
   ```

3. Navigate to the project directory
   ```console
   cd resist0rz
   ```

4. Install the package via PIP (PIP should come installed by default, if it's not then install it)
   ```console
   pip install -e .
   ```
   
   ```Note:``` This installs current directory as a module, make sure the current directory the console is ```resist0rz```


5. Check whether the installation was complete
   ```console
   resc -h
   
### Direct package installation

The package can also be downloaded directly from repo via PIP:
   ```console
   pip install https://github.com/BagOfSnacks/IPgen.git
   ```

### Note that this program can be used without being installed as a pip, it's not a necessary step, just convenient. Feel free to omit pip commands if you want.

## Usage
***
resist0rz is a script launched via console and it also produces output to said console

### Run via entry point
If you have installed this package via PIP you can call this command from anywhere in the console

   ```console
   resc [args]
   ```

### Run resist0rz from directory
To be able to do this you must be in ./resist0rz/src/ directory

   ```console
   python3 -m resist0rz
   ```

### Example Usage
Running this command:
   
   ```console
   resc -t color -v "orange, orange, black, black, gold"
   ```

Outputs the below string to the console:

   ```console
   VALUES: [ORANGE, ORANGE, BLACK, BLACK, GOLD]
   RESISTANCE: 330 Ohm
   TOLERANCE_RANGE: 313.5 - 346.5 Ohm
   ```

### Arguments
```
usage: resc [args]

Get the resistance value of any color-coded or SMD resistor

options:
  -h, --help            show this help message and exit
  -t RESISTOR_TYPE, --type RESISTOR_TYPE
                        Type of measured resistor.
                        Depending on the type specified a different way of calculation is used.
                        Options: ['color' (default) | 'smd']
  -v RESISTOR_VALUE, --value RESISTOR_VALUE
                        Value of a given resistor, matching the chosen type.
                        'color' - string sequence of full color names (ex. 'brown,black,black').
                        Color names have to be separated by commas
                        Minimum of 3 colors for value to be calculated. (base + multiplier + tolerance)
                        'smd' - string value of a SMD type resistor. The value has to input the way it appears on the resistor's surface
```

## License
***

The code in this repository is licensed under the MIT License. See the ```LICENSE``` file for more information.