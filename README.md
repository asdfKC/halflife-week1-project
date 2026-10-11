### halflife-week1-project
For this project, I made a Macropad!

My components used are listed in BOM.md 


 This is an image of the 3d view of the PCB
<img width="1252" height="691" alt="image" src="https://github.com/user-attachments/assets/6a5b8083-c142-4fd9-b6fe-80be4ef79861" />



This is an image of the PCB Gerber files!

 <img width="684" height="299" alt="image" src="https://github.com/user-attachments/assets/57521186-ade6-4ead-8bfb-76745852437d" />


This is my first pcb ever!


## GPIO USAGE:
It starts at GPIO0


| Switch | GPIO |
|---|---|
| 1 | GP0 |
| 2 | GP1 |
| ... | ... |
| 18 | GP17 |

The middle goes in numerical order.

## Firmware =D
The firmware is in 'firmware/code.py.' It uses KMK on CircuitPython.


## Switch plate :D

A pretty basic and simple plate is included in the plate/ directory. It has 18 cutouts that match the PCB, each the size of a standard MX switch cutout. The outline is in plate/Plates/plate_Edge_Cuts.dxf

<img width="1082" height="457" alt="image" src="https://github.com/user-attachments/assets/d48d8446-62fb-4e6d-9b3c-2df1205e1ee5" />

I provided an STL file in the plate/ directory called plate.stl.

<img width="689" height="256" alt="image" src="https://github.com/user-attachments/assets/386fa20f-ca0e-4a61-b1a2-2ef31c288db3" />
