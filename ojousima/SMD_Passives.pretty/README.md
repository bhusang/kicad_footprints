SMD_Passives.pretty
===================

SMD passive component footprints for kicad. Based on KiCAD footprint guidelines.

Component footprints have 5 distinct layers:
1) Pads on which components are soldered to. Pads are in layer F.Cu
Soldermask opening layer which defines parts of copper to expose as a soldering surface is auto-generated from pads. 
Solder paste layer is also auto-generated from pads.

2) Courtyard, which defines the spacing around component for tools used in soldering process. 
Couryards must not overlap each other. Courtyard is in layer F.CrtYd

3) Silkscreen layer, used for visual inspection of boards as well as a help of assembly.
Silkscreen should be visible after assembly, must not overlap pads, and must be included within couryard of component.
However, silkscreen can provide information for hand soldering which is covered after assembly, such as reference numbers or other markings for clarification. Silkscreen must provide a reference for pin 1 and reference must be completely visible after assembly.

4) Mechanical drawing, which defines mechanical dimensions of part. Mechanical drawing is in layer Dwgs.User

5) Assembly drawing, which is used to relay information of the board for assembler. Must contain a reference of part as well as a reference mark for pin 1.

Variants
========

A-, B- and C-variants are made from mechanical dimensions of components. A-variants have large pads and are handsolderable, C-variants are as tight as reasonably possible and should be only used with CNC Pick'n'Place and reflow process. B-variant is a compromise between the two. Please see IPC_7351 for details.
