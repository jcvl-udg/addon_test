import bpy

# from bpy.types import Panel

# Definir un grupo de propiedades
class CustomAddonProps(bpy.types.PropertyGroup):
    humidity = bpy.props.IntProperty(
    name="Humedad",
    description="Nivel de humedad en la escena",
    default=50, min=0, max=100
    )
    sun_hours = bpy.props.IntProperty(
        name="Horas de Sol",
        description="Número de horas de sol",
        default=8, min=0, max=24
    )
    temperature = bpy.props.IntProperty(
        name="Temperatura",
        description="Temperatura en grados Celsius",
        default=20, min=-30, max=50
    )