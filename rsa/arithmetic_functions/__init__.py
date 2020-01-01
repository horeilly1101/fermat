from rsa.arithmetic_functions.arithmetic_function import ArithmeticFunction
from rsa.arithmetic_functions.delta_function import DeltaFunction
from rsa.arithmetic_functions.euler_totient_function import EulerTotientFunction
from rsa.arithmetic_functions.identity_function import IdentityFunction
from rsa.arithmetic_functions.mobius_function import MobiusFunction
from rsa.arithmetic_functions.sigma_k_function import SigmaKFunction, SigmaFunction, DivisorFunction
from rsa.arithmetic_functions.unit_function import UnitFunction

# shorthand notation for several arithmetic functions
delta = DeltaFunction()
phi = EulerTotientFunction()
identity = IdentityFunction()
mu = MobiusFunction()
sigma = SigmaFunction()
d = DivisorFunction()
u = UnitFunction()
