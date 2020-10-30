import os
from qgis.core import QgsApplication, QgsVectorLayer, QgsProject

# add this parameter when you get Qt error about not being able to connect to display (eg when using WSL2)
os.environ["QT_QPA_PLATFORM"] = "offscreen"

# Supply path to qgis install location, default for ubuntu linux is /usr
QgsApplication.setPrefixPath("/usr", True)

# Create a reference to the QgsApplication.  Setting the second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

# Write your code here to load some layers, use processing algorithms, etc.

# get the path to a geopackage  e.g. /usr/share/qgis/resources/data/world_map.gpkg
path_to_gpkg = os.path.abspath("qgis_world_map.gpkg")
print(path_to_gpkg)

# append the layername part
gpkg_countries_layer = path_to_gpkg + "|layername=countries"
# e.g. gpkg_places_layer = "/usr/share/qgis/resources/data/world_map.gpkg|layername=countries"
vlayer = QgsVectorLayer(gpkg_countries_layer, "Countries layer", "ogr")

if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

print("---")
print(vlayer.crs())
print(vlayer.extent())
print(vlayer.featureCount())
print(list(vlayer.fields()))
print("---")
x = list(vlayer.getFeatures())
print(x[1].fields().names())
print(x[1].attributes())
print(x[1].geometry().boundingBox())
print("---")

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
