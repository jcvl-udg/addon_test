### TODO

# from openalea.lpy.lsysparameters import LsystemParameters

# lp = LsystemParameters()
# lp.add_scalar(name='w', value=0.01, minvalue=0.001, maxvalue=0.025, precision=3)
# lp.add_scalar(name='a', value=40, minvalue=0, maxvalue=70)


# %%lpy -a True -w 6 -p lp

# # default values if parameter names not found in LsystemParameters passed with '-p'
# extern (a = 40)    # angle
# extern (w = 0.01) # width

# f = lambda s : s/2.

# Axiom: ,(2)_(0.3)F(1, 0.25)A(1)

# production:
# derivation length: 6

# A(s) --> !(0.2*s)[^(a)F(s, 0.1*s)A(f(s))][/(90)^(a)F(s, 0.1*s)A(f(s))][/(180)^(a)F(s, 0.1*s)A(f(s))][/(270)^(a)F(s, 0.1*s)A(f(s))]/(137.5)F(s, 0.1*s)A(f(s))

# interpretation:

# A(s) --> @O(w)



