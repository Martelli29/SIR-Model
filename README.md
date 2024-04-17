# SIR Model

[SIR models](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology) are mathematical tools that divide a population into three compartments:

- susceptible: compratment of healthy individuals that can contract the infection by the interaction with an infected individual and transit to the infected compartment.
- infected: individuals who have been infected and are capable of infecting susceptible individuals.
- recovered (healed or dead): individuals who have been infected and have either recovered from the disease or died. It is assumed that they can no longer contract the infection.

The transition between the compartments is descbribed through the parameters $\gamma$ and $\beta$.
$\gamma \in ]0,1]$ represent the healing probability and $\beta \in [0,\infty]$ represent the infection probability, these parameters govern the rates at which individuals transition between the compartments, influencing the dynamics of the epidemic.
The program allows users to explore various scenarios involving vaccine and isolation measures, observing how these interventions impact the epidemic parameters. The simulation culminates in a visual representation of the trends in susceptible, infected, and recovered individuals, along with a numerical summary of the epidemic parameters.

$$
\frac{dS}{dt} = -\beta \frac{S}{N} I
$$

$$
\frac{dI}{dt} = \beta \frac{S}{N} I - \gamma I
$$

$$
\frac{dR}{dt} = \gamma I
$$

## list of contents

1. [Install and run the code](https://github.com/Martelli29/SIR-Model#Install-and-run-the-code)
2. [Input parameters](https://github.com/Martelli29/SIR-Model#Input-parameters)
3. [Repository structure](https://github.com/Martelli29/SIR-Model#Repository-structure)
4. [More on the algorithm](https://github.com/Martelli29/SIR-Model#More-on-the-algorithm)

## Install and run the code

From _terminal_ move into the desired folder and clone this repository using the following command:

```shell
git clone https://github.com/Martelli29/SIR-Model.git
```

The requirements to run this application are:

- [python 3](https://www.python.org)
- [pytest](https://docs.pytest.org)
- [matplotlib](https://matplotlib.org)

Once the github repository is cloned use the following command to run the script:

```shell
python3 main.py
```

## Input parameters

Upon program execution, you'll be prompted to enter several parameters in the following order:

- $\gamma$ (gamma): This parameter represents the daily probability of recovery, ranging from 0 (no recovery) to 1 (guaranteed recovery). It's a floating number.
- $\beta$ (beta): This parameter represents the daily probability of infection, ranging from 0 (no infection) to 1 (guaranteed infection). It's also a floating-point number.
- Number of Susceptible individuals: This integer value represents the initial number of healthy individuals in the population.
- Number of Infected individuals: This integer value represents the initial number of infected individuals in the population.
- Number of Removed Individuals: This integer value represents the initial number of removed individuals (healed or deceased) in the population.
- Mitigation Measures (yes/no): Enter "yes" to activate mitigation measures or "no" to proceed without them.
    if you choose yes:
    1. Light Lockdown (20% $\beta$ reduction): Reduces the infection rate by 20%.
    2. Heavy Lockdown (70% $\beta$ reduction): Reduces the infection rate by 70%.
    3. Weakly Effective Vaccine (20% $\beta$ reduction, 50% $\gamma$ reduction): Reduces both infection and recovery rates by 20% and 50%, respectively.
    4. Strongly Effective Vaccine (60% $\beta$ reduction, 90% $\gamma$ reduction): Reduces both infection and recovery rates by 60% and 90%, respectively.

## Repository structure

The repository contains the following python files:

- epidemic_class.py:This file defines a class that encapsulates all the parameters and methods necessary to simulate the epidemic's evolution.
- input.py: This file handles the user interaction, prompting for initial parameters and passing them to the epidemic_class.py module.
- main.py: runs the evolution and and generating the graphical representation of the results.
- plot.py: This file contains the code responsible for creating the visual representation (plot) of the epidemic using the Matplotlib library.
- requirements.txt: This text file lists the external Python libraries required for the program to function. ([mentioned before](https://github.com/Martelli29/SIR-Model#Install-and-run-the-code))
- test.py: This file utilizes the pytest library to implement automated unit tests for the program's functionality.

## More on the algorithm

The SIR Model, as previously mentioned, utilizes three [differential equations](https://github.com/Martelli29/SIR-Model) to track the trends within three population groups: susceptible, infected, and recovered.
However, a key challenge arises when implementing this model in code. Differential equations operate with floating-point numbers, whereas real-world populations consist of discrete individuals (whole numbers).
To address this discrepancy, the algorithm employs a specific strategy after each iteration (representing a day) in the simulation. The differential equations provide updates for each population compartment (Susceptible, Infected, Recovered). Here, the algorithm separates the integer and decimal parts of these updates (e.g., 10.6 becomes 10 and 0.6). It then calculates the sum of the updated compartments (S, I, and R) and verifies if this sum matches the initial total population. If it does, the simulation proceeds to the next iteration. However, a discrepancy can exists, the algorithm further analyzes the decimal components. It identifies the compartment with the largest decimal value and increments the integer value of that compartment by 1. This cycle repeats until the total population remains consistent.

This core algorithm is implemented within the Evolve(...) method of the epidemic_class.py file.
