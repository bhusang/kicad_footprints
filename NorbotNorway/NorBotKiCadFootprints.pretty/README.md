# NorBotKiCadFootprints.pretty
Our custom PCB footprints for KiCad (www.kicad-pcb.org)

## How to add to KiCad ##

1. Open the Footprint Editor->Preferences->Footprint Libraries Wizard
2. Choose GitHub repository, set 'https://github.com/NorbotNorway', and click 'Next'.
3. Select all .pretty libraries in the list

If you want to make changes/add new footprints to this library then you need to tell KiCad where to save the new .kicad_mod files.

1. Footprint Editor->Preferences->Footprint Libraries Manager
2. Select the 'NorBotKicadFootprints' library at the bottom of the list, and click 'Options Editor' button.
3. Select 'allow_pretty_writing_to_this_dir' and click 'Append selected option'.
4. In the value field type in a local path that ends with .pretty, for example 'e:\git\NorBotFootprints.pretty'. 
If that folder is an existing clone of the GitHub repo it is easy to commit the new footprints.
