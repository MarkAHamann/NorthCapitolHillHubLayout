# North Capitol Hill Emergency Communication Hub Layout

This repository is to maintain a LibreCAD version of a layout for the hub located at the Seventh Day Adventist Church at 13-14th and Aloha near Volunteer Park.

## Issues
1) Create an issue at https://github.com/MarkAHamann/NorthCapitolHillHubMap/issues

## What you need to do your own updates
* Install LibreCAD. The version used is:
```
Version: 2.2.0.2
Compiler: GNU GCC 13.1.0
Compiled on: Jul 29 2023
Qt Version: 5.12.11
Boost Version: 1.75.0
System: Windows 10 (10.0)
```
* Install git for your platform

* Get a token to make updates (ask Mark Hamann)

## LibreCAD usage and gotchas
LibreCAD is free. But it's hard to learn and use. Here are some hints to help you.

### Scales
This units of the coordinate system are in feet. The printing scale of the text and most lines is 0.5mm (ISO). The dotted lines on the tents that indicate the open to the public side are "Dots(tiny) and 0.25mm.

### General practice for best results for noobs (yes I'm a noob)
If you make a mistake, ctrl-Z. For example, don't add something, then delete it if you don't want it. Add it and ctrl-Z to remove it.
Minimize the number of visible layers.
Unlock no more than one layer at a time.
Close block editing windows a print preview windows when you are done with them.
If LibreCAD starts acting funny, close it and reopen.
Work on small change sets--e.g.e at a time. Once it is complete, save the map.dxf file and commit it to git.
If you've committed things to git and you have royally screwed up, close LibreCAD, run  `git checkout .` and reopen to get back to the state it was in when you last did the git commit.
Black and white are special. Don't use them because they get swapped. Instead use custom colors that are close enough to be considered black and white. These are not swapped.

### Layers
Each role and item is on its own layer. In many cases the color associated with a layer is fixed by the hub leadership. Click the color field in the `eye, lock, hash, color` area. If you want black or white, you cannot use black or white because for some reason, when you go to print or export the image, LibreCAD swaps black and white. Instead of white (#ffffff) use e.g. #fcfcfc by setting the individual colors to 250. With black (#000000) use #050505 by setting the rbg colors each to 5.

In general keep all layers locked at all times. Only unlock the layer you're currently editing and ensure that its eye indicated it is visible AND that the layer name is **bold-face**. If the lines and text seem unresponsive, recheck the **bold** layer and the lock icon.

There are 3 image layers:
* a google maps satellite view
* a faded google map satellite view
* a google map default view
These are aligned with each other. They can be swapped in and out.

Sometimes an item you add to a layer disappears behind one of the map layers when you make the map layer visible. To fix that, hide the map layer, select the item, one the menu, go to Modify>Order>Bring to Top.

### Blocks
Some items that are repeating are blocks. Blocks are tricky to learn, but here are some hints.

When editting an existing block, select it in the Blocks view and edit in another window. There will be a tab to the left of the main work area with the name of the block and it will be selected. In the layers tab, unview all layers except for layer 0 at the top. Ensure that it is unlocked, the only visible layer, and the **0** is **bold**. The blocks are done near the origin, zoom out until you see the small + and then zoom in on that.Make your edits.

When the block looks right, view a layer containing the block to ensure that the change looks right.

When the block is done, close the block tab, hide layer 0, and relock it.

## Exporting your image
Once things look good and you want to export, you have few options. It seems like you could export a .png or .jpg, but that export method doesn't honor the line widths and the text is unreadable. The current only option is to export as pdf.

To do that, make all the layers invisible including the map image layer. Then make all the layers you want to show visible.
Now use File>Print Preview...

This will open a tab that shows your items and a white sheet of paper. It will be auto scaled to about 1:600-ish in the scale box just above the main window. Adjust this in the little dropdown text box about 1:300. Do not use the drop-down--just type in 1:300.

Grab the sheet of paper and place it so that all of the items you want to show are on it. Adjust the scale to 1:350 or something if they don't fit anymore.

Now in the layer section, unhide the map you want to use. This will hide the sheet of paper.

Now export as pdf. with File>Export>Export as PDF. Name it something logical. I use YYYYMMDD_HHMM.pdf and place it in ./deliverables.

Once the PDF looks good. Close the print preview window.
