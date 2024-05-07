import matplotlib.pyplot as plt

def plot(S, I, R, vaccine_day):
    '''
    This function takes as input three lists and uses the functionality of matplotlib
    to plot them in a graph.
    '''
    
    plt.plot(S, color="blue")
    plt.plot(I, color="red")
    plt.plot(R, color="black")

    if vaccine_day != None:
        plt.axvline(vaccine_day, color='gray', linestyle='dashed', linewidth=1)
    else:
        pass
    
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.grid(True)
    
    plt.title("SIR model")
    plt.legend(["Subsceptible", "Infected", "Removed"])
    
    plt.show()