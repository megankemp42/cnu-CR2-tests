import matplotlib.pyplot as plt
import numpy as np


# Some input argument checking has been included in this model answer,
# please remember that this was not mandatory, and don't penalise
# if e.g. fig_type or plot_type wasn't checked for correctness.

# The test cases proposed here are also just examples, the amount
# shown here was not necessary. The important thing is that all the plots
# are created as instructed, and are clear to understand -- the actual data
# you choose to plot for the tests doesn't have to be particularly complicated,
# as long as a good plot is produced.

# Overall, this is only one of the possible ways to solve the problem.
# Other people may have chosen different layouts, or different ways to produce
# the plots altogether. This was a fairly complicated premise --
# judge each submission individually, trust your judgement,
# and stick to the marking scheme!


def plot_columns(fig_type, x, y, plot_type):
    '''
    Create and display a figure to plot x vs. y, column-wise.
    10 columns at most.

    Input:
    - x and y are 2D Numpy arrays.
    - fig_type is either "single" or "subplots", and indicates
        whether to plot everything on one graph or to make
        multiple subplots.
    - plot_type is a list of strings which are each either
        "line" (to produce a line plot) or "scatter" (for scatter plot).

    Output: returns None, but displays the final plot.
    '''
    # Find the number of plots we need
    plot_num = x.shape[1]

    if fig_type == "single":
        # we just need 1 set of axes
        ax_num = 1
    elif fig_type == "subplots":
        # we need as many axes as there are columns in e.g. x
        ax_num = plot_num
    else:
        # wrong input, we stop the function and ask for a better one
        print('Please specify a figure type as either "single" or "subplots".')
        return

    # Create the figure and axes -- we decide to align plots vertically.
    # Make sure the figure is big enough so we can see all the plots nicely.
    fig, ax = plt.subplots(ax_num, 1, figsize=(10, 5*ax_num))

    # We have at most 10 columns: prepare a list of 10 different markers
    markers = ['.', 'x', 's', '+', 'd', 'v', '^', '>', '<', 'p']

    # Create a loop to produce all the plots we need
    for i in range(plot_num):

        # Decide which axis we plot on, depending on how many we have in total
        if ax_num == 1:    # this is True either if fig_type is "single", or if
                           # it's "subplots" but there is only 1 column to plot.
            # We always plot in the same (the only) ax.
            current_ax = ax

        else:   # we have more than 1 ax
            # We plot in the ith element of the ax array
            current_ax = ax[i]

            # While we are here, let's set labels for each plot
            current_ax.set(title=f'Plot {i}', ylabel='y')

        # Create a random RGB colour to differentiate the plots
        col = np.random.random(3)

        # Decide what kind of plot we need for the ith plot
        if plot_type[i] == "line":
            # Make the ith plot: extract ith column of x and y
            current_ax.plot(x[:, i], y[:, i], label=f'Plot {i}', color=col)

        elif plot_type[i] == "scatter":
            # Make the ith plot a scatter plot
            current_ax.scatter(x[:, i], y[:, i], label=f'Plot {i}', color=col, marker=markers[i])
            # Alternatively:
            #  current_ax.plot(x[:, i], y[:, i], label=f'Plot {i}', color=col, linestyle='', marker=markers[i])

        else:
            # Wrong plot type: tell the user and stop
            print(f'Plot {i} has the type "{plot_type[i]}"; make sure it is either "line" or "scatter".')
            return

    # Now we should have all our plots!

    # If I have several subplots, I only want an x-axis label on the
    # bottom plot (which is current_ax after the loop is finished).
    # If I have only one, current_ax is that plot. So this will work for both fig_type choices.
    current_ax.set(xlabel='x')

    # If I just have 1 ax, I also need a title
    if ax_num == 1:
        current_ax.set(title="x vs. y, column-wise", ylabel='y')

        # If there are more than 1 plots, I need a legend
        if plot_num > 1:
            current_ax.legend()

    # If I have several subplots, adjust margins to make sure titles etc. are visible
    else:
        plt.subplots_adjust(left=0.08, right=0.97, bottom=0.08, top=0.93, hspace=0.3)

    # Finally: display the figure!
    plt.show()


# Tests: make a large array, then plot selected columns to run all the tests.
n_points = 80
n_plots = 8
xmin, xmax = -2, 2

x = np.zeros([n_points, n_plots])
for i in range(n_plots):
    x[:, i] = np.linspace(xmin, xmax, n_points)

y = np.zeros_like(x)

# Make some data!

# Cosine and sine
y[:, 0] = np.cos(4 * x[:, 0])
y[:, 1] = np.sin(7 * x[:, 1])

# Noisy cosine and sine (both x and y noisy)
noise_1 = 0.1
noise_2 = 0.02
y[:, 2] = np.cos(4 * (x[:, 2] + noise_1 * np.random.randn(n_points))) + noise_1 * np.random.randn(n_points)
y[:, 3] = np.sin(7 * (x[:, 3] + noise_2 * np.random.randn(n_points))) + noise_2 * np.random.randn(n_points)

# Polynomial of deg. 2 and 5
coeffs_2 = 0.02 * (2 * np.random.random(3) - 1)
coeffs_5 = 0.005 * (2 * np.random.random(6) - 1)
y[:, 4] = np.polyval(coeffs_2, x[:, 4])
y[:, 5] = np.polyval(coeffs_5, x[:, 5])

# Polynomial with some noise
y[:, 6] = np.polyval(coeffs_2, x[:, 6] + noise_1 * np.random.randn(n_points))
y[:, 7] = np.polyval(coeffs_5, x[:, 7] + noise_2 * np.random.randn(n_points))


# Uncomment each test to see the figure. Check that the plots
# match the input parameter values.

# All plots
# (some of these will look messy!)
#  plot_columns("single", x, y, ["line", "line", "scatter", "scatter", "line", "line", "scatter", "scatter"])
#  plot_columns("subplots", x, y, ["line", "line", "scatter", "scatter", "line", "line", "scatter", "scatter"])
#  plot_columns("single", x, y, ["line"] * n_plots)
#  plot_columns("single", x, y, ["scatter"] * n_plots)
#  plot_columns("subplots", x, y, ["line"] * n_plots)
#  plot_columns("subplots", x, y, ["scatter"] * n_plots)

# Clean and noisy data together
# plot_columns("single", x[:, [0, 2]], y[:, [0, 2]], ["line", "scatter"])
# plot_columns("single", x[:, [1, 3]], y[:, [1, 3]], ["line", "scatter"])
# plot_columns("single", x[:, [4, 6]], y[:, [4, 6]], ["line", "scatter"])
# plot_columns("single", x[:, [5, 7]], y[:, [5, 7]], ["line", "scatter"])
#  plot_columns("single", x[:, :4], y[:, :4], ["line", "line", "scatter", "scatter"])
#  plot_columns("single", x[:, 4:], y[:, 4:], ["line", "line", "scatter", "scatter"])

# plot_columns("subplots", x[:, [0, 2]], y[:, [0, 2]], ["line", "scatter"])
# plot_columns("subplots", x[:, [1, 3]], y[:, [1, 3]], ["line", "scatter"])

# Single column
#  plot_columns("single", x[:, [3]], y[:, [3]], ["line"])
#  plot_columns("single", x[:, [3]], y[:, [3]], ["scatter"])
#  plot_columns("subplots", x[:, [3]], y[:, [3]], ["line"])
#  plot_columns("subplots", x[:, [3]], y[:, [3]], ["scatter"])
