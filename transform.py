import os
import sys
import subprocess

# Set Blender installation path
BLENDER_PATH = r"C:\Program Files\Blender Foundation\Blender 4.4\blender.exe"

# Ensure a .blend file path is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python transform.py <blend_file_path>")
    sys.exit(1)

# Get the input .blend file path from the argument
INPUT_BLEND = sys.argv[1]

# Define the output directory
OUTPUT_DIR = r"C:\Users\umash\My project\Assets\models"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define the output .obj file path
blend_filename = os.path.basename(INPUT_BLEND).replace(".blend", ".obj")
OUTPUT_OBJ = os.path.join(OUTPUT_DIR, blend_filename)

# Temporary Blender script content
blender_script = f"""import bpy

# Load the Blender file
bpy.ops.wm.open_mainfile(filepath=r"{INPUT_BLEND}")

# Export to OBJ format
bpy.ops.wm.obj_export(filepath=r"{OUTPUT_OBJ}")

print(r"Exported successfully: {OUTPUT_OBJ}")
"""

# Save the script as a temporary file
script_path = os.path.join(os.getcwd(), "temp_export_script.py")
with open(script_path, "w", encoding="utf-8") as script_file:
    script_file.write(blender_script)

try:
    # Run Blender in background mode to execute the script
    subprocess.run([BLENDER_PATH, "--background", "--python", script_path], check=True)
    print(f"Successfully exported: {OUTPUT_OBJ}")  # Explicitly print the output path
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")

# Clean up temporary script
os.remove(script_path)
