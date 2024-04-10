
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
        self.V = False

    def vaccine(self):
        if self.I > 0.2*self.N or self.V == True:
            self.V == True
            self.gamma = self.gamma*2
            self.beta = self.beta/2

    def Evolve(self, bol):
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
        
        while self.I != 0:
    
            if bol == False:
                pass
            elif bol == True:
                self.vaccine()
            
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


