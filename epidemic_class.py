
class EpidemicSIR:
    '''
    EpidemicSIR contains all the information on the epidemic and the functions to system evolve.
    It takes as input all the parameters setted by the users in the input.py file.
    '''
    
    def __init__(self, S, I, R, gamma, beta):
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

        self.S_vector = []
        self.I_vector = []
        self.R_vector = []
        self.triggerday = None


    def Vaccine(self, scenario, vax_request, int_i):
        '''
        This method set the new possible values of beta and gamma once a scenario has been selected. 
        '''
        
        if vax_request == None:
        
            if scenario == "no measures":
                vax_request = False
            
            elif int_i > 0.1*self.N and scenario == "light lockdown":
                vax_request = True
                self.triggerday = self.day
                self.beta = self.beta - (0.2*self.beta)

            elif int_i > 0.1*self.N and scenario == "heavy lockdown":
                vax_request = True
                self.triggerday = self.day

                self.beta = self.beta - (0.7*self.beta)
            
            elif int_i > 0.1*self.N and scenario == "weakly effective vaccine":
                vax_request = True
                self.triggerday = self.day

                self.beta = self.beta - (0.2*self.beta)
                self.gamma = self.gamma + (0.5*self.gamma)

            elif int_i > 0.1*self.N and scenario == "strongly effective vaccine":
                vax_request = True
                self.triggerday = self.day

                self.beta = self.beta - (0.6*self.beta)
                self.gamma = self.gamma + (0.9*self.gamma)

        return vax_request


    def DifferentialEq(self, S, I, R):
        # Evolution of the epidemic by the differential equation
        deltaS = ((-self.beta) * S * I) / self.N
        deltaI = ((self.beta * S * I / self.N) - self.gamma * I)
        deltaR = self.gamma * I

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


    def Evolve(self, scenario):
        '''
        The method evolves the epidemic day by day through the application of the differetnial
        equation of the SIR model.
        SIR model works with float values, but the number of susceptible, infected, and
        recovered individuals must be whole numbers (integers).
        Therefore, the algorithm incorporates a method to ensure accurate approximation.
        Values of the parameters are saved by filling the lists created in the constructor.
        '''

        self.S_vector.append(self.S) #day 0
        self.I_vector.append(self.I) #day 0
        self.R_vector.append(self.R) #day 0

        #internal variable for the calculation
        diffeq_S = self.S
        diffeq_I = self.I
        diffeq_R = self.R
        vax_request = None

        while self.I_vector[-1] != 0:

            diffeq_S, diffeq_I, diffeq_R = self.DifferentialEq(diffeq_S, diffeq_I, diffeq_R)

            int_S, int_I, int_R = self.Approximation(diffeq_S, diffeq_I, diffeq_R)

            vax_request = self.Vaccine(scenario, vax_request, int_I)

            self.day += 1
            self.S_vector.append(int_S)
            self.I_vector.append(int_I)
            self.R_vector.append(int_R)


    def PrintResults(self, scenario):
        '''
        This function logs the main parameters of the simulation to the terminal.
        '''

        print("-----------------------")
        print("Dimension of the population:", self.N)
        print("Selected scenario:", scenario)
        if self.triggerday != None:
            print("Vaccine/isolation day:", self.triggerday)
        elif scenario != "no measures" and self.triggerday == None:
            print("No Vaccine/isolation measures needed.")
        print("Percentage of infected population:", (self.R_vector[-1]/self.N)*100, "%")
        print("Duration of the epidemic:",  self.day)
        print("-----------------------")