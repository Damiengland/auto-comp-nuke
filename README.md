#Nuke Auto Comp
*Automation tool that is designed to speed up workflow. Using the Nuke library this tool gets the channel data from 
the selected input and shuffles out each channel into its own layer then plussing the layers back over the top of each 
other to provide fine tune image manipulation on specified channels.*

##GETTING STARTED
The first thing to do is to locate your .nuke folder. *(It is hidden by default.)*

- **Windows:** C:\ Users\< username >\.nuke
 
- **Mac:** /Users/< username >/.nuke

Look for a menu.py file.

###Option 1 - Copy File
1. Copy contents on this projects **main.py** and paste at bottom of **.nuke/menu.py**
2. Restart Nuke Application

###Option 2 - Reference File
1. Create a folder inside the **.nuke** folder called scripts
2. Copy & paste this projects **main.py** in the folder
3. Import the **main.py** into the **.nuke/menu.py**

   `from ./scripts/main.py import *`
4. Paste the *Add to nuke menu bar* code from the bottom of this projects **main.py** into **.nuke/menu.py**

    `m = nuke.menu("Nuke")`

    `m.addCommand("Python Tools/Auto Comp", auto_comp)`

##HOW TO USE
1. Select a multi-channeled EXR inside your node graph
2. Navigate to the Python Tools menu bar at the top of the application
3. Click the dropdown Auto Comp
4. Select layer group you want to split i.e. **lgt** or **fx**
5. Select Depth channel.
6. Click okay and wait for the magic.


##Requirements
- The Foundry - Nuke Licence


##Contact
####Damien England
####damien.england@icloud.com
####[Website](http://www.damienengland.com.au) 

