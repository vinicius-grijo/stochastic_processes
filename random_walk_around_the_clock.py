import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import scienceplots
plt.style.use([ 'notebook', 'grid','bright'])

np.random.seed(123)

def random_walk_around_the_clock( alpha_1=1, alpha_2=1, sigma_1=0.1, sigma_2=0.1,  T=1, N=10 ):
    # number of elements = 1 + T*N
    t = np.arange(0, T + 1/N, 1/N)

    dW_1 = np.array( [0] )
    dW_1 = np.concatenate(  (dW_1,  np.random.normal( 0, np.sqrt(1/N), N*T )) )

    dW_2 = np.array( [0] )
    dW_2 = np.concatenate(  (dW_2,  np.random.normal( 0, np.sqrt(1/N), N*T )) )

    W_1 = np.cumsum(dW_1)
    W_2 = np.cumsum(dW_2)

    X = np.array( [[1,0]] )

    for i in range( T*N ):
        value_1 = X[i,0] + ( alpha_1 * X[i,1] )*( t[i+1] - t[i] ) + (sigma_1)*(W_1[i+1] - W_1[i])
        value_2 = X[i,1] + ( -1 * alpha_2 * X[i,0] )*( t[i+1] - t[i] ) + (sigma_2)*( W_2[i+1] - W_2[i] )
        X = np.concatenate( (X, [[value_1, value_2]] ) )

    return X

if __name__ == '__main__':
    alpha_1 = 1
    alpha_2 = 1
    sigma_1 = 0.1
    sigma_2 = 0.1

    # time interval
    T = int( np.ceil(2*np.pi) )
    # number of times [0,1] is divided
    N = 50

    process_1 = random_walk_around_the_clock(N=N, T=T)
    process_2 = random_walk_around_the_clock(N=N, T=T)
    process_3 = random_walk_around_the_clock(N=N, T=T)
    process_4 = random_walk_around_the_clock(N=N, T=T)
    process_5 = random_walk_around_the_clock(N=N, T=T)

    fig=plt.figure()
    plt.title('Random Walk Around the Clock')
    l_1, = plt.plot( [], [], label='process_1' )
    l_2, = plt.plot( [], [], label='process_2' )
    l_3, = plt.plot( [], [], label='process_3' )
    l_4, = plt.plot( [], [], label='process_4' )
    l_5, = plt.plot( [], [], label='process_5' )
    plt.xlim( -2, 2 )
    plt.ylim( -2, 2 )
    plt.legend()
    metadata = dict( title='random_walk_around_the_clock', artist='me' )
    writer = PillowWriter(fps=(N*T+1), metadata=metadata)

    with writer.saving(fig, 'random_walk_around_the_clock.gif', 100):
        for i in range(N*T+1):
            l_1.set_data( process_1[0:i, 0], process_1[0:i, 1] )
            l_2.set_data( process_2[0:i, 0], process_2[0:i, 1] )
            l_3.set_data( process_3[0:i, 0], process_3[0:i, 1] )
            l_4.set_data( process_4[0:i, 0], process_4[0:i, 1] )
            l_5.set_data( process_5[0:i, 0], process_5[0:i, 1] )
            writer.grab_frame()


    # plt.plot( X[:,0], X[:,1] )
    # plt.show()