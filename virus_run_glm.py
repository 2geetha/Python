# virus_run_glm_v003.py
# agent-based simulation experiment with analysis of deviance
# simulation run with NetLogo model Virus on a Network

# run the program in Enthought Canopy, setting the working directory
# to be the same directory as the edited file and the experimental data
import numpy as np
import pandas as pd
import statsmodels.api as sm

# read in summary results and code the experimental factors
virus = pd.read_csv("virus_results.csv")

# check input DataFrame
print(virus)

Intercept = np.array([1] * 20)

# use dictionary object for mapping to 0/1 binary codes
degree_to_binary = {3 : 0, 5 : 1}
Connectivity = np.array(virus['degree'].map(degree_to_binary))

# use dictionary object for mapping to 0/1 binary codes
spread_to_binary = {5 : 0, 10 : 1}
Susceptibility = np.array(virus['spread'].map(spread_to_binary))

Connectivity_Susceptibility = Connectivity * Susceptibility

Design_Matrix = np.array([Intercept, Connectivity, Susceptibility, Connectivity_Susceptibility]).T

print(Design_Matrix)

Market_Share = np.array(virus['infected'])

# generalized linear model for response variable that is a proportion
glm_binom = sm.GLM(Market_Share, Design_Matrix, family=sm.families.Binomial())
res = glm_binom.fit()
print res.summary()
        


