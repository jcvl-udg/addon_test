# Blender Add-on (L-system)

## Herramientas(core)
![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)
![Blender](https://img.shields.io/badge/Blender-4.4.3+-F5792A?logo=blender&logoColor=white)

#### Repositorios usados
- [L-system](https://github.com/krljg/lsystem)

- [Blender-Addon-Template](https://github.com/doramgajo/blender-addon-template)

## Instalación

La guia completa se encuentra en el repositorio del template basico, el addon esta pensado para ser descargado como " .zip " y arrastrado al entorno de blender para instalarse

#### Que es esto?

Este desarrollo contiene una extension de la libreria "L-system" usando 
el "addon template" como base para desarrollar
la libreria esta enfocada en modelos paleobotanicos

##### Activate the addon

Search for your add-on and activate it.

<p align="center">
<img src="docs/media/blender_addon_04.webp" alt="Activate add-on">
</p>

## Custom scripts directory structure

Este es un ejemplo del arbol de carpetas que podrias ver si entras a la carpeta de addons de **Blender**
<!-- > [!NOTE] -->
<pre>
custom scripts directory/
    └── addons/
        ├── addon_exist.py      # Single-file add-on
        └── addon_test_folder/  # Folder-based add-on
            ├── __init__.py
            ├── other_module.py
            └── ...
</pre>