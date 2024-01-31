from numpy import *
import matplotlib.pyplot as plt


def calculate_complex_squared_magnitude(file_path):
    results = []

    # Open the file and read each line
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) == 3:
                real_part = float(columns[1])
                imag_part = float(columns[2][:-1])  # Remove the 'i' at the end
                complex_number = complex(real_part, imag_part)
                # Calculate the squared magnitude and append to the list
                z_z = complex_squared_magnitude(complex_number.real, complex_number.imag)
                results.append(z_z)
            else:
                value = float(columns[0])
                value_squared = squared_value(value)
                results.append(value_squared)
    return results


def complex_squared_magnitude(a, b):
    # z*z = sqrt(a**2+b**2)
    result_real = a ** 2 + b ** 2
    result = sqrt(result_real)
    return result


def squared_value(a):
    aa = a ** 2
    return aa


def x_values_(file):
    x_vals = []
    with open(file, 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) == 1:
                val = float(columns[0])
                x_vals.append(val)
    return x_vals


def sum_magnitude(lumo, lumo_1, lumo_2):
    sum_list = []
    for i in range(len(lumo)):
        sumall = lumo[i] + lumo_1[i] + lumo_2[i]
        sum_list.append(sumall)
    return sum_list




file1 = 'homo'
file2 = 'lumo'
file3 = 'lumo+1'
file4 = 'lumo+2'
homo = calculate_complex_squared_magnitude(file1)
lumo = calculate_complex_squared_magnitude(file2)
lumo1 = calculate_complex_squared_magnitude(file3)
lumo2 = calculate_complex_squared_magnitude(file4)

magnitude = sum_magnitude(lumo, lumo1, lumo2)

print(lumo)
print(len(homo))
print(len(lumo))
print(len(lumo1))
print(len(lumo2))


x_values = x_values_('x_values')
plt.plot(x_values, homo)
plt.plot(x_values, lumo)
plt.plot(x_values, lumo1)
plt.plot(x_values, lumo2)
plt.plot(x_values, magnitude)
# plt.ylim(0.9999998, 1.0000005)
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.3f'))
plt.gca().set_ylim(-0.1, 1.15)  # Set y-axis limits on the current axis

plt.xlabel('pt charge distance along z-axis(Angstroms')
plt.ylabel('Weight')
plt.title('H$_2$ Stationary Approximation Canonical Orbitals Plots')  # , LUMO, LUMO+1, LUMO+2))
plt.legend([r'|<ψ(0)$_{homo}$|ψ(d)$_{homo}$>|$^2$', r'|<ψ(0)$_{homo}$|ψ(d)$_{lumo}$>|$^2$',
            r'|<ψ(0)$_{homo}$|ψ(d)$_{lumo+1}$>|$^2$', r'|<ψ(0)$_{homo}$|ψ(d)$_{lumo+2}$>|$^2$',
            r'sum'
            ])
plt.show()
