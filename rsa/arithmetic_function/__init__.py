from rsa.arithmetic_function.arithmetic_function import ArithmeticFunction
from rsa.arithmetic_function.delta_function import DeltaFunction
from rsa.arithmetic_function.euler_totient_function import EulerTotientFunction
from rsa.arithmetic_function.identity_function import IdentityFunction
from rsa.arithmetic_function.mobius_function import MobiusFunction
from rsa.arithmetic_function.sigma_k_function import SigmaKFunction, SigmaFunction, DivisorFunction
from rsa.arithmetic_function.unit_function import UnitFunction

# shorthand notation for several arithmetic functions
delta = DeltaFunction()
phi = EulerTotientFunction()
identity = IdentityFunction()
mu = MobiusFunction()
sigma = SigmaFunction()
d = DivisorFunction()
u = UnitFunction()
