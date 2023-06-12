import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import PillowWriter
import scienceplots
plt.style.use([ 'notebook', 'grid','bright'])

np.random.seed(123)

def brownian_bridge( a_1=0, b_1=0, a_2=0, b_2=0, sigma_1=1, sigma_2=1,  T=1, N=10 ):
    # number of elements = 1 + T*N
    t = np.arange(0, T + 1/N, 1/N)

    dW_1 = np.array( [0] )
    dW_1 = np.concatenate(  (dW_1,  np.random.normal( 0, np.sqrt(1/N), N*T )) )

    dW_2 = np.array( [0] )
    dW_2 = np.concatenate(  (dW_2,  np.random.normal( 0, np.sqrt(1/N), N*T )) )

    W_1 = np.cumsum(dW_1)
    W_2 = np.cumsum(dW_2)

    X = np.array( [[a_1,a_2]] )

    for i in range( T*N ):
        value_1 = X[i,0] + ( b_1 - X[i,0] )/( T - t[i] )*( t[i+1] - t[i] ) + sigma_1*( W_1[i+1] - W_1[i] )
        value_2 = X[i,1] + ( b_2 - X[i,1] )/( T - t[i] )*( t[i+1] - t[i] ) + sigma_2*( W_2[i+1] - W_2[i] )
        X = np.concatenate( (X, [[value_1, value_2]] ) )

    return X

if __name__ == '__main__':
    # time interval
    T = 1
    # number of times [0,1] is divided
    N = 100

    process_1 = brownian_bridge(a_1=1, b_1=-1, a_2=-1, b_2=-1, sigma_1=0.1, sigma_2=0.1, N=N, T=T)
    process_2 = brownian_bridge(a_1=-1, b_1=-1, a_2=-1, b_2=1, sigma_1=0.1, sigma_2=0.1, N=N, T=T)
    process_3 = brownian_bridge(a_1=-1, b_1=1, a_2=1, b_2=1, sigma_1=0.1, sigma_2=0.1, N=N, T=T)
    process_4 = brownian_bridge(a_1=1, b_1=1, a_2=1, b_2=-1, sigma_1=0.1, sigma_2=0.1, N=N, T=T)

    fig=plt.figure()
    plt.title('Brownian Bridges')
    l_1, = plt.plot( [], [], label='process_1' )
    l_2, = plt.plot( [], [], label='process_2' )
    l_3, = plt.plot( [], [], label='process_3' )
    l_4, = plt.plot( [], [], label='process_4' )
    plt.xlim( -1.5, 1.5 )
    plt.ylim( -1.5, 1.5 )
    plt.legend()
    metadata = dict( title='brownian_bridge', artist='me' )
    writer = PillowWriter(fps=(N*T+1)*2, metadata=metadata)

    with writer.saving(fig, 'brownian_bridge.gif', 100):
        for i in range(N*T+1):
            l_1.set_data( process_1[0:i, 0], process_1[0:i, 1] )
            l_2.set_data( process_2[0:i, 0], process_2[0:i, 1] )
            l_3.set_data( process_3[0:i, 0], process_3[0:i, 1] )
            l_4.set_data( process_4[0:i, 0], process_4[0:i, 1] )
            writer.grab_frame()