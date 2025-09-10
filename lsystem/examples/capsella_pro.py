"""
Capsella Bursa-Pastoris L-system simulation.
Best practices: parameterization, stateful Exec, ready for custom interpretation/tropism.
"""

import lsystem.exec

def make_capsella(exec_obj, humidity=50, sun_hours=8, temperature=20, soil_nutrients=50, co2_concentration=400, seasonal_variation=0):
    """
    Configure Capsella plant rules using Exec best practices.
    """
    # Define constants for parameterization
    exec_obj.define("branch_angle", 70 + (humidity / 100) * 10 + (seasonal_variation * 15))
    exec_obj.define("leaf_angle", 18 + sun_hours * 2)
    exec_obj.define("flower_size", 10 + (temperature - 20) * 0.3 + (co2_concentration / 400) * 1.5)
    exec_obj.define("stem_length", 9 + (soil_nutrients / 100) * 2 + (temperature - 20) * 0.2)

    # Set axiom with placeholders
    exec_obj.set_axiom("p(subsurf)I(#stem_length#)aa(13)")
    exec_obj.rules = []

    # Growth rules using placeholders
    exec_obj.add_rule("aa(t)", "[&(#branch_angle#)L]/(137.5)I(10)aa(sub(t,1))", "gt(t,0)")
    exec_obj.add_rule("aa(t)", "[&(#branch_angle#)L]/(137.5)I(10)A", "eq(t,0)")
    exec_obj.add_rule("A", "[&(#leaf_angle#)uu(4)FFI(10)I(5)X(5)K{'K'*int(#flower_size#)}]/(137.5)I(8)A")
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

    # Example: set tropism (gravity)
    exec_obj.set_tropism((0, 0, -1), 0.2)

    # Example: set custom interpretation (optional, for advanced geometry)
    # def custom_F(symbol, params):
    #     # Custom mesh logic here
    #     pass
    # exec_obj.set_interpretation("F", custom_F)

def simulate_capsella(exec_obj, humidity=50, sun_hours=8, temperature=20, soil_nutrients=50, co2_concentration=400, seasonal_variation=0, min_iterations=1, max_iterations=16):
    # Configure the L-system with parameters
    make_capsella(exec_obj, humidity, sun_hours, temperature, soil_nutrients, co2_concentration, seasonal_variation)
    # Run the simulation
    exec_obj.exec(min_iterations=min_iterations, max_iterations=max_iterations)