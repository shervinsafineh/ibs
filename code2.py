import math
import random


def dbm2w(l):
    return 10**((l-30)/10)


def snr_abs2snr_db(o):
    print("o value is " + str(o), "\n")
    # if o > 0:
    return 10*math.log10(o)
    # else:
    # return -1000


def snr(bandwidth, p_tx_dbm, d_angle, frequency, distance, fi=random.uniform(0, 2 * math.pi)):
    p_tx = dbm2w(p_tx_dbm)
    d_angle_rad = math.radians(d_angle)
    g_rx = 1
    c = 3*(10**8)
    k_b = 1.38*(10**(-23))
    t = 293
    noise = k_b*t*bandwidth


    if 2*math.pi-(d_angle_rad/2) <= fi <= 2*math.pi:
        g_tx = 2/(1-(math.cos((d_angle_rad/2))))
    else:
        g_tx = 0

    pl = (4*math.pi*distance*frequency/c)**2
    p_rx = p_tx*g_tx*g_rx*(1/pl)
    snr_abs = p_rx/noise
    snr_db = snr_abs2snr_db(snr_abs)
    return fi, snr_db, d_angle_rad


def fi_gen():
    snr_t = 0
    steps = 0

    fi, snr_db, d_angle_rad = snr(10**9, 0, 5, 3000, 10)
    while snr_db <= snr_t:

        fi = fi + d_angle_rad
        steps = steps + 1
        print("\n\n")
        print("steps = " + str(steps))
        print("fi = " + str(fi))
        fi, snr_db, d_angle_rad = snr(10**9, 0, 5, 3000, 10, fi)
        print("d_angle_rad = " + str(d_angle_rad))

    return fi, steps


fi_gen()
