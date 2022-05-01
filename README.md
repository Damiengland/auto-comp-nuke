# Nuke Auto Comp
*Automation tool that is designed to speed up workflow. Using the Nuke library this tool gets the channel data from 
the selected input and shuffles out each channel into its own layer then plussing the layers back over the top of each 
other to provide fine tune image manipulation on specified channels.*

## GETTING STARTED
The first thing to do is to locate your .nuke folder. *(It is hidden by default.)*

- **Windows:** C:\ Users\< username >\.nuke
 
- **Mac:** /Users/< username >/.nuke

Look for a menu.py file.

### Installation

1. Paste the below code into the **menu.py** file located in your .nuke directory

```
# Import Custom Modules
from auto_comp_main import *

m = nuke.menu("Nuke")
m.addCommand("Python Tools/Auto Comp", "auto_comp()")
```

2. Paste the below code into the **init.py** file located in your .nuke directory

```
# Make sure you use the correct version
nuke.pluginAddPath('./auto_comp_1.0.0')
```

3. Place the auto_comp_1.0.0 folder into your .nuke directory
4. Restart Nuke.

## HOW TO USE
1. Select a multi-channeled EXR inside your node graph
2. Navigate to the Python Tools menu bar at the top of the application
3. Click the dropdown Auto Comp
4. Select layer group you want to split i.e. **lgt** or **fx**
5. Select Depth channel.
6. Click okay and wait for the magic.


## Requirements
- The Foundry - Nuke Licence


## Contact
#### Damien England
#### damien.england@icloud.com
#### [Website](http://www.damienengland.com.au) 

