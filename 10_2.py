import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Межі інтегрування
a, b = 0, 2

# Визначення функції для інтегрування
def f(x):
    return x ** 2

def visualize_results(x_random, y_random, under_curve, a, b):
    # Створення діапазону значень для x
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = f(x)

    _, ax = plt.subplots()

    ax.plot(x, y, "r", linewidth=2)
    ax.scatter(x_random, y_random, color="blue", s=1)
    ax.scatter(x_random[under_curve], y_random[under_curve], color="red", s=1)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) від {a} до {b}")
    
    plt.grid()
    plt.show()

def monte_carlo(a, b, num_samples):
    # Максимальне значення функції на інтервалі [a, b]
    max_f = f(b)
    
    # Обчислення інтеграла методом Монте-Карло
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, max_f, num_samples)

    # Кількість точок під кривою
    under_curve = y_random < f(x_random)

    # Площа під кривою
    area_under_curve = (b - a) * max_f * np.sum(under_curve) / num_samples

    # Обчислення інтеграла за допомогою функції quad
    result, error = spi.quad(f, a, b)

    print(f'Площа обчислена методом Монте-Карло: {area_under_curve}')
    print(f'Площа обчислена функцією quad: {result}')
    print(f'Абсолютна похибка: {abs(area_under_curve - result)}')
    visualize_results(x_random, y_random, under_curve, a, b)

if __name__ == "__main__":
    for density in [100, 1000, 10000, 100000]:
        print(f"\nРезультати для кількості точок: {density}")
        monte_carlo(a, b, density)
