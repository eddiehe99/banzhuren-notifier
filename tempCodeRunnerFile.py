import numpy as np
from scipy.optimize import fsolve


def distortion_model_equations(
    parameters,
    f_x,
    f_y,
    c_x,
    c_y,
    k1,
    k2,
    k3,
    p1,
    p2,
    u,
    v,
):
    theta, phi = parameters
    tan_theta = np.tan(theta)
    tan2_theta = tan_theta**2
    tan4_theta = tan_theta**4
    tan6_theta = tan_theta**6

    cos_phi = np.cos(phi)
    sin_phi = np.sin(phi)
    cos2_phi = cos_phi**2
    sin2_phi = sin_phi**2

    x_distorted = (
        f_x
        * (
            tan_theta
            * cos_phi
            * (1.0 + k1 * tan2_theta + k2 * tan4_theta + k3 * tan6_theta)
            + 2 * p1 * tan2_theta * sin_phi * cos_phi
            + p2 * tan2_theta * (1 + 2 * cos2_phi)
        )
        + c_x
    )

    y_distorted = (
        f_y
        * (
            tan_theta
            * sin_phi
            * (1.0 + k1 * tan2_theta + k2 * tan4_theta + k3 * tan6_theta)
            + 2 * p2 * tan2_theta * sin_phi * cos_phi
            + p1 * tan2_theta * (1 + 2 * sin2_phi)
        )
        + c_y
    )

    return [x_distorted - u, y_distorted - v]


# example parameters
f_x = 1000.0
f_y = 1000.0
c_x = 500.0
c_y = 500.0
k1 = 0.01
k2 = 0.001
k3 = 0.0001
p1 = 0.001
p2 = 0.001
u = 550.0  # known u
v = 550.0  # known v
theta = np.radians(30)  # 30 degrees
phi = np.radians(45)  # 45 degrees
initial_guess = [theta, phi]

solution = fsolve(
    distortion_model_equations,
    initial_guess,
    args=(f_x, f_y, c_x, c_y, k1, k2, k3, p1, p2, u, v),
)

theta_solution, phi_solution = solution

print(
    f"Solved angles: theta = {np.degrees(theta_solution)} degrees, phi = {np.degrees(phi_solution)} degrees"
)
