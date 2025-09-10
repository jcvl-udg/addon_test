"""
Blender Add-on Template

Base template for developing Blender add-ons.
"""

# Standard library imports
import bpy
# Third-party imports
# Blender-Python API imports
from bpy.utils import register_class, unregister_class

# Local application imports
from .user_interface import panels
from .controller import operators

# importing props
from .controller.props import CustomAddonProps

bl_info = {
    "name": "Blender Add-on Template",
    "description": "Template used as a structured starting point for Blender addons",
    "author": "Doramas García Jorge (doramgajo)",
    "version": (0, 0, 1),
    "blender": (4, 4, 3),
    "location": "View3D > Sidebar > Blender Addon Template tab",
    "warning": "Experimental under-development add-on",
    "tracker_url": "https://github.com/doramgajo/blender-addon-template/issues",
    "category": "3D View"
}
_registrable_classes = \
    operators.registrable \
        + panels.registrable


def register():
    """Register all add-on classes in Blender."""
    register_class(CustomAddonProps)  # Register property group first
    bpy.types.Scene.custom_addon_props = bpy.props.PointerProperty(type=CustomAddonProps)
    for cls in _registrable_classes:
        register_class(cls)

def unregister():
    """Unregister all add-on classes in Blender in reverse order to avoid
    dependency issues between classes.
    """
    del bpy.types.Scene.custom_addon_props
    unregister_class(CustomAddonProps)
    for cls in reversed(_registrable_classes):
        unregister_class(cls)
