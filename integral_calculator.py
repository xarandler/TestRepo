import streamlit as st
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

def calculate_and_plot_integral(function, lower_limit, upper_limit):
    x = sp.symbols('x')
    f = sp.lambdify(x, function, 'numpy')
    integral_value = sp.integrate(function, (x, lower_limit, upper_limit))

    fig, ax = plt.subplots()
    x_vals = np.linspace(lower_limit, upper_limit, 100)
    y_vals = f(x_vals)
    ax.plot(x_vals, y_vals, label=f'f(x) = {function}')
    ax.fill_between(x_vals, y_vals, alpha=0.3)
    ax.legend()

    return integral_value, fig

def show_integral_calculator():
    st.title("Integral Calculator")

    function_input = st.text_input("Enter the integrand function (in terms of x)", "x**2")
    lower_limit = st.number_input("Enter the lower limit", value=0.0)
    upper_limit = st.number_input("Enter the upper limit", value=1.0)

    if st.button("Solve"):
        try:
            integral_value, plot = calculate_and_plot_integral(function_input, lower_limit, upper_limit)
            st.write(f"The integral value is: {integral_value}")
            st.pyplot(plot)
        except Exception as e:
            st.error(f"An error occurred: {e}")
