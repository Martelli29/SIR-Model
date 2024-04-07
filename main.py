import input as inp
import epidemic_class as cl 
import plot as dr

if __name__=="__main__":
    
    gamma, beta= inp.SetPar()
    t= inp.SetT()
    s,i,r= inp.SetSIR()
    inp.Inspector(gamma, beta, t, s, i, r)
    SIR=cl.EpidemicSIR(t, s, i, r, gamma, beta)
    SIR.Evolve()
    dr.plot(t, SIR.S_vector, SIR.I_vector, SIR.R_vector)
