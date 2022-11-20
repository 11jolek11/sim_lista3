from numpy.random import default_rng
import sys

def mm1(arrival_rate, service_rate, n, seed = 1234567):
    rng = default_rng(seed)
    arrive = depart = 0.0
    mean_interarrival_time = 1.0 / arrival_rate
    mean_service_time = 1.0 / service_rate
    print("customer_number,delay_in_queue")
    for customer in range(1, n + 1):
        arrive += rng.poisson(mean_interarrival_time)
        start = max(arrive, depart)
        depart = start + rng.exponential(mean_service_time)
        print("%d,%f" % (customer, start - arrive))

if __name__ == '__main__':
    if len(sys.argv) == 4:
        mm1(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
    else:
        m1 = "Please specify arrival rate, per-server service rate, and"
        m2 = "# customers separated by spaces on the command-line."
        m3 = "Example: python %s 0.95 1.0 20" % sys.argv[0]
        print("\n\t" + m1, file = sys.stderr)
        print("\t" + m2 + "\n", file = sys.stderr)
        print("\t" + m3 + "\n", file = sys.stderr)