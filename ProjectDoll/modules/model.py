'''
model.py - Class definition of a Human Model.

Team Cloth
CSCI-4440
4/13/14

Last Updated: Bryant Pong: 4/20/14 - 2:03 PM
'''

# Blender API Libraries:
import bpy

# Model definition:
class Model:
    
    def __init__(self, height, width):
        self.height_ = height
        self.width_ = width
            
    # Accessor functions:
    def getHeight(self):
        return self.height_
    
    def getWidth(self):
        return self.width_
    
    # Modifier functions:
    def setHeight(self, newHeight):
        self.height_ = newHeight
        
    def setWidth(self, newWidth):
        self.width_ = newWidth