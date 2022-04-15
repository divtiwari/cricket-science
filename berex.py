def berex(avg, r, balls, wickets=10):
    """
    Return the mean and standard deviation of the Bernoulli Run Expectation for a player

    avg: Average
    r: score/concede rate; this is either SR/100 or Econ/6
    balls: Total number of balls in innings
    wickets: Number of wickets available
    """
    from math import sqrt
    from scipy.stats import binom

    probDismissal = r/avg
    scoreRate = r/(1-probDismissal)     # Adjust to scoring rate excluding dismissals

    Eout = 0
    Eover = 0
    Eoutsq = 0
    Eoversq = 0

    for b in range(wickets, balls+1):
        Eout += scoreRate * (b - wickets) * binom.pmf(wickets-1, b-1, probDismissal) * probDismissal
        Eoutsq += (scoreRate * (b - wickets))**2 * binom.pmf(wickets-1, b-1, probDismissal) * probDismissal

    for w in range(0, wickets):
        Eover += scoreRate * (balls - w) * binom.pmf(w, balls, probDismissal)
        Eoversq += (scoreRate * (balls - w))**2 * binom.pmf(w, balls, probDismissal)
    
    mean = Eout + Eover
    sd = sqrt(Eoutsq + Eoversq - mean**2)

    return (mean, sd)