"""Finite-dimensional Weil operator tools."""

from .completed import CompletedDirichletData, conductor_matrix
from .explicit_formula import (
    PrimeOperatorTerm,
    assemble_prime_operator,
    exponential_prime_weight,
    gaussian_log_prime_weight,
    prime_operator_terms,
    quadratic_prime_power_coefficient,
    sharp_prime_weight,
    universal_prime_operator,
    von_mangoldt,
)
from .gamma import gamma_kernel, gamma_matrix, gamma_weight
from .gram import gram_matrix, scalar_form_matrix
from .lfunctions import (
    PrimitiveQuadraticCharacter,
    is_fundamental_discriminant,
    jacobi_symbol,
    kronecker_symbol,
    prime_power_base,
)
from .operators import (
    generalized_eigenvalues,
    gram_operator_norm,
    gram_whitened_matrix,
)
from .packets import GaussianPacketFamily
from .weil_operator import WeilOperator

__all__ = [
    "CompletedDirichletData",
    "GaussianPacketFamily",
    "PrimeOperatorTerm",
    "PrimitiveQuadraticCharacter",
    "WeilOperator",
    "assemble_prime_operator",
    "conductor_matrix",
    "exponential_prime_weight",
    "gamma_kernel",
    "gamma_matrix",
    "gamma_weight",
    "gaussian_log_prime_weight",
    "generalized_eigenvalues",
    "gram_matrix",
    "gram_operator_norm",
    "gram_whitened_matrix",
    "is_fundamental_discriminant",
    "jacobi_symbol",
    "kronecker_symbol",
    "prime_operator_terms",
    "prime_power_base",
    "quadratic_prime_power_coefficient",
    "scalar_form_matrix",
    "sharp_prime_weight",
    "universal_prime_operator",
    "von_mangoldt",
]
