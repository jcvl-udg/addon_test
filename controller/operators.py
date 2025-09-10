"""
Blender Add-on Template

Blender Add-on operators module.
"""

# Blender-Python API imports
from bpy.types import Operator
from bpy.ops import mesh

from .test import pruebini


class ADDONNAME_OT_create_cube(Operator):
    """Operator to create a primitive cube in the scene."""
    bl_idname = "addonname.create_cube"
    bl_label = "Create cube"

    def execute(self, context):
        props = context.scene.lsystem_props
        mesh.primitive_cube_add()
        pruebini()
        self.report({'INFO'}, f"Props: {str(props)}")
        return {"FINISHED"}


registrable = [
    ADDONNAME_OT_create_cube,
]
