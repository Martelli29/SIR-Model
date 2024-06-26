from typing import Tuple


class EpidemicSIR:
    """
    EpidemicSIR contains all the information about the epidemic and the methods to evolve the system.
    It takes as input all the parameters passed by the users through the configuration file.
    """

    def __init__(self, config: dict):
        """
        Constructor of the EpidemicSIR class, here there is the configuration of main parameters of the
        simulation passed by the user through the configuration file, the creation of three vectors and two variables.
        Vectors store the values of S/I/R compartments for each day of the simulation, variable vaccine_day
        keep the count of the duration of the simulation and variable day
        represent the day in which countermeasures were taken.

        1 parameter needed:
            config (dictionary): contains the paramaters used for the epidemic: 
                "S" (int): number of the initial susceptible population.
                "I" (int): number of the initial infected population.
                "R" (int): number of the initial removed population.
                "gamma" (float): healing probability after each day of the simulation.
                "beta" (float): infection probability after each day of the simulation.
                "scenario" (str): selected scenario for the simulation.
        """

        self.S = int(config["S"])
        self.I = int(config["I"])
        self.R = int(config["R"])
        self.N = int(config["S"] + config["I"] +
                     config["R"])  # total population
        self.gamma = config["gamma"]       # healing probability
        self.beta = config["beta"]        # infection probability
        self.scenario = config["scenario"]

        self.S_vector = [self.S]  # day 0
        self.I_vector = [self.I]  # day 0
        self.R_vector = [self.R]  # day 0
        self.vaccine_day = None
        self.day = 1

    def Vaccine(self, vax_request: bool | None, gamma: float, beta: float) -> Tuple[bool | None, float, float]:
        """
        Method select the proper scenario that is given by the user in the constructor of the class,
        we want that the modification of the gamma and/or beta parameters is executed only once during the simulation.
        The modification of the parameters gamma and beta will be allowed only if the number of infetced people
        on a givne day are at least eqaul to 10% of the total population.

        Five different scenario are available: 
        -no measures: gamma and beta unchanged.
        -light lockdown: 20% reduction of beta.
        -heavy lockdown: 70% reduction of beta.
        -weakly effective vaccine: 20% reduction of beta and 50 % increase of gamma.
        -strongly effective vaccine: 60% reduction of beta and 90 % increase of gamma.

        3 parameters needed:
            vax_request (None|bool): boolean variable that allow to change the gamma/beta parameters only once.
            gamma (float): healing probability after each day of the simulation.
            beta (float): infection probability after each day of the simulation.

        return:
            vax_request (bool): boolean variable that is setted to true if some countermeasures is been taken and viceversa.
            gamma (float): new healing probability after the application (or not) of the countermeasures.
            beta (float): new infection probability after the application (or not) of the countermeasures.
        """

        if vax_request == None:

            if self.scenario == "no measures":

                vax_request = False

            elif self.I_vector[-1] > 0.1 * self.N and self.scenario == "light lockdown":

                vax_request = True
                self.vaccine_day = self.day - 1

                beta = beta - (0.2 * beta)

            elif self.I_vector[-1] > 0.1 * self.N and self.scenario == "heavy lockdown":

                vax_request = True
                self.vaccine_day = self.day - 1

                beta = beta - (0.7 * beta)

            elif self.I_vector[-1] > 0.1 * self.N and self.scenario == "weakly effective vaccine":

                vax_request = True
                self.vaccine_day = self.day - 1

                beta = beta - (0.2 * beta)
                gamma = gamma + (0.5 * gamma)

            elif self.I_vector[-1] > 0.1 * self.N and self.scenario == "strongly effective vaccine":

                vax_request = True
                self.vaccine_day = self.day - 1

                beta = beta - (0.6 * beta)
                gamma = gamma + (0.9 * gamma)

        return vax_request, gamma, beta

    def DifferentialEq(self, S: float, I: float, R: float, gamma: float, beta: float) -> Tuple[float, float, float]:
        """
        Application of the differential eqautions of the SIR model for the calculation of the 
        susceptible, infected and removed for the next day of the epidemic.

        5 parameters needed:
            S (float): number of susceptible population.
            I (float): number of infected population.
            R (float): number of removed population.
            gamma (float): healing probability after each day of the simulation.
            beta (float): infection probability after each day of the simulation.

        return:
            S (float): number of susceptible population after the application of the differential eqautions.
            I (float): number of infected population after the application of the differential eqautions.
            R (float): number of removed population after the application of the differential eqautions.
        """

        deltaS = ((-beta) * S * I) / self.N
        deltaI = ((beta * S * I / self.N) - gamma * I)
        deltaR = gamma * I

        S += deltaS
        I += deltaI
        R += deltaR

        return S, I, R

    def Approximation(self, S: float, I: float, R: float) -> Tuple[int, int, int]:
        """
        Takes the three float numbers of S/I/R and approximates them in three integer numbers.
        The float numbers are divided into whole part and deciaml part, then he checks if the sum
        of the whole numbers are equal to the total population, if they are equal, the algorithm
        ends, if not the algorithm increments the compartment which has the biggest 
        decimal part until the sum of S-I-R are equal to the total population.

        3 parameters needed:
            S (float): number of susecptible population. 
            I (float): number of infected population.
            R (float): number of removed population.

        return:
            int_S (int): number of susecptible population after conversion in whole number and approximation.
            int_I (int): number of infected population after conversion in whole number and approximation.
            int_R (int): number of removed population after conversion in whole number and approximation.
        """
        # the integer part of the internal variables are assigned to the parameters S,I,R
        int_S = int(S)
        int_I = int(I)
        int_R = int(R)

        # calculation of the decimal part of the internal variables
        decimal_s = S - int_S
        decimal_i = I - int_I
        decimal_r = R - int_R

        current_n = int(int_S + int_I + int_R)  # current values of N

        while current_n < self.N:
            # following loop works the approximation in case current_n is minor than N
            # current_n and S or I or R which have the biggest decimal part is incremented by one

            if (decimal_s > decimal_i) and (decimal_s > decimal_r) and (self.S_vector[-1] > int_S):
                int_S += 1
                decimal_s = 0

            elif (decimal_i > decimal_s) and (decimal_i > decimal_r):
                int_I += 1
                decimal_i = 0

            else:
                int_R += 1
                decimal_r = 0

            current_n += 1

        return int_S, int_I, int_R

    def Evolve(self) -> None:
        """
        This method is the core engine of the epidemic evolution.
        Calls the methods that works the differential equations of the SIR model, the approximation
        and an eventual vaccine scenario until the number of infected population is equal to 0.
        During each iteration (day) of the simulation, the values of the three compartments are
        stored in vectors that will be used in the plot of the graph.

        0 parameters needed:
            None

        return:
            None
        """

        # internal variable for the calculation
        diffeq_S = self.S
        diffeq_I = self.I
        diffeq_R = self.R
        gamma = self.gamma
        beta = self.beta
        vax_request = None

        while self.I_vector[-1] != 0:

            vax_request, gamma, beta = self.Vaccine(vax_request, gamma, beta)

            diffeq_S, diffeq_I, diffeq_R = self.DifferentialEq(
                diffeq_S, diffeq_I, diffeq_R, gamma, beta)

            int_S, int_I, int_R = self.Approximation(
                diffeq_S, diffeq_I, diffeq_R)

            self.day += 1
            self.S_vector.append(int_S)
            self.I_vector.append(int_I)
            self.R_vector.append(int_R)

    def PrintResults(self) -> None:
        """
        Print function, logs the main parameters of the simulation to the terminal.
        """

        print("-----------------------")
        print("Dimension of the population:", self.N)
        print("Selected scenario:", self.scenario)
        if self.vaccine_day != None:
            print("Vaccine/isolation day:", self.vaccine_day)
        elif self.scenario != "no measures" and self.vaccine_day == None:
            print("No Vaccine/isolation measures needed.")
        print("Percentage of infected population:",
              (self.R_vector[-1]/self.N)*100, "%")
        print("Duration of the epidemic:",  self.day)
        print("-----------------------")
