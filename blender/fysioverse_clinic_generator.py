# Fysioverse Blender Asset Generator
# Open this script in Blender's Scripting workspace and Run Script.
# It creates a lightweight stylised low-poly clinic asset pack designed for web export.
import bpy
from mathutils import Vector

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def mat(name, color):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.diffuse_color=(*color,1)
    return m

def cube(name, loc, scale, material):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o=bpy.context.object; o.name=name; o.scale=scale; bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); o.data.materials.append(material); return o

def cyl(name, loc, radius, depth, material):
    bpy.ops.mesh.primitive_cylinder_add(vertices=16,radius=radius,depth=depth,location=loc)
    o=bpy.context.object; o.name=name; o.data.materials.append(material); return o

green=mat('Fysio Green',(0.13,0.74,0.55)); wood=mat('Warm Wood',(0.62,0.39,0.22)); blue=mat('Care Blue',(0.25,0.55,0.88)); pink=mat('Patient Pink',(0.90,0.35,0.48)); dark=mat('Screen Dark',(0.08,0.14,0.16)); white=mat('Clinic White',(0.96,0.98,0.97))

# Reception
cube('Reception_Desk',(0,0,0.45),(1.4,0.35,0.45),wood)
cube('Reception_Screen',(0,-0.38,1.05),(0.35,0.05,0.22),dark)

# Treatment bed
cube('Treatment_Bed',(3,1.3,0.52),(0.85,0.32,0.12),wood)
cube('Treatment_Pillow',(2.25,1.3,0.66),(0.18,0.30,0.05),white)

# Exercise mat and ball
cube('Exercise_Mat',(4.8,1.3,0.06),(0.45,0.72,0.04),green)
bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, radius=.22, location=(4.8,.55,.25))
ball=bpy.context.object; ball.name='Exercise_Ball'; ball.data.materials.append(pink)

# Plant
cyl('Plant_Pot',(-1.1,.2,.18),.22,.35,wood)
cyl('Plant_Stem',(-1.1,.2,.62),.04,.8,green)
for x,y,z in [(-1.3,.2,.8),(-.9,.2,.85),(-1.15,.2,1.0)]:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=.18,location=(x,y,z))
    bpy.context.object.data.materials.append(green)

# Hybrid-care screen and chair
cube('Hybrid_Screen',(4,-.2,.95),(.8,.06,.55),dark)
cyl('Hybrid_Chair',(4,-.95,.32),.34,.45,white)

# Save a reusable Blender file
bpy.ops.wm.save_as_mainfile(filepath=bpy.path.abspath('//fysioverse_clinic_assets.blend'))

# Select all generated assets for easy export as GLB from Blender.
bpy.ops.object.select_all(action='SELECT')
print('Fysioverse clinic asset pack created. Export selected objects as glTF/GLB for the web game.')