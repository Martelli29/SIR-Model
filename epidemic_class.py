
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

        self.t = 1
        self.S = int(S)
        self.I = int(I)  
        self.R = int(R)  
        self.N = int(S + I + R) # total population
        self.gamma = gamma      # healing probability
        self.beta = beta        # infection probability

        self.S_vector = []
        self.I_vector = []
        self.R_vector = []
        self.triggerday = None

    def Vaccine(self, scenario):
        '''
        This method set the new possible values of beta and gamma once a scenario has been selected. 
        '''

        if scenario == 1:
            self.beta = self.beta - (0.2*self.beta)
        
        elif scenario == 2:
            self.beta = self.beta - (0.7*self.beta)
        
        elif scenario == 3:
            self.beta = self.beta - (0.2*self.beta)
            self.gamma = self.gamma + (0.5*self.gamma)

        elif scenario == 4:
            self.beta = self.beta - (0.6*self.beta)
            self.gamma = self.gamma + (0.9*self.gamma)


    def Evolve(self, bol, scenario):
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
        db_s = self.S
        db_i = self.I
        db_r = self.R
        self.trig = bol
        
        while self.I != 0:
            
            if self.trig == False:
                pass

            elif self.trig == True and self.I > 0.1*self.N:
                self.trig = False
                self.triggerday = self.t-1
                self.Vaccine(scenario)
            
            # Evolution of the epidemic by the differential equation
            delta_s = ((-self.beta) * db_s * db_i) / self.N
            delta_i = ((self.beta * db_s * db_i / self.N) - self.gamma * db_i)
            delta_r = self.gamma * db_i

            # assignment of the new variables to the internal variable
            db_s += delta_s
            db_i += delta_i
            db_r += delta_r

            # the integer part of the internal variables are assigned to the parameters S,I,R
            self.S = int(db_s)
            self.I = int(db_i)
            self.R = int(db_r)

            # calculation of the decimal part of the internal variables
            decimal_s = db_s - self.S
            decimal_i = db_i - self.I
            decimal_r = db_r - self.R
            
            A = int(self.S + self.I + self.R) #current values of N
            
            while A < self.N:
                #following loop works the approximation in case A is minor than N
                #A and S or I or R which have the biggest decimal part is incremented by one 
        
                if (decimal_s > decimal_i) and (decimal_s > decimal_r) and (self.S>self.S_vector[self.t-1]):
                    self.S += 1
                    decimal_s = 0

                elif (decimal_i > decimal_s) and (decimal_i > decimal_r):
                    self.I += 1
                    decimal_i = 0

                else:
                    self.R += 1
                    decimal_r = 0
                A += 1

            self.t += 1
            self.S_vector.append(self.S)
            self.I_vector.append(self.I)
            self.R_vector.append(self.R)
    
    
    def PrintResults(self):
        '''
        This function logs the main parameters of the simulation to the terminal.
        '''

        print("-----------------------")
        print("Dimension of the population:", self.N)
        if self.triggerday != None:
            print("Vaccine/isolation day:", self.triggerday)
        elif self.trig == True and self.triggerday == None:
            print("No Vaccine/isolation measures needed.")
        else:
            pass
        print("Percentage of infected population:", (self.R/self.N)*100, "%")
        print("Duration of the epidemic:",  self.t)
        print("-----------------------")