# Kicad_Footprint_Connectors.pretty
The footprints that I have made

## Instruction:
To make these footprints work with corresponding libraries, use the following setings in 'Footprint Libraries Manager'
 - Nickname this library = My_Connectors
 - Library Path = https://github.com/Gijsco/Kicad_Footprint_Connectors.pretty
 - Plugin Type = Github
 
Or make them local in your project with 3D files
 - In your project folder make a folder named 'My_Connectors.pretty'
 - Copy all your project specific footprints to My_Connectors.pretty
 - In your project folder make a folder named '3D'. Note the Capital D, this is important because some footprints here reffer to a 3D file in this specific 3D folder located in your project folder.
 - Copy your project specific .wrl files to the folder named '3D'.
 - In Kicad use Footprint Libraries Wizzard and add My_Connectors.pretty to your footprint library list. In the last step of the Wizard select 'To the current project only'.
