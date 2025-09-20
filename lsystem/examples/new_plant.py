from mathutils import Vector
import lsystem.exec

import bpy
import lsystem.util
import mathutils
import bmesh

def make_flowering_plant(exec_obj, humidity=50, sun_hours=8, temperature=20, 
                        soil_nutrients=50, co2_concentration=400, seasonal_variation=0):
    """
    Configure a flowering plant with cordate leaves and inflorescence.
    """
    def sphere(turtle, parameters, bl_obj, obj_base_pairs, context):
        mesh = bpy.data.meshes.new("sphere")
        obj = bpy.data.objects.new("sphere", mesh)
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, radius=0.66)
        bm.to_mesh(mesh)
        bm.free()
        obj.location = lsystem.util.matmul(turtle.transform, mathutils.Vector((0.0, 0.0, 0.0)))
        obj.rotation_euler = turtle.transform.to_euler()
        base = lsystem.util.link(context, obj)
        obj.parent = bl_obj.object
        obj_base_pairs.append((obj, base))
        
    def make_leaf_geometry(turtle, parameters, bl_obj, obj_base_pairs, context):
        # Create a new mesh and object for the leaf
        # Simple leaf (Figure 5.6 b in Algorithmic Beauty of Plants on page 124)
        mesh = bpy.data.meshes.new("leaf_mesh")
        leaf_obj = bpy.data.objects.new("leaf", mesh)
        bm = bmesh.new()

        # Create a new Exec object for the leaf L-system
        leaf_exec = lsystem.exec.Exec()
        leaf_exec.define("LA", "5")
        leaf_exec.define("RA", "1")
        leaf_exec.define("LB", "0.6")
        leaf_exec.define("RB", "1.06")
        leaf_exec.define("PD", "0.25")
        leaf_exec.set_axiom("p(surface)F(0)A(0)")
        leaf_exec.add_rule("A(t)", "f(LA,RA)[-B(t)F(0)][A(add(t,1))][+B(t)F(0)]")
        leaf_exec.add_rule("B(t)", "f(LB,RB)B(sub(t,PD))", condition="gt(t,0)")
        leaf_exec.add_rule("f(s,r)", "f(mul(s,r),r)")

        # Run the leaf L-system, generating geometry into bm (bmesh)
        # You may need to adapt this part depending on how your L-system outputs geometry
        # For example, if your L-system can output to a bmesh:
        leaf_exec.exec(min_iterations=20, angle=60, bmesh_out=bm)

        # Write the bmesh to the mesh
        bm.to_mesh(mesh)
        bm.free()

        # Set the leaf object's transform and parent
        leaf_obj.location = lsystem.util.matmul(turtle.transform, mathutils.Vector((0.0, 0.0, 0.0)))
        leaf_obj.rotation_euler = turtle.transform.to_euler()
        leaf_obj.parent = bl_obj.object

        # Link the object to the scene
        base = lsystem.util.link(context, leaf_obj)
        obj_base_pairs.append((leaf_obj, base))

    # Define constants for parameterization
    exec_obj.define("branch_angle", str( 70 + (humidity / 100) * 10 + (seasonal_variation * 15) ) )
    exec_obj.define("leaf_angle", str( 18 + sun_hours * 2 ) )
    exec_obj.define("flower_size", str( 10 + (temperature - 20) * 0.3 + (co2_concentration / 400) * 1.5 ) )
    exec_obj.define("stem_length", str( 9 + (soil_nutrients / 100) * 2 + (temperature - 20) * 0.2 ) )

    # Set axiom with placeholders
    exec_obj.set_axiom("p(subsurf)I(stem_length)aa(13)")
    exec_obj.rules = []

    # Growth rules using placeholders
    exec_obj.add_rule("aa(t)", "[&(branch_angle)L]/(137.5)I(10)aa(sub(t,1))", "gt(t,0)")
    exec_obj.add_rule("aa(t)", "[&(branch_angle)L]/(137.5)I(10)A", "eq(t,0)")
    exec_obj.add_rule("A", "[&(leaf_angle)uu(4)FFI(10)I(5)X(5)K{mul('K',flower_size)}]/(137.5)I(8)A")
    exec_obj.add_rule("I(t)", "FI(sub(t,1))", "gt(t,0)")
    exec_obj.add_rule("I(t)", "F", "eq(t,0)")
    exec_obj.add_rule("ii(t)", "fii(sub(t,1))", "gt(t,0)")
    exec_obj.add_rule("ii(t)", "f", "eq(t,0)")
    exec_obj.add_rule("uu(t)", "&(9)uu(sub(t,1))", "gt(t,0)")
    exec_obj.add_rule("uu(t)", "&(9)", "eq(t,0)")
    exec_obj.add_rule("L", "[:p(surface)F(0)-FI(7)+FI(7)+FI(7);][:p(surface)F(0)+FI(7)-FI(7)-FI(7);]")
    exec_obj.add_rule("K", "[&:p(surface)F(0)+FI(2)--FI(2);][&:p(surface)F(0)-FI(2)++FI(2);]/(90)")
    exec_obj.add_rule("X(t)", "X(sub(t,1))", "gt(t,0)")
    exec_obj.add_rule("X(t)", "^(50):p(surface)[[-ffff++[fff[++f{F(0)]F(0)]F(0)]F(0)++ffffF(0)--fffF(0)--fF(0)}];%", "eq(t,0)")

    exec_obj.set_interpretation("K", sphere)
    exec_obj.set_interpretation("L", make_leaf_geometry)

def simulate_flowering_plant(exec_obj, humidity=50, sun_hours=8, temperature=20, 
                           soil_nutrients=50, co2_concentration=400, seasonal_variation=0, 
                           min_iterations=6, max_iterations=18):
    # Configure the L-system with parameters
    make_flowering_plant(exec_obj, humidity, sun_hours, temperature, 
                        soil_nutrients, co2_concentration, seasonal_variation)
    # Run the simulation
    exec_obj.exec(min_iterations=min_iterations, max_iterations=max_iterations)


# Capsella bursa pastoris con Spheres reemplazando la flor
#TO-DO:
# CREAR NUEVA GEOMETRIA PARA LAS FLORES
