import numpy as np
from numpy import linalg
import Param as P

class Trim():
    def __init__(self,Va,gamma,R,alpha,beta,phi):
        # These parameters are specified by the user
        self.Va = Va        # Trim airspeed, m/s
        self.gamma = gamma  # Trim flight path angle, rad
        self.R = R          # Trim turn radius, m
        self.alpha = alpha  # Trim angle of attack, rad
        self.beta = beta    # Trim side slip angle, rad
        self.phi = phi      # Trim roll angle, rad

        # These parameters are calculated based off of the specified parameters above

        # Body frame velocities
        self.u = 0.0        # x-axis, m/s
        self.v = 0.0        # y-axis, m/s
        self.w = 0.0        # z-axis, m/s

        # Pitch angle
        self.theta = 0.0    # units rad

        # Angular rates
        self.p = 0.0        # Roll rate along x-axis, rad/s
        self.q = 0.0        # Pitch rate along y-axis, rad/s
        self.r = 0.0        # Yaw rate along z-axis, rad/s

        # Control surface coefficients
        self.delta_e = 0.0       # Elevator
        self.delta_a = 0.0       # Aileron
        self.delta_r = 0.0       # Rudder
        self.delta_t = 0.0       # Throttle

        # Lift Model coefficients
        self.sigma = 0.0         # Sigmoid function
        self.C_L = 0.0     # Lift coefficient
        self.C_D = 0.0     # Drag coefficient
        self.C_X = 0.0
        self.C_X_q = 0.0   
        self.C_X_delta_e = 0.0
        self.Z = 0.0
        self.Z_q = 0.0
        self.Z_delta_e = 0.0

    def getBodyFrameVelocities(self):
        self.u = self.Va*np.cos(self.alpha)*np.cos(self.beta)
        self.v = self.Va*np.sin(self.beta)
        self.w = self.Va*np.sin(self.alpha)*np.cos(self.beta)

    def getPitchAngle(self):
        self.theta = self.alpha + self.gamma

    def getAngularRates(self):

        self.p = -self.Va/self.R*np.sin(self.theta)
        self.q = self.Va/self.R*np.sin(self.phi)*np.cos(self.theta)
        self.r = self.Va/self.R*np.cos(self.phi)*np.cos(self.theta)
        # print('p %5.4e' % self.p)



    def getElevator(self):
        # The code is broken down into several steps to increase readability
        temp1 = (P.Jxz*(self.p**2 - self.r**2) + (P.Jx - P.Jz)*self.p*self.r)/(1/2*P.rho*self.Va**2*P.c*P.S)
        temp2 = temp1 - P.C_m_0 - P.C_m_alpha*self.alpha - P.C_m_q*(P.c*self.q/(2*self.Va))

        self.delta_e = temp2/P.C_m_delta_e

    def getThrottle(self):
        # The code is broken down into several steps to increase readability
        temp1 = 2*P.m*(-self.r*self.v + self.q*self.w + P.g*np.sin(self.theta))
        temp2 = -P.rho*(self.Va)**2*P.S*(self.C_X + self.C_X_q*P.c*self.q/(2*self.Va) + self.C_X_delta_e*self.delta_e)
        temp3 = (temp1 + temp2)/(P.rho*P.Sprop*P.Cprop*P.kmotor**2)
        temp4 = self.Va**2/P.kmotor**2
        self.delta_t = np.sqrt(temp3 + temp4)

    def getAileronAndRudder(self):
        # The code is broken down into several steps to increase readability
        matrix1 = np.matrix([[P.C_p_delta_a, P.C_p_delta_r], [P.C_r_delta_a, P.C_r_delta_r]])
        matrix1 = linalg.inv(matrix1)


        temp1 = (-P.Gamma1*self.p*self.q + P.Gamma2*self.q*self.r)/(0.5*P.rho*self.Va**2*P.S*P.b)
        temp2 = P.C_p_p*(P.b*self.p/(2*self.Va))
        temp3 = P.C_p_r*(P.b*self.r/(2*self.Va))
        temp4 = (-P.Gamma7*self.p*self.q + P.Gamma1*self.q*self.r)/(0.5*P.rho*self.Va**2*P.S*P.b)
        temp5 = P.C_r_p*(P.b*self.p/(2*self.Va))
        temp6 = P.C_r_r*(P.b*self.r/(2*self.Va))

        matrix2 = np.matrix([[temp1 - P.C_p_0 - P.C_p_beta*self.beta - temp2 - temp3],
            [temp4 - P.C_r_0 - P.C_r_beta*self.beta - temp5 - temp6]])

        controls = matrix1*matrix2

        self.delta_a = controls[0,0]
        self.delta_r = controls[1,0]

    def getSigma(self):
        # The code is broken down into several steps to increase readability
        numerator = 1+np.exp(-P.M*(self.alpha-P.alpha_0))+np.exp(P.M*(self.alpha+P.alpha_0))
        den = ((1 + np.exp(-P.M*(self.alpha-P.alpha_0)))*(1+np.exp(P.M*(self.alpha+P.alpha_0))))
        self.sigma = numerator/den

    def getLiftModelCoeff(self):
        self.C_L =  (1-self.sigma)*(P.C_L_0 + P.C_L_alpha*self.alpha) + \
        self.sigma*(2*np.sign(self.alpha)*np.sin(self.alpha)**2*np.cos(self.alpha))

    def getDragModelCoeff(self):
        AR = P.b**2/P.S
        self.C_D =P.C_D_p + (P.C_L_0 + P.C_L_alpha*self.alpha)**2/(np.pi*P.e*AR)

    def getLiftCoeff(self):
        self.getSigma()
        self.getLiftModelCoeff()
        self.getDragModelCoeff()



        self.C_X =           -self.C_D*np.cos(self.alpha)  +          self.C_L*np.sin(self.alpha)
        self.C_X_q =         -P.C_D_q*np.cos(self.alpha) +            P.C_L_q*np.sin(self.alpha)
        self.C_X_delta_e =   -P.C_D_delta_e*np.cos(self.alpha) +      P.C_L_delta_e*np.sin(self.alpha)
        self.C_Z =           -self.C_D*np.sin(self.alpha) -           self.C_L*np.cos(self.alpha)
        self.C_Z_q =         -P.C_D_q*np.sin(self.alpha)-             P.C_L_q*np.cos(self.alpha)
        self.C_Z_delta_e =   -P.C_D_delta_e*np.sin(self.alpha) -      P.C_L_delta_e*np.cos(self.alpha)

        # print('Sigma %5.4e' % self.sigma)
        # print('CL', self.C_L)
        # print('CD', self.C_D)
        # print( 'C_X', self.C_X)
        # print('C_X_q ', self.C_X_q)
        # print('C_X_delta_e', self.C_X_delta_e)
        # print( 'C_Z', self.C_Z)
        # print('C_Z_q ', self.C_Z_q)
        # print('C_Z_delta_e', self.C_Z_delta_e)

    def computeTrim(self):
        self.getLiftCoeff()
        self.getBodyFrameVelocities()
        self.getPitchAngle()
        self.getAngularRates()
        self.getElevator()
        self.getThrottle()
        self.getAileronAndRudder()

    def printValues(self):
        print('x trim')
        print('pn')
        print('pe')
        print('pd')
        print('u',self.u)
        print('v',self.v)
        print('w',self.w)
        print('phi',self.phi)
        print('theta',self.theta)
        print('psi')
        print('p',self.p)
        print('q',self.q)
        print('r',self.r)

        print('u trim')
        print('delta e', self.delta_e)
        print('delta t', self.delta_t)
        print('delta a', self.delta_a)
        print('delta r', self.delta_r)




if __name__ == "__main__": 
    # Va,gamma,R,alpha,beta,phi
    Va = float(35)
    gamma = float(60*np.pi/180)
    # R = float('inf')
    alpha = -0.0018  # atan(wr/ur)
    beta = 3.9160e-29 #np.arcsin(-5.60228271932687e-27/Va)                         # vr/Va
    R = 500
    phi = np.arctan(Va**2*np.cos(gamma)/(R*P.g))

    T = Trim(Va,gamma,R,alpha,beta,phi)
    T.computeTrim()
    T.printValues()
    print('R', R)



