"""
Blender Add-on Template

Blender Add-on operators module.
"""

# Blender-Python API imports
from bpy.types import Operator
from bpy.ops import mesh

# importing local libs
from .test import pruebini
import lsystem
from ..lsystem.examples.capsella_bursa_pastoris import simulate_capsella

from ..lsystem.examples.capsella_pro import simulate_capsella as simulate_capsella_pro

class ADDONNAME_OT_create_cube(Operator):
    """Operator to create a primitive cube in the scene."""
    bl_idname = "addonname.create_cube"
    bl_label = "Create cube"

    def execute(self, context):
        props = context.scene.custom_addon_props
        self.report({'INFO'}, f"Humidity: {props.humidity}, Sun Hours: {props.sun_hours}, Temperature: {props.temperature}")
    # Crear un objeto de ejecución del sistema L
        exc = lsystem.exec.Exec()
                # Ejecutar la simulación
        try:
            simulate_capsella_pro(
                exc, 
                humidity=props.humidity, 
                sun_hours=props.sun_hours, 
                temperature=props.temperature,
            )
            self.report({'INFO'}, "Friend like me!")
        except Exception as e:
            self.report({'ERROR'}, f"Error al generar la planta: {str(e)}")
        return {"FINISHED"}

class ADDONNAME_OT_create_capsella(Operator):
    """Operador para crear un ejemplo de capsella_bursa."""
    bl_idname = "addonname.create_capsella"
    bl_label = "Simular Planta"
    def execute(self, context):
        props = context.scene.custom_addon_props
        self.report({'INFO'}, f"Humidity: {props.humidity}, Sun Hours: {props.sun_hours}, Temperature: {props.temperature}")
    # Crear un objeto de ejecución del sistema L
        ex = lsystem.exec.Exec()
                # Ejecutar la simulación
        try:
            simulate_capsella(
                ex, 
                humidity=props.humidity, 
                sun_hours=props.sun_hours, 
                temperature=props.temperature,
            )
            self.report({'INFO'}, "Friend like me!")
        except Exception as e:
            self.report({'ERROR'}, f"Error al generar la planta: {str(e)}")
        
        return {'FINISHED'}

registrable = [
    ADDONNAME_OT_create_cube,
    ADDONNAME_OT_create_capsella
]