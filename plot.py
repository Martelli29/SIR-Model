import matplotlib.pyplot as plt


def plot(S: list, I: list, R: list, vaccine_day: None | int) -> None:
    '''
    This function is used for plotting the trend of the epidemic in a graph through
    matplotlib library.

    4 parameters needed:
    S (list): contains the number of subsceptible in the population for each day in a sequential order.
    I (list): contains the number of infected in the population for each day in a sequential order.
    R (list): contains the number of removed in the population for each day in a sequential order.
    vaccine_day (int): day on which contromeasures were taken.
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
