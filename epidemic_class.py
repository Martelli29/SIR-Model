
class EpidemicSIR:
    def __init__(self, t, S, I, R, gamma, beta):
        self.t = int(t)  
        self.S = int(S)
        self.I = int(I)  
        self.R = int(R)  
        self.N = int(S + I + R)  
        self.gamma = gamma  # healing probability
        self.beta = beta    # infection probability

        self.S_vector = []
        self.I_vector = []
        self.R_vector = []

    def Evolve(self):
        # Il metodo fa evolvere l'epidemia di un giorno
        # Applico equazioni differenziali del modello SIR
        # Poi trasformo i risultati ottenuti in valori interi
        self.S_vector.append(self.S) #day 0
        self.I_vector.append(self.I) #day 0
        self.R_vector.append(self.R) #day 0

        delta_s = 0.0 
        delta_i = 0.0
        delta_r = 0.0

        db_s = self.S #qua assegno il valore di S a db
        db_i = self.I #idem
        db_r = self.R #idem

        decimal_s = 0.0
        decimal_i = 0.0
        decimal_r = 0.0

        for i in range(1, self.t):
            # Calcolo il cambiamento delle variabili dopo un giorno
            delta_s = ((-self.beta) * db_s * db_i) / self.N
            delta_i = ((self.beta * db_s * db_i / self.N) - self.gamma * db_i)
            delta_r = self.gamma * db_i

            # db è il valore vero, poi separo in parte intera e parte decimale e li metto in s e deimals
            db_s += delta_s
            db_i += delta_i
            db_r += delta_r

            # Trasformo i valori ottenuti in parte intera e parte decimale
            # Assegno parte intera a variabili di S I R originali
            self.S = int(db_s)
            self.I = int(db_i)
            self.R = int(db_r)
            # Assegno parte decimale a apposite variabili
            decimal_s = db_s - self.S
            decimal_i = db_i - self.I
            decimal_r = db_r - self.R

            # Il calcolo di S I R non conserva il valore di N
            # Approssima per difetto i valori nella conversione a int
            # Distribuisco valori restanti tra S I R in base alla parte decimale
            A = int(self.S + self.I + self.R)
            
            while A < self.N:
                if (decimal_s > decimal_i) and (decimal_s > decimal_r) and (self.S>self.S_vector[i-1]):
                    self.S += 1
                    decimal_s = 0

                elif (decimal_i > decimal_s) and (decimal_i > decimal_r):
                    self.I += 1
                    decimal_i = 0

                else:
                    # Se non c'è valore più alto degli altri aumento R
                    self.R += 1
                    decimal_r = 0
                print(i, self.S, self.I, self.R, self.N)
                A += 1

            self.S_vector.append(self.S)
            self.I_vector.append(self.I)
            self.R_vector.append(self.R)