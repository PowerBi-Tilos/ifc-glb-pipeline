import bpy
import sys
import ifcopenshell

# --- Parse Arguments ---
argv = sys.argv
argv = argv[argv.index("--") + 1:] if "--" in argv else []
ifc_path = argv[0]
output_glb_path = argv[1]

# --- Reset Scene ---
bpy.ops.wm.read_factory_settings(use_empty=True)

# --- Import IFC ---
bpy.ops.import_scene.ifc(filepath=ifc_path)

# --- Extract GUIDs ---
model = ifcopenshell.open(ifc_path)
for obj in bpy.context.scene.objects:
    if "IfcGuid" in obj:
        guid = obj["IfcGuid"]
        obj["ifc_guid"] = guid  # Add as GLB metadata

# --- Export GLB with extras ---
bpy.ops.export_scene.gltf(
    filepath=output_glb_path,
    export_format='GLB',
    export_extras=True
)

print(f"Exported GLB with GUIDs to {output_glb_path}")
