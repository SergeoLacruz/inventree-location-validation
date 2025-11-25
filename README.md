[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# location validation plugin
This very simple plugin checks if there is still room in the target location
for an additional stockitem. A json container in the metadata field of the stocklocation
is used to set a maximum quantity of stock items. 

Example: A SMD reel rack usually can hold only one reel per position. The plugin 
prohibits adding a second reel to an already occupied position. 
