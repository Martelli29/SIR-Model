# SIR Model

[SIR models](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology) are mathematical tools that divide a population into three compartments:

- susceptible: compartment of healthy individuals that can contract the infection by the interaction with an infected individual and transit to the infected compartment.
- infected: individuals who have been infected and are capable of infecting susceptible individuals.
- recovered: individuals who have been infected and have either recovered from the disease or died. It is assumed that they can no longer contract the infection.

The transition between the compartments is descbribed through the parameters $\gamma$ and $\beta$.
$\gamma \in ]0,1]$ represent the healing probability and $\beta \in [0,1]$ represent the infection probability, these parameters govern the rates at which individuals transition between the compartments, influencing the dynamics of the epidemic.
The program allows users to explore various scenarios involving vaccine and isolation measures, observing how these interventions impact the epidemic parameters, this measures will be activated only if 10% of population is infected on a current day.
The simulation culminates in a visual representation of the trends in susceptible, infected, and recovered individuals, along with a numerical summary of the epidemic parameters.

$$
\frac{dS}{dt} = -\beta \frac{S}{N} I
$$

$$
\frac{dI}{dt} = \beta \frac{S}{N} I - \gamma I
$$

$$
\frac{dR}{dt} = \gamma I
$$

## List of contents

1. [Install and run the code](https://github.com/Martelli29/SIR-Model#Install-and-run-the-code)
2. [Repository structure](https://github.com/Martelli29/SIR-Model#Repository-structure)
3. [Parameters settings](https://github.com/Martelli29/SIR-Model#Input-parameters)
4. [More on the algorithm](https://github.com/Martelli29/SIR-Model#More-on-the-algorithm)
5. [Some examples](https://github.com/Martelli29/SIR-Model#Some-examples)

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

## Repository structure

The repository contains the following python files:

- config.json: Configuration file where users can set the parameter values for the simulation.
- config.py: This file retrieves data from config.json, validates the parameters, and prepares them for the simulation.
- epidemic_class.py: This file defines a class that encapsulates all the parameters and methods necessary to simulate the epidemic's evolution.
- main.py: runs the evolution and generating the graphical representation of the results.
- plot.py: This file contains the code responsible for creating the visual representation (plot) of the epidemic using the Matplotlib library.
- requirements.txt: This text file lists the external Python libraries required for the program to function. ([mentioned before](https://github.com/Martelli29/SIR-Model#Install-and-run-the-code))
- test.py: This file utilizes the pytest library to implement automated unit tests for the program's functionality.

## Parameters setting

The simulation use the parameters given by the config.json file, parameters are:

- $\gamma$ (gamma): This parameter represents the daily probability of recovery, ranging from 0 (no recovery) to 1 (guaranteed recovery). It's a floating number.
- $\beta$ (beta): This parameter represents the daily probability of infection, ranging from 0 (no infection) to 1 (guaranteed infection). It's also a floating-point number.
- Number of Susceptible individuals (S): This integer value represents the initial number of healthy individuals in the population.
- Number of Infected individuals (I): This integer value represents the initial number of infected individuals in the population.
- Number of Removed Individuals (R): This integer value represents the initial number of removed individuals (healed or deceased) in the population.
- Scenario: Selection of a possible lockdown/vaccine scenario.
    five different scenarios available:
    1. No measures.
    2. Light Lockdown (20% $\beta$ reduction): Reduces the infection rate by 20%.
    3. Heavy Lockdown (70% $\beta$ reduction): Reduces the infection rate by 70%.
    4. Weakly Effective Vaccine (20% $\beta$ reduction, 50% $\gamma$ reduction): Reduces both infection and recovery rates by 20% and 50%, respectively.
    5. Strongly Effective Vaccine (60% $\beta$ reduction, 90% $\gamma$ reduction): Reduces both infection and recovery rates by 60% and 90%, respectively.

Default parameter values are given: S=999999, I=0, R=0, $\gamma$=0.03, $\beta$=0.5, scenario= "strongly effective vaccine".

You are free to modify them as you want to obtain different scenarios.
In according to do this you can go into the config.json file and modify the number/characters after "value":

```json
    "gamma": {
        "description": "Healing probability (between 0 and 1)",
        "options": ["float number, must be between 0 and 1"],
        "value": 0.03
    },
```

In this case you can modify the value of $\gamma$ with a new one.

Pay attention to the "options" line to notice the constraints that you have to take into account.

In the scenario option choose one of the suggested sequence.
The sequence need the quotation marks "" and is no caps sensitive, avoid to insert additional space
or tab, an error will occurr (difference between different scenarios mentioned [before](https://github.com/Martelli29/SIR-Model#Repository-structure)).

```json
    "vaccine_scenario": {
        "description": "Mitigation scenario",
        "options": [
            "no measures",
            "light lockdown",
            "heavy lockdown",
            "weakly effective vaccine",
            "strongly effective vaccine"
        ],
        "value": "strongly effective vaccine"
    }
```

## More on the algorithm

The SIR Model, as previously mentioned, utilizes three [differential equations](https://github.com/Martelli29/SIR-Model) to track the trends within three population groups: susceptible, infected, and recovered.

However, a key challenge arises when implementing this model in code. Differential equations operate with floating-point numbers, whereas real-world populations consist of discrete individuals (whole numbers).
To address this discrepancy, the algorithm employs a specific strategy after each iteration (representing a day) in the simulation. The differential equations provide updates for each population compartment (Susceptible, Infected, Recovered). Here, the algorithm separates the integer and decimal parts of these updates (e.g., 10.6 becomes 10 and 0.6). It then calculates the sum of the updated compartments (S, I, and R) and verifies if this sum matches the initial total population. If it does, the simulation proceeds to the next iteration. However, a discrepancy can exists, the algorithm further analyzes the decimal components. It identifies the compartment with the largest decimal value and increments the integer value of that compartment by 1. This cycle repeats until the total population remains consistent.

This core algorithm is implemented within the Evolve(...) method of the epidemic_class.py file.

## Some examples

Let's how to show some results of the program:

In first example we will see the output with $\gamma$=0.05 and $\beta$=0.3:

```shell
-----------------------
Dimension of the population: 1000000
Selected scenario: no measures
Percentage of infected population: 99.82130000000001 %
Duration of the epidemic: 339
-----------------------
```

![In this case we have a complete epidemic diffusion without the usage of vaccine/isolation measures.](/Images/SimpleNoVaccineCase.png)

In this case we have a complete epidemic diffusion without the usage of vaccine/isolation measures.

Now, we will see the usage of a light isolation measures with the same parameters:

```shell
-----------------------
Dimension of the population: 1000000
Selected scenario: heavy lockdown
Vaccine/isolation day: 53
Percentage of infected population: 78.2412 %
Duration of the epidemic: 533
-----------------------
```

![In this case we have the activation of the heavy isolation measures, the vertical line represent the day in which the measures have been activated.](/Images/IsolationCase.png)

In this case we have the activation of the heavy isolation measures (scenario 2), the vertical line represent the day in which the measures have been activated.

Now we want to use the very effective vaccine option (scenario 4) and see how this disturb an aggressive epidemic with $\gamma$=0.03 and $\beta$=0.5:

```shell
-----------------------
Dimension of the population: 1000000
Selected scenario: no measures
Percentage of infected population: 100.0 %
Duration of the epidemic: 514
-----------------------
```

![No vaccine scenario.](/Images/HeavyScenarioNoVaccine.png)

No vaccine scenario.

```shell
-----------------------
Dimension of the population: 1000000
Selected scenario: strongly effective vaccine
Vaccine/isolation day: 31
Percentage of infected population: 97.3699 %
Duration of the epidemic: 323
-----------------------
```

![Scenario with vaccine usage.](/Images/HeavyScenarioWithVaccine.png)

Scenario with vaccine usage.

How we can see, both scenarios involve the entire population throughout the epidemic. However, the presence of a vaccine introduces a key difference. Vaccination leads to a broader peak in the number of infected individuals. This wider peak distributes the infected cases over a longer time period.
In contrast, the absence of vaccination results in a much narrower peak. In real-world situations, such a narrow peak can overwhelm healthcare systems, posing significant challenges for managing the epidemic.
