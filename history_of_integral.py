import streamlit as st

def show_history_of_integral():
    st.title("History of Integral Calculus")
    st.image("img/history.png")

    st.write("""
        Integral calculus is a fundamental component of mathematics, deeply rooted in understanding areas, volumes, and the concept of infinity. Its development spans centuries and continents, with significant contributions from various mathematicians.

        ## Early Beginnings
        The origins of integral calculus can be traced back to ancient mathematicians who used rudimentary methods to find areas and volumes. These methods laid the groundwork for the formal development of calculus.

        ## The 17th Century Breakthrough
        The 17th century marked a turning point with two mathematicians, Isaac Newton and Gottfried Wilhelm Leibniz, who independently developed the foundations of calculus.


        - **Gottfried Wilhelm Leibniz (1646–1716)**: Leibniz's work on calculus was more about analysis than geometry. He introduced the integral symbol ∫, which is an elongated 'S' representing 'summa' (Latin for 'sum').
    """)
    st.image("img/leibniz.jpg", caption="Gottfried Wilhelm Leibniz")
    st.write("""
        - **Isaac Newton (1643–1727)**: Newton approached calculus from a more geometric perspective, focusing on rates of change and slopes of curves.
    """)
    st.image("img/newton.jpg", caption="Isaac Newton")
    st.write("""

        ## 18th and 19th Centuries: Expansion and Formalization
        After Newton and Leibniz, many mathematicians contributed to the refinement and expansion of calculus.

        - **Leonhard Euler (1707–1783)**: Euler made significant contributions to the formalization of calculus and introduced many of its modern terminologies.
    """)
    st.image("img/euler.jpg", caption="Leonhard Euler")
    st.write("""
        - **Carl Friedrich Gauss (1777–1855)**: Known as the 'Prince of Mathematicians', Gauss's work in the field of analysis, especially differential geometry, further advanced the understanding of integrals.


        ## Modern Developments
        In the 19th and 20th centuries, calculus continued to evolve. The rigorous foundations were established, and calculus began to be applied in other fields like physics, engineering, and economics.

        Integral calculus remains a vibrant area of mathematical research and application, continually expanding our understanding of the natural world.

    """)


# Call the function to display the page
show_history_of_integral()
