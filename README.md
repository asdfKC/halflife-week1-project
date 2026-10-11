### halflife-week1-project
For this project, I made a Macropad!

My components used are listed in BOM.md 


 This is an image of the 3d view of the PCB
<img width="1259" height="559" alt="image" src="https://github.com/user-attachments/assets/2f058ac7-d566-472c-ad9f-d72abdc83af8" />



This is an image of the PCB Gerber files!

<img width="797" height="342" alt="image" src="https://github.com/user-attachments/assets/45175c36-548a-4ae3-a1eb-59c8b084c98c" />


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


I provided an STL file in the plate/ directory called plate.stl.

<img width="635" height="293" alt="image" src="https://github.com/user-attachments/assets/b5e78658-d045-444d-a78f-d684c6bc8ebb" />
