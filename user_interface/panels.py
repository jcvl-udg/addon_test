"""
Blender Add-on Template

Blender Add-on panels module.
"""

# Blender-Python API imports
import bpy
from bpy.types import Panel

# Local application imports
from ..controller.operators import ADDONNAME_OT_create_cube , ADDONNAME_OT_create_capsella

# importing props
from ..controller.props import CustomAddonProps

class ADDONNAME_PT_main_panel(Panel):
    """Main panel for the Blender Add-on."""
    bl_category = "Blender Addon"
    bl_label = "Blender Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        pass


class ADDONNAME_PT_tools(Panel):
    """Panel for tools related to the Blender Add-on."""
    bl_parent_id = "ADDONNAME_PT_main_panel"
    bl_label = "Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_order = 1

    def draw(self, context):
        layout = self.layout
    # Controles de la simulación
        scene = context.scene
        layout.prop(scene.custom_addon_props, "humidity")
        layout.prop(scene.custom_addon_props, "sun_hours")
        layout.prop(scene.custom_addon_props, "temperature")
        layout.separator()
        layout.operator(
            ADDONNAME_OT_create_cube.bl_idname,
            text="Create cube", icon="CUBE")
        layout.separator()
        layout.operator(
            ADDONNAME_OT_create_capsella.bl_idname,
            text="Simular Plante", icon="CUBE")


registrable = [
    ADDONNAME_PT_main_panel,
    ADDONNAME_PT_tools,
    CustomAddonProps
]
