from mathutils import Vector
import lsystem.exec

import bpy
import lsystem.util
import mathutils
import bmesh

import random

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
        # Unique prefix for this leaf instance
        leaf_prefix = f"leaf_{random.randint(0, 100000)}_"

        # Run the leaf L-system (returns a list of objects)
        leaf_exec = lsystem.exec.Exec()
        # Smaller leaf parameters
        leaf_exec.define("LA", "2")
        leaf_exec.define("RA", "1.15")
        leaf_exec.define("LB", "0.7")
        leaf_exec.define("RB", "1.25")
        leaf_exec.define("LC", "1.5")
        leaf_exec.define("RC", "1.19")
        leaf_exec.set_axiom("p(surface)s(0.01)[{A(0,0)F(0)}][{A(0,1)F(0)}]")
        leaf_exec.add_rule("A(t,d)", "F(0)f(LA,RA)F(0)[+B(t)f(LC,RC,t)F(0)}][+B(t){F(0)]A(add(t,1),d)", condition="eq(d,0)")
        leaf_exec.add_rule("A(t,d)", "F(0)f(LA,RA)F(0)[-B(t)f(LC,RC,t)F(0)}][-B(t){F(0)]A(add(t,1),d)", condition="eq(d,1)")
        leaf_exec.add_rule("B(t)", "f(LB,RB)B(sub(t,1))", condition="gt(t,0)")
        leaf_exec.add_rule("f(s,r)", "f(mul(s,r),r)")
        leaf_exec.add_rule("f(s,r,t)", "f(mul(s,r),r,sub(t,1))", condition="gt(t,1)")

        # Run the L-system, get the objects
        leaf_exec.exec(min_iterations=27, angle=60, context=context)
        leaf_objs = leaf_exec.objects

        # Rename all leaf objects with the prefix
        for obj in leaf_objs:
            obj.name = leaf_prefix + obj.name

        # Deselect all, select only the leaf objects
        bpy.ops.object.select_all(action='DESELECT')
        for obj in leaf_objs:
            obj.select_set(True)
        context.view_layer.objects.active = leaf_objs[0]

        # Join all selected objects into one
        bpy.ops.object.join()
        joined_leaf = context.view_layer.objects.active

        # Set transform and parent
        joined_leaf.location = lsystem.util.matmul(turtle.transform, mathutils.Vector((0.0, 0.0, 0.0)))
        joined_leaf.rotation_euler = turtle.transform.to_euler()
        joined_leaf.parent = bl_obj.object

        # Only link if not already in the scene
        if joined_leaf.name not in context.scene.collection.objects:
            base = lsystem.util.link(context, joined_leaf)
        else:
            base = joined_leaf

        obj_base_pairs.append((joined_leaf, base))

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
    # exec_obj.add_rule("L", "[:p(surface)F(0)-FI(7)+FI(7)+FI(7);][:p(surface)F(0)+FI(7)-FI(7)-FI(7);]")
    # exec_obj.add_rule("K", "[&:p(surface)F(0)+FI(2)--FI(2);][&:p(surface)F(0)-FI(2)++FI(2);]/(90)")
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
