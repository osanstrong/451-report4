import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

T = 180 # 180 seconds for every measurement

vac_dist = [1, 17, 25, 33, 49] #mm
vac_x = [895.1, 856.94, 815.68, 792.3, 666.6]
vac_I = [g/T for g in [
    2.824395e6, 
    8.399e5, # or 8.522e5
    3.405e5,
    2.709e5,
    1.272e5,
]]

E = 5486 #keV
C = E / vac_x[0] # E corresponding to each bin

A = 450 #mm²
PI = np.pi
a = 2*np.sqrt(A / PI) # mm
def sangle(d):
    return (2*PI*(1 - d/(np.hypot(d, a))))
# print([sangle(d) for d in vac_dist])
def norm(I, d):
    return 4*PI*I / sangle(d)
    # return I
norm_I = [4*PI*vac_I[i]/sangle(vac_dist[i]) for i in range(len(vac_dist))]

# plt.scatter(vac_dist, vac_I, label="In vacuum")
# plt.scatter(vac_dist, norm_I, label="In vacuum, normalized by solid angle")
# plt.xlabel("Distance (mm)")
# # plt.ylabel("Integrated peak intensity (counts)")
# plt.ylabel("Peak intensity (counts per second)")
# plt.legend()
# plt.show()


air_dist = [1, 17, 25, 33, 49] #mm
air_I = [g/T for g in [
    2.841e6,
    8.546e5,
    3.44e5,
    2.72e5,
    1
]]
air_x = [x*C for x in [
    865.58,
    661.38,
    438.20,
    331.65,
]]
air_FWHM = [f*C for f in [
    22.22,
    60.39,
    55.56,
    58.84,
]]

# plt.scatter(air_dist, air_I, label="In air")
# plt.scatter(air_dist, [norm(air_I[i], air_dist[i]) for i in range(5)], label="In air, normalized by solid angle")
# plt.xlabel("Distance (mm)")
# # plt.ylabel("Integrated peak intensity (counts)")
# plt.ylabel("Peak intensity (counts per second)")
# plt.legend()
# plt.show()

# plt.scatter(air_dist[:4], air_x, label="In air")
# plt.xlabel("Distance (mm)")
# plt.ylabel("Peak Energy (keV)")
# plt.legend()
# plt.show()
# plt.scatter(air_dist[:4], air_FWHM, label="In air")
# plt.xlabel("Distance (mm)")
# plt.ylabel("Peak FWHM (keV)")
# plt.legend()
# plt.show()

al_thickness = 18 #microns
al_dist = [al_thickness * n for n in range(1,6)]
al_dat = [
    [610.5, 60.19, 3195, 2542], # I in rates this time
    [293.68, 116.28, 2146, 1112],
    [8.51, 2.61, 58, 7],
    [8.77, 1.85, 17, 10],
    [24, 1, 0.15, 0]
]
al_x = [d[0]*C for d in al_dat]
al_f = [d[1]*C for d in al_dat]
al_i = [d[2] for d in al_dat] # For now using gross

# plt.scatter(al_dist, al_x, label="Aluminum")
# plt.xlabel("Thickness of material (microns)")
# plt.ylabel("Peak location (keV)")
# plt.legend()
# plt.show()

# plt.scatter(al_dist, al_f, label="Aluminum")
# plt.xlabel("Thickness of material (microns)")
# plt.ylabel("Peak FWHM (keV)")
# plt.legend()
# plt.show()

# plt.scatter(al_dist, al_i, label="Aluminum")
# plt.xlabel("Thickness of material (microns)")
# plt.ylabel("Peak intensity (counts per second)")
# plt.legend()
# plt.show()

#### Mylar ####
my_thickness = 3.6 #microns
my_dist = [my_thickness * n for n in range(1,6)]
my_dat = [
    [758.58, 26.58, 3328, 2973],
    [673, 38.62, 3308, 2701],
    [491, 46.84, 1114, 833], # 3 left peak
    # [589.7, 55.46, 441, 330], # 3 right peak
    [512.82, 57.72, 1791, 1199],
    [434.42, 65.60, 2715, 1771]
]
my_x = [d[0] for d in my_dat]
my_f = [d[1]*C for d in my_dat]
my_i = [d[2]*C for d in my_dat] # For now using gross

# plt.scatter(my_dist, my_x, label="Mylar")
# plt.xlabel("Thickness of material (microns)")
# plt.ylabel("Peak location (keV)")
# plt.legend()
# plt.show()

# plt.scatter(my_dist, my_f, label="Mylar")
# plt.xlabel("Thickness of material (microns)")
# plt.ylabel("Peak FWHM (keV)")
# plt.legend()
# plt.show()

# plt.scatter(my_dist, my_i, label="Mylar")
# plt.xlabel("Thickness of material (microns)")
# plt.ylabel("Peak intensity (counts per second)")
# plt.legend()
# plt.show()


#### Get peak energy of simulated transmissions

# Import and test
def get_spectrum(fpath):
    df = pd.read_csv(fpath, sep="\t", skiprows=12)