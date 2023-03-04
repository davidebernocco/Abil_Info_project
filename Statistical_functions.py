import numpy as np
import math as mt


# Evaluate the mean of each of the 9 Nbins x Nmeasures matrices in the 
def Mean(ls_test, matr_meas):
    Mn= [list(list([]) for y in range(3)) for x in range(len(ls_test))]
    for j in range(len(ls_test)):
        for k in range(3):
            Mn[j][k].append(np.mean(matr_meas[j][k],axis=1))
    return Mn


# Evaluate the covariance matrices:
def Covariance_M(Nm, Nb, Mean1, Mean2, Matrix1, Matrix2):
    covar_matr = np.zeros((Nb,Nb),dtype=float)
    for i in range(Nb):
        for j in range(Nb):
            Sum = 0
            for n in range(Nm):
                Sum += (Matrix1[i][n] - Mean1[i])*(Matrix2[j][n] - Mean2[j])
            Sum /= (Nm - 1)
            covar_matr[i][j] = Sum
    return covar_matr
  
  
# Evaluate the correlation matrices:
def Correlation_M(MatrixC, Nb):
    corr_matr = np.zeros((Nb,Nb),dtype=float)
    for i in range(Nb):
        for j in range(Nb):
            corr_matr[i][j] = MatrixC[i][j]/mt.sqrt(MatrixC[i][i]*MatrixC[j][j])
    return corr_matr
  
  
# Build the theoretical covarince matrices based on Squared Exponential kernel:
def Correlation_theor(Nb, x, sig1, l1, sig2, l2):
    corr_matr_th = np.zeros((Nb,Nb),dtype=float)
    for i in range(Nb):
        for j in range(Nb):
            corr_matr_th[i][j] = (np.sqrt(2.*l1*l2)*np.exp(-(np.sqrt((x[i] - x[j])**2.)**2./(l1**2. + l2**2.)))*sig1*sig2)/np.sqrt(l1**2. + l2**2.)
    return corr_matr_th
  
  
# Evaluate the residuals between measured and theoretical self-correlation and cross-correlation matrices:
def Residuals_M(Cth, C, R, Nb, Nm):
    res_matr = np.zeros((Nb,Nb),dtype=float)
    for i in range(Nb):
        for j in range(Nb):
            res_matr[i][j] = (Cth[i][j] - C[i][j])*(mt.sqrt((Nm-1)/((1+ R[i][j])*Cth[i][i]*Cth[j][j])))
    return res_matr
  
  
# Calculate the standard deviation of the unwrapped residual matrices ( now seen as (Nbins)^2 long arrays)
def Stdv(resM, Nb):
    rms_deviation = []
    for m in range(len(Res)):
        rms_deviation.append(np.std(resM[m].reshape(Nb**2)))
    return rms_deviation
  
  
# Tests which theoretical multipole covariance corresponds to the selected measured covariance:
def Test(vet):
    for i in range(len(vet)):
        minimum = np.min(np.abs(1-vet[i]))
        for j in range(6):
            if np.abs(1-vet[i][j]) == minimum:
                print(f'In the test{ i//6 + 1 } the Cmeas matrix for the dipoles{ i - 6*(i//6) } is mostly compatible with the Cth matrix for the dipoles{j}')
        minimum = 0
