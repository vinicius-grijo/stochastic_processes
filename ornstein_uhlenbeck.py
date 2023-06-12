import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import scienceplots
plt.style.use([ 'notebook', 'grid','bright'])
np.random.seed(123)

def ornstein_uhlenbeck( alpha=1, sigma=1, T=1, N=100 ):
    #number of elements = 1 + T*N
    t = np.arange(0, T + 1 / N, 1 / N)
    #random increments
    dW = np.array( [0] )
    dW = np.concatenate(  (dW,  np.random.normal( 0, np.sqrt(1/N), N*T )) )

    W = np.cumsum(dW)

    X = np.array( [1] )

    for i in range( T*N ):
        value = X[i] + ( -1*alpha*X[i] )*( t[i+1] - t[i] ) + (sigma)*(W[i+1] - W[i])
        X = np.concatenate( (X, [value]) )

    return (t,X)



def main():
    #time interval
    T = 1
    # number of divisions of [0,1]
    N = 200
    #parameters
    alpha= 1
    sigma = 1

    process_1 = ornstein_uhlenbeck(alpha=alpha, sigma=sigma, T=T, N=N)
    process_2 = ornstein_uhlenbeck(alpha=alpha, sigma=sigma, T=T, N=N)
    process_3 = ornstein_uhlenbeck(alpha=alpha, sigma=sigma, T=T, N=N)
    process_4 = ornstein_uhlenbeck(alpha=alpha, sigma=sigma, T=T, N=N)
    process_5 = ornstein_uhlenbeck(alpha=alpha, sigma=sigma, T=T, N=N)

    # plt.title('Simulating Ornstein-Uhlenbeck Processes')
    # plt.plot(process_1[0], process_1[1], linewidth=1, label='process_1')
    # plt.plot(process_2[0], process_2[1], linewidth=1, label='process_2')
    # plt.plot(process_3[0], process_3[1], linewidth=1, label='process_3')
    # plt.legend()
    # plt.show()

    fig=plt.figure()
    plt.xlim( 0, 1 )
    plt.ylim( -1, 3 )
    plt.title('Simulating Ornstein-Uhlenbeck Processes')
    l_1, = plt.plot( [], [], linewidth=1, label='process_1' )
    l_2, = plt.plot( [], [], linewidth=1, label='process_2' )
    l_3, = plt.plot( [], [], linewidth=1, label='process_3' )
    l_4, = plt.plot( [], [], linewidth=1, label='process_4')
    l_5, = plt.plot( [], [], linewidth=1, label='process_5')
    plt.legend()

    metadata = dict( title='ornstein_uhlenbeck', artist='me' )
    writer = PillowWriter(fps=(N*T+1), metadata=metadata)

    with writer.saving(fig, 'ornstein_uhlenbeck.gif', 100):
        for i in range(N*T+1):
            l_1.set_data( process_1[0][0:i], process_1[1][0:i] )
            l_2.set_data( process_2[0][0:i], process_2[1][0:i] )
            l_3.set_data( process_3[0][0:i], process_3[1][0:i] )
            l_4.set_data( process_4[0][0:i], process_4[1][0:i] )
            l_5.set_data( process_5[0][0:i], process_5[1][0:i] )
            writer.grab_frame()

if __name__ == '__main__':
    main()