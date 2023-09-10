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
    sigma_1 = 0.5
    sigma_2 = 0.5

    # time interval
    T = int( np.ceil(2*np.pi) )
    # number of times [0,1] is divided
    N = 5000

    path_1 = random_walk_around_the_clock(alpha_1=alpha_1, alpha_2=alpha_2, sigma_1=sigma_1, sigma_2=sigma_2, T=T, N=N)
    path_2 = random_walk_around_the_clock(alpha_1=alpha_1, alpha_2=alpha_2, sigma_1=sigma_1, sigma_2=sigma_2, T=T, N=N)
    path_3 = random_walk_around_the_clock(alpha_1=alpha_1, alpha_2=alpha_2, sigma_1=sigma_1, sigma_2=sigma_2, T=T, N=N)
    path_4 = random_walk_around_the_clock(alpha_1=alpha_1, alpha_2=alpha_2, sigma_1=sigma_1, sigma_2=sigma_2, T=T, N=N)
    path_5 = random_walk_around_the_clock(alpha_1=alpha_1, alpha_2=alpha_2, sigma_1=sigma_1, sigma_2=sigma_2, T=T, N=N)

    # plt.xlim( -2, 2 )
    # plt.ylim( -2, 2 )
    plt.title('Random Walk Around the Clock')
    plt.plot(path_1[:,0], path_1[:,1], linewidth=1, label='path_1')
    plt.plot(path_2[:,0], path_2[:,1], linewidth=1, label='path_2')
    plt.plot(path_3[:,0], path_3[:,1], linewidth=1, label='path_3')
    plt.plot(path_4[:,0], path_4[:,1], linewidth=1, label='path_4')
    plt.plot(path_5[:,0], path_5[:,1], linewidth=1, label='path_5')
#     plt.legend()
    plt.savefig('random_walk_around_the_clock.png')
    plt.show()

    # fig=plt.figure()
    # plt.title('Random Walk Around the Clock')
    # l_1, = plt.plot( [], [], label='process_1' )
    # l_2, = plt.plot( [], [], label='process_2' )
    # l_3, = plt.plot( [], [], label='process_3' )
    # l_4, = plt.plot( [], [], label='process_4' )
    # l_5, = plt.plot( [], [], label='process_5' )
    # plt.xlim( -2, 2 )
    # plt.ylim( -2, 2 )
    # plt.legend()
    # metadata = dict( title='random_walk_around_the_clock', artist='me' )
    # writer = PillowWriter(fps=(N*T+1), metadata=metadata)

    # with writer.saving(fig, 'random_walk_around_the_clock.gif', 100):
    #     for i in range(N*T+1):
    #         l_1.set_data( path_1[0:i, 0], path_1[0:i, 1] )
    #         l_2.set_data( path_2[0:i, 0], path_2[0:i, 1] )
    #         l_3.set_data( path_3[0:i, 0], path_3[0:i, 1] )
    #         l_4.set_data( path_4[0:i, 0], path_4[0:i, 1] )
    #         l_5.set_data( path_5[0:i, 0], path_5[0:i, 1] )
    #         writer.grab_frame()