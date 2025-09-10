"""
Capsella Bursa-Pastoris L-system simulation.
See figure 3.5 in 'Algorithmic Beauty of Plants' (http://algorithmicbotany.org/papers/abop/abop.pdf), page 74.
"""

import lsystem.exec

def make_capsella(exec_obj, humidity=50, sun_hours=8, temperature=20, soil_nutrients=50, co2_concentration=400, seasonal_variation=0):
    """
    Configure Capsella plant rules based on climate variables.
    """
    # Ajustar parámetros según variables climáticas
    branch_angle = 70 + (humidity / 100) * 10 + (seasonal_variation * 15)
    leaf_angle = 18 + sun_hours * 2
    flower_size = 10 + (temperature - 20) * 0.3 + (co2_concentration / 400) * 1.5
    stem_length = 9 + (soil_nutrients / 100) * 2 + (temperature - 20) * 0.2

    # Establecer axioma inicial
    exec_obj.set_axiom(f"p(subsurf)I({int(stem_length)})aa(13)")
    exec_obj.rules = []

    # Reglas de crecimiento
    exec_obj.add_rule("aa(t)", f"[&({branch_angle})L]/(137.5)I(10)aa(sub(t,1))", "gt(t,0)")
    exec_obj.add_rule("aa(t)", f"[&({branch_angle})L]/(137.5)I(10)A", "eq(t,0)")
    exec_obj.add_rule("A", f"[&({leaf_angle})uu(4)FFI(10)I(5)X(5)K{'K'*int(flower_size)}]/(137.5)I(8)A")
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

def simulate_capsella(exec_obj, humidity=50, sun_hours=8, temperature=20, soil_nutrients=50, co2_concentration=400, seasonal_variation=0, min_iterations=1, max_iterations=16):
    # Configurar las reglas según los parámetros ambientales
    make_capsella(exec_obj, humidity, sun_hours, temperature, soil_nutrients, co2_concentration, seasonal_variation)
    
    # Ejecutar el sistema L
    exec_obj.exec(min_iterations=min_iterations, max_iterations=max_iterations)