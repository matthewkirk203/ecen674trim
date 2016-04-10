import numpy as np
from numpy import linalg
import Param as P
from scipy.optimize import leastsq

class Trim():
    def __init__(self,Va,gamma,R):
        # These parameters are specified by the user
        self.Va = Va        # Trim airspeed, m/s
        self.gamma = gamma  # Trim flight path angle, rad
        self.R = R          # Trim turn radius, m

        # These parameters are calculated based off of the specified parameters above

        # Body frame velocities
        self.u = 0.0        # x-axis, m/s
        self.v = 0.0        # y-axis, m/s
        self.w = 0.0        # z-axis, m/s

        # Pitch angle
        self.theta = 0.0    # units rad
        self.psi = 0.0

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

        # fx
        self.fx = np.zeros((12,1))


        #xdotTrim
        self.xdotTrim = np.matrix([[0],                                 # pn dot
                               [0],                                 # pe dot
                               [self.Va*np.sin(self.gamma)],        # h dot
                               [0],                                 # u dot
                               [0],                                 # v dot
                               [0],                                 # w dot
                               [0],                                 # phi dot
                               [0],                                 # theta dot
                               [self.Va/self.R*np.cos(self.gamma)], # psi dot
                               [0],                                 # p dot
                               [0],                                 # q dot
                               [0]])                                # r dot 

        self.alpha_dl = self.gamma
        self.beta_dl = 0.0
        self.phi_dl = 0.0
        self.J_dl = 0.0

        self.alpha = 0.0
        self.beta = 0.0
        self.phi = 0.0
        self.J = 0.0

        self.epsilon = 0.005
        self.K = 0.00005

    def getBodyFrameVelocities(self, alpha, beta): # I have verified this function
        self.u = self.Va*np.cos(alpha)*np.cos(beta)
        self.v = self.Va*np.sin(beta)
        self.w = self.Va*np.sin(alpha)*np.cos(beta)

    def getPitchAngle(self,alpha):                  # I have verified this function
        self.theta = alpha + self.gamma

    def getAngularRates(self,phi):                  # I have verified this function

        self.p = -self.Va/self.R*np.sin(self.theta)
        self.q = self.Va/self.R*np.sin(phi)*np.cos(self.theta)
        self.r = self.Va/self.R*np.cos(phi)*np.cos(self.theta)
        # print('p %5.4e' % self.p)



    def getElevator(self,alpha): # I have verified this function
        # The code is broken down into several steps to increase readability
        temp1 = (P.Jxz*(self.p**2 - self.r**2) + (P.Jx - P.Jz)*self.p*self.r)/(1/2*P.rho*self.Va**2*P.c*P.S)
        temp2 = temp1 - P.C_m_0 - P.C_m_alpha*alpha - P.C_m_q*(P.c*self.q/(2*self.Va))

        self.delta_e = temp2/P.C_m_delta_e

    def getThrottle(self): # I have verified this function
        # The code is broken down into several steps to increase readability
        temp1 = 2*P.m*(-self.r*self.v + self.q*self.w + P.g*np.sin(self.theta))
        temp2 = -P.rho*(self.Va)**2*P.S*(self.C_X + self.C_X_q*P.c*self.q/(2*self.Va) + self.C_X_delta_e*self.delta_e)
        temp3 = (temp1 + temp2)/(P.rho*P.Sprop*P.Cprop*P.kmotor**2)
        temp4 = self.Va**2/P.kmotor**2
        self.delta_t = np.sqrt(temp3 + temp4)

    def getAileronAndRudder(self,beta):  # I have verified this function
        # The code is broken down into several steps to increase readability
        matrix1 = np.matrix([[P.C_p_delta_a, P.C_p_delta_r], [P.C_r_delta_a, P.C_r_delta_r]])
        matrix1 = linalg.inv(matrix1)


        temp1 = (-P.Gamma1*self.p*self.q + P.Gamma2*self.q*self.r)/(0.5*P.rho*self.Va**2*P.S*P.b)
        temp2 = P.C_p_p*(P.b*self.p/(2*self.Va))
        temp3 = P.C_p_r*(P.b*self.r/(2*self.Va))
        temp4 = (-P.Gamma7*self.p*self.q + P.Gamma1*self.q*self.r)/(0.5*P.rho*self.Va**2*P.S*P.b)
        temp5 = P.C_r_p*(P.b*self.p/(2*self.Va))
        temp6 = P.C_r_r*(P.b*self.r/(2*self.Va))

        matrix2 = np.matrix([[temp1 - P.C_p_0 - P.C_p_beta*beta - temp2 - temp3],
            [temp4 - P.C_r_0 - P.C_r_beta*beta - temp5 - temp6]])

        controls = matrix1*matrix2

        self.delta_a = controls[0,0]
        self.delta_r = controls[1,0]

    def getSigma(self,alpha): # I have verified this function
        # The code is broken down into several steps to increase readability
        numerator = 1+np.exp(-P.M*(alpha-P.alpha_0))+np.exp(P.M*(alpha+P.alpha_0))
        den = ((1 + np.exp(-P.M*(alpha-P.alpha_0)))*(1+np.exp(P.M*(alpha+P.alpha_0))))
        self.sigma = numerator/den

    def getLiftModelCoeff(self,alpha): # I have verified this function
        self.C_L =  (1-self.sigma)*(P.C_L_0 + P.C_L_alpha*alpha) + \
        self.sigma*(2*np.sign(alpha)*np.sin(alpha)**2*np.cos(alpha))

    def getDragModelCoeff(self,alpha): # I have verified this function
        AR = P.b**2/P.S
        self.C_D =P.C_D_p + (P.C_L_0 + P.C_L_alpha*alpha)**2/(np.pi*P.e*AR)

    def getLiftCoeff(self,alpha): # I have verified this function
        self.getSigma(alpha)
        self.getLiftModelCoeff(alpha)
        self.getDragModelCoeff(alpha)



        self.C_X =           -self.C_D*np.cos(alpha)  +          self.C_L*np.sin(alpha)
        self.C_X_q =         -P.C_D_q*np.cos(alpha) +            P.C_L_q*np.sin(alpha)
        self.C_X_delta_e =   -P.C_D_delta_e*np.cos(alpha) +      P.C_L_delta_e*np.sin(alpha)
        self.C_Z =           -self.C_D*np.sin(alpha) -           self.C_L*np.cos(alpha)
        self.C_Z_q =         -P.C_D_q*np.sin(alpha)-             P.C_L_q*np.cos(alpha)
        self.C_Z_delta_e =   -P.C_D_delta_e*np.sin(alpha) -      P.C_L_delta_e*np.cos(alpha)

        # print('Sigma %5.4e' % self.sigma)
        # print('CL', self.C_L)
        # print('CD', self.C_D)
        # print( 'C_X', self.C_X)
        # print('C_X_q ', self.C_X_q)
        # print('C_X_delta_e', self.C_X_delta_e)
        # print( 'C_Z', self.C_Z)
        # print('C_Z_q ', self.C_Z_q)
        # print('C_Z_delta_e', self.C_Z_delta_e)

    def compute_X_Trim_U_Trim(self,alpha,beta,phi):
        self.getLiftCoeff(alpha)
        self.getBodyFrameVelocities(alpha,beta)
        self.getPitchAngle(alpha)
        self.getAngularRates(phi)
        self.getElevator(alpha)
        self.getAileronAndRudder(beta)
        self.getThrottle()

    def printValues(self):
        print('\n\n x trim')
        print('pn')
        print('pe')
        print('pd')
        print('u',self.u)
        print('v',self.v)
        print('w',self.w)
        print('phi',self.phi)
        print('theta',self.theta)
        print('psi', self.psi)
        print('p',self.p)
        print('q',self.q)
        print('r',self.r)

        print('\n\n u trim')
        print('delta e', self.delta_e)
        print('delta t', self.delta_t)
        print('delta a', self.delta_a)
        print('delta r', self.delta_r)

        print('\n\n xhatdot')
        print('pndot', self.fx[0,0])
        print('pedot', self.fx[1,0])
        print('hdot', self.fx[2,0])
        print('udot', self.fx[3,0])
        print('vdot', self.fx[4,0])
        print('wdot', self.fx[5,0])
        print('phidot', self.fx[6,0])
        print('thetadot', self.fx[7,0])
        print('psidot', self.fx[8,0])
        print('pdot', self.fx[9,0])
        print('qdot', self.fx[10,0])
        print('rdot', self.fx[11,0])

        print('beta ', self.beta)
        print('alpha ', self.alpha)

    def get_f_x_u(self,alpha,beta,phi):
        # Calculates xhatdot

        self.compute_X_Trim_U_Trim(alpha,beta,phi)

        cos_phi = np.cos(phi)
        cos_theta = np.cos(self.theta)
        cos_psi = np.cos(self.psi)
        sin_phi = np.sin(phi)
        sin_theta = np.sin(self.theta)
        sin_psi = np.sin(self.psi)

        temp1 = P.rho*Va**2*P.S/(2*P.m)

        pndot = (cos_theta*cos_psi*self.u + (sin_phi*sin_theta*cos_psi - 
            cos_phi*sin_psi)*self.v + (cos_phi*sin_theta*cos_psi + 
            sin_phi*sin_psi)*self.w)

        pedot = (cos_theta*sin_psi*self.u + (sin_phi*sin_theta*sin_psi +
            cos_phi*cos_psi)*self.v + (cos_phi*sin_theta*sin_psi - 
            sin_phi*cos_psi)*self.w)

        hdot = (self.u*sin_theta - self.v*sin_phi*cos_theta -
            self.w*cos_phi*cos_theta)

        udot = (self.r*self.v - self.q*self.w - P.g*sin_theta + 
            temp1*(self.C_X + self.C_X_q*P.c*self.q/(2*self.Va) + self.C_X_delta_e*self.delta_e) +
            P.rho*P.Sprop*P.Cprop/(2*P.m)*((P.kmotor*self.delta_t)**2 - self.Va**2))

        vdot = (self.p*self.w - self.r*self.u + P.g*cos_theta*sin_phi + temp1*
            (P.C_Y_0 + P.C_Y_beta*beta + P.C_Y_p*P.b*self.p/(2*self.Va) + P.C_Y_r*P.b*self.r/(2*self.Va) +
             P.C_Y_delta_a*self.delta_a + P.C_Y_delta_r*self.delta_r))

        wdot = (self.q*self.u - self.p*self.v + P.g*cos_theta*cos_phi + temp1*(self.C_Z + 
            self.C_Z_q*P.c*self.q/(2*self.Va) + self.C_Z_delta_e*self.delta_e))

        phidot = self.p + self.q*sin_phi*np.tan(self.theta) + self.r*cos_phi*np.tan(self.theta)

        thetadot = self.q*cos_phi - self.r*sin_phi

        psidot = self.q*sin_phi*(1/cos_theta) + self.r*cos_phi*(1/cos_theta)

        pdot = (P.Gamma1*self.p*self.q - P.Gamma2*self.q*self.r + (1/2)*P.rho*self.Va**2*P.S*P.b*
            (P.C_p_0 + P.C_p_beta*beta + P.C_p_p*P.b*self.p/(2*self.Va) + P.C_p_r*P.b*self.r/(2*self.Va) +
             P.C_p_delta_a*self.delta_a + P.C_p_delta_r*self.delta_r))

        qdot = (P.Gamma5*self.p*self.r - P.Gamma6*(self.p**2 - self.r**2) + P.rho*self.Va**2*P.S*P.c/(2*P.Jy)*
            (P.C_m_0 + P.C_m_alpha*alpha + P.C_m_q*P.c*self.q/(2*self.Va) + P.C_m_delta_e*self.delta_e))

        rdot = (P.Gamma7*self.p*self.q - P.Gamma1*self.q*self.r + (1/2)*P.rho*self.Va**2*P.S*P.b*
            (P.C_r_0 + P.C_r_beta*beta + P.C_r_p*P.b*self.p/(2*self.Va) + P.C_r_r*P.b*self.r/(2*self.Va) +
            P.C_r_delta_a*self.delta_a + P.C_r_delta_r*self.delta_r))

        self.fx = np.matrix([[pndot],
                             [pedot],
                             [hdot],
                             [udot],
                             [vdot],
                             [wdot],
                             [phidot],
                             [thetadot],
                             [psidot],
                             [pdot],
                             [qdot],
                             [rdot]])

        return [self.fx[0,0], self.fx[1,0], self.fx[2,0], self.fx[3,0], self.fx[4,0], self.fx[5,0],
                self.fx[6,0], self.fx[7,0], self.fx[8,0], self.fx[9,0], self.fx[10,0], self.fx[11,0]]

    
    def getJ(self,alpha,beta,phi):

        self.get_f_x_u(alpha,beta,phi)
        # print('fx ', self.fx)
        return np.linalg.norm(self.xdotTrim - self.fx)**2



    def minimizeJ(self):

        N = 1000;

        for x in range(0, N):
            self.alpha = self.alpha_dl + self.epsilon
            self.beta = self.beta_dl + self.epsilon
            self.phi = self.phi_dl + self.epsilon
            self.J_dl = self.getJ(self.alpha_dl,self.beta_dl,self.phi_dl)
            # print('J_dl ', self.J_dl)
            dJ_dAlpha = (self.getJ(self.alpha,self.beta_dl,self.phi_dl) - self.J_dl)/self.epsilon
            dJ_dBeta = (self.getJ(self.alpha_dl,self.beta,self.phi_dl) - self.J_dl)/self.epsilon
            dJ_dPhi = (self.getJ(self.alpha_dl,self.beta_dl,self.phi) - self.J_dl)/self.epsilon

            self.alpha_dl = self.alpha_dl -self.K*dJ_dAlpha
            self.beta_dl = self.beta_dl - self.K*dJ_dBeta
            self.phi_dl = self.phi_dl - self.K*dJ_dPhi

            # print('alpha ', self.alpha_dl)
            # print('beta ', self.beta_dl)
            # print('phi ', self.phi_dl)
            # print('\n\n')



    def residuals(self,p,y):
        alpha,beta,phi = p

        # print('y', y)
        # print('p', p)
        fx = self.get_f_x_u(alpha,beta,phi)
        # print('fx', fx)
        fx = np.array(fx)

        err = y - fx
        # print('err', err)
        return err

    def minimize(self):
        p0 = [0,0,0]
        y = [self.xdotTrim[0,0], self.xdotTrim[1,0], self.xdotTrim[2,0], self.xdotTrim[3,0], self.xdotTrim[4,0], self.xdotTrim[5,0],
             self.xdotTrim[6,0], self.xdotTrim[7,0], self.xdotTrim[8,0], self.xdotTrim[9,0], self.xdotTrim[10,0], self.xdotTrim[11,0]]
        y = np.array(y)
        plsq = leastsq(self.residuals, p0, args=(y))
        return plsq


if __name__ == "__main__": 
    # Va,gamma,R,alpha,beta,phi
    Va = float(35)
    gamma = float(15*np.pi/180)

    R = float(200)
  

    T = Trim(Va,gamma,R)
    plsq = T.minimize()
    print('plsq ', plsq)
    # T.get_f_x_u( 0.0810,1.1844e-07,0.454364868269413)

    # T.getLiftCoeff(1)
    T.printValues()
  



