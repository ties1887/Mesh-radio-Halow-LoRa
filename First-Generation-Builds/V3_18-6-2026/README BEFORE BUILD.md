# Read before building V3

The V3 build is a slightly more complex build than the earlier versions, so here are some tips to help you on your way!
Please take your time and check every part carefully before assembly.

This version is still in beta. Some parts may need small adjustments, sanding, fitting, or extra work during the build.

## Important notes

* Make sure you use the correct screw lengths.
* Screws that are too long can go too deep into the frame and may cause shorts by touching internal electronics, PCB parts, or solder pads.
* When sliding the PCBs into the enclosure, there is very little tolerance. Move them in carefully and make sure you do not push off or damage any small components.
* All positive and negative power wires should be twisted together as pairs. This helps reduce electrical noise and keeps the wiring cleaner.
* It is recommended to use 16 AWG or 18 AWG wire for the main power wiring. Thicker wire has lower resistance, which helps reduce voltage drop and heat generation.
* The buck converter can generate a lot of electrical noise. It is recommended to shield/isolate the buck converter from the rest of the electronics using copper tape.
* If copper tape is used as shielding, it should be connected/soldered to ground. Make sure the copper tape cannot touch any live contacts, solder pads, or components, otherwise it can create a short.
* It is recommended to install a small heatsink kit on the Raspberry Pi.
* The rear heatsink included in the build files as a 3MF and STEP file is mainly intended for visual/reference purposes. In the BOM, there is a link to the real metal version of this heatsink. It is recommended to buy and use the metal version instead of the 3D-printed version.
* The twist-lock battery connection system is still being improved. The current pogo-pin connection will likely be replaced soon with a stronger magnetic connection that clicks in more firmly and is easier to solder.
* For the front and rear seals, there is a groove designed for a 2 mm diameter rubber cord or rubber O-ring material.
* A practical way to make these seals is to buy large rubber O-rings, cut them to the correct length, and glue the ends together.
* This should be considered water-resistant, not fully waterproof. No waterproof rating or guarantee is given.
* All parts are designed to be 3D printed without supports.<img width="993" height="1584" alt="db9d3973-dfbc-4dac-b72b-2cc7cdb6f751" src="https://github.com/user-attachments/assets/fcf75cf3-d45b-4983-ba87-7fa4130c5cd1" />
