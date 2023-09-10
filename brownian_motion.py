import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import scienceplots
plt.style.use([ 'notebook', 'grid','bright'])
np.random.seed(123)

def brownian_motion( x_0=0, mu=0, sigma=1, T=1, N=100 ):
    #number of elements = 1 + T*N
    t = np.arange(0, T + 1 / N, 1 / N)
    #random increments
    dW = np.array( [0] )
    dW = np.concatenate(  (dW,  np.random.normal( 0, np.sqrt(1/N), N*T )) )

    W = np.cumsum(dW)

    X = np.array( [x_0] )

    for i in range( T*N ):
        value = X[i] + mu*( t[i+1] - t[i] ) + (sigma)*(W[i+1] - W[i])
        X = np.concatenate( (X, [value]) )

    return (t,X)



def main():
    #time interval
    T = 10
    # number of divisions of [0,1]
    N = 100
    #parameters
    x_0 = 0
    mu = 0
    sigma = 1

    path_1 = brownian_motion(x_0=x_0, mu=mu, sigma=sigma, T=T, N=N)
    path_2 = brownian_motion(x_0=x_0, mu=mu, sigma=sigma, T=T, N=N)
    path_3 = brownian_motion(x_0=x_0, mu=mu, sigma=sigma, T=T, N=N)
    path_4 = brownian_motion(x_0=x_0, mu=mu, sigma=sigma, T=T, N=N)
    path_5 = brownian_motion(x_0=x_0, mu=mu, sigma=sigma, T=T, N=N)

    # plt.xlim( 0, T+1)
    # plt.title('Simulating Brownian Motion')
    # plt.plot(path_1[0], path_1[1], linewidth=1, label='path_1')
    # plt.plot(path_2[0], path_2[1], linewidth=1, label='path_2')
    # plt.plot(path_3[0], path_3[1], linewidth=1, label='path_3')
    # plt.plot(path_4[0], path_4[1], linewidth=1, label='path_4')
    # plt.plot(path_5[0], path_5[1], linewidth=1, label='path_5')
    # plt.legend()
    # plt.savefig('brownian_motion.png')
    # plt.show()

    fig=plt.figure()
    plt.xlim( 0, T+1)
    plt.ylim(-(mu + 10*sigma), mu + 10*sigma)
    plt.title('Simulating Brownian Motion')
    l_1, = plt.plot( [], [], linewidth=1, label='path_1' )
    l_2, = plt.plot( [], [], linewidth=1, label='path_2' )
    l_3, = plt.plot( [], [], linewidth=1, label='path_3' )
    l_4, = plt.plot( [], [], linewidth=1, label='path_4')
    l_5, = plt.plot( [], [], linewidth=1, label='path_5')
    plt.legend()

    metadata = dict( title='brownian_motion', artist='me' )
    writer = PillowWriter(fps=(N*T+1), metadata=metadata)

    with writer.saving(fig, 'brownian_motion.gif', 100):
        for i in range(N*T+1):
            l_1.set_data( path_1[0][0:i], path_1[1][0:i] )
            l_2.set_data( path_2[0][0:i], path_2[1][0:i] )
            l_3.set_data( path_3[0][0:i], path_3[1][0:i] )
            l_4.set_data( path_4[0][0:i], path_4[1][0:i] )
            l_5.set_data( path_5[0][0:i], path_5[1][0:i] )
            writer.grab_frame()

if __name__ == '__main__':
    main()