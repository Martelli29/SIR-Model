
class EpidemicSIR:
    '''
    EpidemicSIR contains all the information on the epidemic and the functions to system evolve.
    It takes as input all the parameters setted by the users in the input.py file.
    '''
    
    def __init__(self, S, I, R, gamma, beta, scenario):
        '''
        In the constructor we have the assignment of the parameters passed as argument and the
        creation of three empty lists useful for the plot.
        '''

        self.S = int(S)
        self.I = int(I)
        self.R = int(R)
        self.N = int(S + I + R) # total population
        self.gamma = gamma      # healing probability
        self.beta = beta        # infection probability
        self.day = 1
        self.scenario = scenario

        self.S_vector = [self.S] #day 0
        self.I_vector = [self.I] #day 0
        self.R_vector = [self.R] #day 0
        self.triggerday = None


    def Vaccine(self, vax_request, gamma, beta):
        '''
        This method set the new possible values of beta and gamma once a scenario has been selected. 
        '''

        if vax_request == None:
        
            if self.scenario == "no measures":
                
                vax_request = False
            
            elif self.I_vector[-1] > 0.1 * self.N and self.scenario == "light lockdown":
                
                vax_request = True
                self.triggerday = self.day - 1
                
                beta = beta - (0.2 * beta)

            elif self.I_vector[-1] > 0.1 * self.N and self.scenario == "heavy lockdown":
                
                vax_request = True
                self.triggerday = self.day - 1

                beta = beta - (0.7 * beta)
            
            elif self.I_vector[-1] > 0.1 * self.N and self.scenario == "weakly effective vaccine":
                
                vax_request = True
                self.triggerday = self.day - 1

                beta = beta - (0.2 * beta)
                gamma = gamma + (0.5 * gamma)

            elif self.I_vector[-1] > 0.1 * self.N and self.scenario == "strongly effective vaccine":

                vax_request = True
                self.triggerday = self.day - 1

                beta = beta - (0.6 * beta)
                gamma = gamma + (0.9 * gamma)

        return vax_request, gamma, beta


    def DifferentialEq(self, S, I, R, gamma, beta):
        # Evolution of the epidemic by the differential equation
        deltaS = ((-beta) * S * I) / self.N
        deltaI = ((beta * S * I / self.N) - gamma * I)
        deltaR = gamma * I

        S += deltaS
        I += deltaI
        R += deltaR

        return S, I, R


    def Approximation(self, float_S, float_I, float_R):
        # the integer part of the internal variables are assigned to the parameters S,I,R
        int_S = int(float_S)
        int_I = int(float_I)
        int_R = int(float_R)

        # calculation of the decimal part of the internal variables
        decimal_s = float_S - int_S
        decimal_i = float_I - int_I
        decimal_r = float_R - int_R

        current_n = int(int_S + int_I + int_R) #current values of N

        while current_n < self.N:
            #following loop works the approximation in case current_n is minor than N
            #current_n and S or I or R which have the biggest decimal part is incremented by one 

            if (decimal_s > decimal_i) and (decimal_s > decimal_r) and (int_S > self.S_vector[-1]):
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


    def Evolve(self):
        '''
        The method evolves the epidemic day by day through the application of the differetnial
        equation of the SIR model.
        SIR model works with float values, but the number of susceptible, infected, and
        recovered individuals must be whole numbers (integers).
        Therefore, the algorithm incorporates a method to ensure accurate approximation.
        Values of the parameters are saved by filling the lists created in the constructor.
        '''

        #internal variable for the calculation
        diffeq_S = self.S
        diffeq_I = self.I
        diffeq_R = self.R
        gamma = self.gamma
        beta = self.beta
        vax_request = None

        while self.I_vector[-1] != 0:

            vax_request, gamma, beta = self.Vaccine(vax_request, gamma, beta)

            diffeq_S, diffeq_I, diffeq_R = self.DifferentialEq(diffeq_S, diffeq_I, diffeq_R, gamma, beta)

            int_S, int_I, int_R = self.Approximation(diffeq_S, diffeq_I, diffeq_R)

            self.day += 1
            self.S_vector.append(int_S)
            self.I_vector.append(int_I)
            self.R_vector.append(int_R)


    def PrintResults(self):
        '''
        This function logs the main parameters of the simulation to the terminal.
        '''

        print("-----------------------")
        print("Dimension of the population:", self.N)
        print("Selected scenario:", self.scenario)
        if self.triggerday != None:
            print("Vaccine/isolation day:", self.triggerday)
        elif self.scenario != "no measures" and self.triggerday == None:
            print("No Vaccine/isolation measures needed.")
        print("Percentage of infected population:", (self.R_vector[-1]/self.N)*100, "%")
        print("Duration of the epidemic:",  self.day)
        print("-----------------------")