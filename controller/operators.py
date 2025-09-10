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
        # props = context.scene.lsystem_props
        try:
            mesh.primitive_cube_add()
            pruebini()
            # self.report({'INFO'}, f"Props: {str(props)}")
            self.report({'INFO'}, "Pruebini passed")
        except Exception as e:
            self.report({'ERROR'}, f"Error al llamar metodo: {str(e)}")
        return {"FINISHED"}

class ADDONNAME_OT_create_capsella(Operator):
    """Operador para crear un ejemplo de capsella_bursa."""
    bl_idname = "addonname.create_capsella"
    bl_label = "Simular Planta"
    def execute(self, context):
        props = context.scene.lsystem_props
        # humidity = props.humidity
        # sun_hours = props.sun_hours
        # temperature = props.temperature
        self.report({'INFO'}, f"Propsn: {str(props)}")
        return {"A friend like me"}

registrable = [
    ADDONNAME_OT_create_cube,
    ADDONNAME_OT_create_capsella
]