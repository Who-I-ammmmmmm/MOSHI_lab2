import numpy as np
import matplotlib.pyplot as plt

def test_function(x):
    return x**2

def main_function(x):
    return np.exp(x) * 2

def exact_integral(func, a, b):
    x = np.linspace(a, b, 1000)
    y = func(x)
    integral = np.trapz(y, x)
    return integral

def generate_random_point(a, b):
    x = np.random.uniform(a, b)
    y = np.random.uniform(0, 1) 
    return x, y

def evaluate_function(func, x):
    return func(x)

def monte_carlo_integration(func, a, b, num_samples=10000):
    total_area = 0
    for _ in range(num_samples):
        x, y = generate_random_point(a, b)
        total_area += y * (b - a)  
    return total_area / num_samples

def visualize(func, a, b, num_samples=10000):
    x = np.linspace(a, b, 1000)
    y = func(x)

    plt.plot(x, y, 'r-', label='Function')

    random_x = np.random.uniform(a, b, num_samples)
    random_y = func(random_x)

    plt.scatter(random_x, random_y, color='blue', alpha=0.5, label='Random Samples')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Monte Carlo Integration')
    plt.show()

if __name__ == "__main__":
    a, b = 0, 1 
    num_samples = 10000 

    exact_integral_test = exact_integral(test_function, a, b)
    estimated_integral_test = monte_carlo_integration(test_function, a, b, num_samples)
    print("Exact Integral (Test):", exact_integral_test)
    print("Estimated Integral (Test):", estimated_integral_test)

    exact_integral_main = exact_integral(main_function, a, b)
    estimated_integral_main = monte_carlo_integration(main_function, a, b, num_samples)
    print("Exact Integral (Main):", exact_integral_main)
    print("Estimated Integral (Main):", estimated_integral_main)

    absolute_error_test = abs(exact_integral_test - estimated_integral_test)
    relative_error_test = absolute_error_test / exact_integral_test
    print("Absolute Error (Test):", absolute_error_test)
    print("Relative Error (Test):", relative_error_test)

    absolute_error_main = abs(exact_integral_main - estimated_integral_main)
    relative_error_main = absolute_error_main / exact_integral_main
    print("Absolute Error (Main):", absolute_error_main)
    print("Relative Error (Main):", relative_error_main)

    visualize(test_function, a, b)
