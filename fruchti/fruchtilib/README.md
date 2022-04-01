# This project is no longer maintained.

As I mainly work with Horizon now, this library will no longer receive updates.

# fruchtilib

This is my KiCAD component library, which I use exclusively for all my projects.
It was created because I found the default KiCAD component library pretty ugly
and wanted to have prettier schematics. This actually is the third revision of
the library and the basic structure will now stay more or less the same (as it
is more or less consistent by now). I might still change one or the other
component, so don't be upset if a commit of mine moves a pin of an existing part
and screws up your schematics (this is rare, but occasionally I come across a
flaw I want to wipe out).

That said, feel free to use this library for anything you want to use it for,
but be aware that I will not assume any liability for anything. If you use a
component library of some guy on the internet for a critical application without
checking and there is a mistake somewhere in the library and things go wrong in
your design it might just be your fault.

However, if a commit changes the structure of the library, renumber pads or do
anything which might break your projects, I will explicitly mark it and
elaborate the changes I made.

## Known issues

 - Some SMD pads miss the solder paste layer pads (although I think I fixed most
   of them by now). Please be extra-careful when ordering a SMT stencil!
