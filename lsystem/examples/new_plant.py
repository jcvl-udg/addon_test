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
    # Define parameters based on environmental factors
    exec_obj.define("stem_length", str(8 + (soil_nutrients / 100) * 3))
    exec_obj.define("branch_angle", str(40 + (humidity / 100) * 15))
    exec_obj.define("leaf_size", str(5 + (sun_hours / 12) * 3))
    exec_obj.define("flower_size", str(4 + (temperature - 20) * 0.2 + (co2_concentration / 400) * 1.2))
    exec_obj.define("internode_length", str(6 + (soil_nutrients / 100) * 2))
    
    # Set axiom
    exec_obj.set_axiom("A")
    
    # Clear any existing rules
    exec_obj.rules = []
    
    # Growth rules
    exec_obj.add_rule("A", "I(stem_length)[+B][-B]A")
    exec_obj.add_rule("B", "I(internode_length)[+L][-L]B", "probability(0.7)")
    exec_obj.add_rule("B", "I(internode_length)F")
    exec_obj.add_rule("F", "K(flower_size)")
    
    # Leaf rules - cordate (heart-shaped) leaves
    exec_obj.add_rule("L", "[:p(surface)FI(leaf_size)&(30)FI(leaf_size*0.6)~(180)FI(leaf_size*0.6)&(30)FI(leaf_size);]")
    
    # Flower rules - simple inflorescence
    exec_obj.add_rule("K(s)", "[&(45):p(surface)~(72){F(s*0.3)};]^(135)[&(45):p(surface)~(72){F(s*0.3)};]", "gt(s,0)")

def simulate_flowering_plant(exec_obj, humidity=50, sun_hours=8, temperature=20, 
                           soil_nutrients=50, co2_concentration=400, seasonal_variation=0, 
                           min_iterations=3, max_iterations=8):
    # Configure the L-system with parameters
    make_flowering_plant(exec_obj, humidity, sun_hours, temperature, 
                        soil_nutrients, co2_concentration, seasonal_variation)
    # Run the simulation
    exec_obj.exec(min_iterations=min_iterations, max_iterations=max_iterations)

# Example usage with custom interpretation
def setup_custom_interpretation(exec_obj):
    """Set up custom interpretation for leaves and flowers"""
    
    # def interpret_leaf(symbol, params):
    #     # Placeholder for custom leaf geometry
    #     # In practice, you would create mesh data here
    #     print(f"Creating leaf with params: {params}")
    #     # This would typically create a heart-shaped mesh
        
    def interpret_flower(turtle, parameters, bl_obj, obj_base_pairs, context):
        mesh = bpy.data.meshes.new("sphere")
        obj = bpy.data.objects.new("sphere", mesh)
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=bl_obj.radius*5)
        bm.to_mesh(mesh)
        bm.free()
        obj.location = lsystem.util.matmul(turtle.transform, mathutils.Vector((0.0, 0.0, 0.0)))
        obj.rotation_euler = turtle.transform.to_euler()
        base = lsystem.util.link(context, obj)
        obj.parent = bl_obj.object
        obj_base_pairs.append((obj, base))
        # Placeholder for custom flower geometry
        # print(f"Creating flower with params: {params}")
        # This would typically create a flower mesh with petals
        
    # Set custom interpretations
    # exec_obj.set_interpretation("L", interpret_leaf)
    exec_obj.set_interpretation("K", interpret_flower)

# Create and run the simulation
# exec_obj = lsystem.exec.Exec()
# simulate_flowering_plant(exec_obj)
# setup_custom_interpretation(exec_obj)

# Tirando Issues en la primer prueba
#Error al generar la planta: must be real number, not method
