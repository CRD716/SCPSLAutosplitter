# SCPSLAutosplitter

## How to use (Quick)

Install python, and run `pip install Pillow` and `pip install Pynput` </br>
Settings in Livesplit needed (you can go in the code and change stuff if you want to customize): </br>
Split hotkey: F7 </br>
Reset hotkey: F6 </br>

You may want to set the start time to ~a quarter of a second as it takes a small amount of time by default for the program to check if you've started.

Run the .py file

# How to install (Long)

Install the latest version of python from https://www.python.org/downloads/ </br>
Remember to check the "Add to PATH" box when installing! </br>
Open Command Prompt on windows, and Terminal on Linux. </br>
Enter `pip install Pillow` and after `pip install Pynput`. </br>
In Livesplit, set the Split hotkey to F7, and the Reset Hotkey to F6. </br>
Edit Splits> Start Timer at: 0.1 </br>
Double click/run the .py file. </br>
Start up a round, it should split once when you spawn in as d class. </br>
There is a 15 second cooldown from the first split until you can reset. </br>

## FAQ/Troubleshooting

It's not detecting my start! : Go in and mess with the ranges, as well as the getpixel(x,y) values. It will have to be trial and error. </br>
The detection is too slow. : In the sleep() at the bottom of the page, lower the number. </br>
Have you ever heard the tragedy of Darth Plagius the Wise? : </br>
