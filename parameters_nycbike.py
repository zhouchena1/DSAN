data_train = "./data/NYBike/bike_train.npz"
data_val = "./data/NYBike/bike_val.npz"
data_test = "./data/NYBike/bike_test.npz"
data_max = 295.0
t_max = 39.0
n_sec_int = 1800
n_int_day = 48
total_day = 90
n_int = total_day * 24 * 60 * 60 / n_sec_int
loss_threshold = 10
len_r = 14
len_c = 8