# Blender Add-on (L-system)

#### Herramientas(core)
![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)
![Blender](https://img.shields.io/badge/Blender-4.4.3+-F5792A?logo=blender&logoColor=white) 

#### Repositorios
- [L-system](https://github.com/krljg/lsystem)

- [Blender-Addon-Template](https://github.com/doramgajo/blender-addon-template)

- [Lpy](https://github.com/openalea/lpy/tree/master)
- [Lpy-Docs](https://lpy.readthedocs.io/en/latest/)

- [PlantGL and L-Py Jupyter widgets](https://github.com/fredboudon/plantgl-jupyter)

##### Guias Paleobotany
- [Extinct_plants](https://github.com/PaleoNate/extinct_plants)

This is a place for the paleobotany and paleo-art communities to find references to papers with illustrations of extinct plants.

- [Paleobotanical-3D-reconstruction-guides Public](https://github.com/robertlmenning/Paleobotanical-3D-reconstruction-guides)

Paleobotany focused guides for segmenting, editing, and animating 3D reconstructions of plant fossils

- [Paleobotany-Books](https://github.com/manjunath5496/Paleobotany-Books)

"Now, evolution is the substance of fossils hoped for, the evidence of links not seen." ― Duane T. Gish

- [Paleobotany_research](https://github.com/BenjaminVanOttenberg/paleobotany_research)

## Instalación

La guia completa se encuentra en el repositorio del [template](https://github.com/doramgajo/blender-addon-template) 

El addon esta pensado para ser **descargado como " .zip " y arrastrado al entorno de blender** para instalarse

#### Que es esto?

Este desarrollo contiene una extension de la libreria "L-system" usando 
el "addon template" como base para construir metodos enfocados en generar modelos paleobotanicos
mediante las técnicas:

- Pariente Vivo más Cercano (PVC)
- Aproximación Morfológico Estructural (AME)

[1]

### Capturas en funcionamiento
v.0.1
--- 
En esta version se implementa el desarrollo basico de un ejemplar de capsella bursa pastoris
Solo se incluyen 3 variables de influencia a la simulacion del L-system con parametros.

Capsella Bursa-Pastoris L-system simulation.
See figure 3.5 in 'Algorithmic Beauty of Plants' (http://algorithmicbotany.org/papers/abop/abop.pdf), page 74.

[3]

<p align="center">
<img src="docs/media/first_cap.webp" alt="Ejemplo del addon">
</p>

## Estructura de carpetas 

Este es un ejemplo del arbol de carpetas que podrias ver si entras a la carpeta de addons de **Blender**
<!-- > [!NOTE] -->
<pre>
4.5/scripts/
    └── addons/
        ├── addon_pre_exist.py  # Single-file add-on
        └── addon_test_folder/  # Carpeta creada por blender
            ├── __init__.py
            ├── other_module.py
            └── ...
</pre>


#### Referenceias
```
[1] Plantas fósiles e inferencia paleoclimática: aproximaciones metodológicas y algunos ejemplos para México

Hugo I. Martínez-Cabrera 
José L. Ramírez-Garduño2
Emilio Estrada-Ruiz

Boletín de la Sociedad Geológica Mexicana
Volumen 66, núm. 1, 2014, p. 41-52
```


```
[2] Modelling the Plants and Ecosystem of the Rhynie Chert (2015)
Mark Kolesza
UNIVERSITY OF CALGARY
```

```
[3] The Algorithmic Beauty of Plants
- Przemyslaw Prusinkiewicz
- Aristid Lindenmayer

With:
James S. Hanan
F. David Fracchia
Deborah Fowler
Martin J. M. de Boer
Lynn Mercer
```

```
[4] Visual models of plant development (1996)
Przemyslaw Prusinkiewicz, Mark Hammel, Jim Hananz, and Radomir Mech
Department of Computer Science University of Calgary
Calgary, Alberta, Canada
zCSIRO - Cooperative Research Centre for Tropical Pest Management
Springer-Verlag 1996
```

```
Using L−Systems for Modeling the Architecture and Physiology of Growing Trees: The L−PEACH Model Mitch Allen (2004)

Przemyslaw Prusinkiewicz
Theodore DeJong

Department of Pomology, University of California, Davis
Department of Computer Science, University of Calgary
```