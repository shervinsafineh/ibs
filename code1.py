import math
import matplotlib.pyplot as plt
import numpy


def dbm2w(l):
    return 10**((l-30)/10)


def snr_abs2snr_db(o):
    return 10*math.log10(o)


def snr(bandwidth, p_tx_dbm, d_angle, frequency, distances):
    p_tx = dbm2w(p_tx_dbm)
    d_angle_rad = math.radians(d_angle)
    g_tx = 2/(1-(math.cos((d_angle_rad/2))))
    g_rx = 1
    c = 3*(10**8)
    k_b = 1.38*(10**(-23))
    t = 293
    noise = k_b*t*bandwidth
    snr_db_list = []
    snr_abs_list = []

    for x in range(len(distances)):

        pl = (4*math.pi*distances[x]*frequency/c)**2
        p_rx = p_tx*g_tx*g_rx*(1/pl)
        snr_abs = p_rx/noise
        snr_abs_list.append(snr_abs)
        snr_db = snr_abs2snr_db(snr_abs)
        snr_db_list.append(snr_db)

    print('Distances:', distances)
    print('SNRs (dB):', snr_db_list)
    print('SNRs (abs):', snr_abs_list)
    return distances, snr_db_list, snr_abs_list


def plot_dist_vs_snr_db():
    distances1, snr_db_list1, snr_abs_list1 = snr(10 ** 9, 0, 5, 3000, numpy.arange(1, 10, 0.1))
    distances2, snr_db_list2, snr_abs_list2 = snr(10 ** 9, 0, 10, 3000, numpy.arange(1, 10, 0.1))
    distances3, snr_db_list3, snr_abs_list3 = snr(10 ** 9, 0, 45, 3000, numpy.arange(1, 10, 0.1))
    plt.figure(1)
    plt.plot(distances1, snr_db_list1, 'b-', label='5 Degrees')
    plt.plot(distances2, snr_db_list2, 'r--', label='10 Degrees')
    plt.plot(distances3, snr_db_list3, 'g:', label='45 Degrees')
    plt.xlabel('Distance (m)')
    plt.ylabel('SNR (dB)')
    plt.legend(loc='best')
    plt.savefig('Distance_vs_SNR-dB.pdf')
    plt.show()


def plot_dist_vs_snr_abs():
    distances1, snr_db_list1, snr_abs_list1 = snr(10 ** 9, 0, 5, 3000, numpy.arange(1, 10, 0.1))
    distances2, snr_db_list2, snr_abs_list2 = snr(10 ** 9, 0, 10, 3000, numpy.arange(1, 10, 0.1))
    distances3, snr_db_list3, snr_abs_list3 = snr(10 ** 9, 0, 45, 3000, numpy.arange(1, 10, 0.1))
    plt.figure(2)
    plt.plot(distances1, snr_abs_list1, 'b-', label='5 Degrees')
    plt.plot(distances2, snr_abs_list2, 'r--', label='10 Degrees')
    plt.plot(distances3, snr_abs_list3, 'g:', label='45 Degrees')
    plt.xlabel('Distance (m)')
    plt.ylabel('SNR (abs)')
    plt.legend(loc='best')
    plt.savefig('Distance_vs_SNR-abs.pdf')
    plt.show()


snr(10**9, 0, 5, 3000, numpy.arange(1, 10, 0.1))
plot_dist_vs_snr_db()
plot_dist_vs_snr_abs()
