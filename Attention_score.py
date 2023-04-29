import matplotlib.pyplot as plt
import numpy as np


def attention_score(iris, blinks, yawns, off_screen, name):
    total_blinks = 0
    for b in blinks:
        total_blinks = b + total_blinks
    average_blinks = total_blinks / len(blinks)

    total_yawns = 0
    for y in yawns:
        total_yawns = y + total_yawns
    average_yawns = total_yawns / len(yawns)

    total_offscreen = 0
    for o in off_screen:
        total_offscreen = o + total_offscreen
    average_offscreen = total_offscreen / len(off_screen)

    print("\n")
    if name != "":
        print("User : " + str(name))
    else:
        print("User : Not Specified")

    print("Average Blinks : " + str(average_blinks))
    print("Total Blinks Over Session : " + str(total_blinks))

    print("Average Yawns : " + str(average_yawns))
    print("Total Yawns  : " + str(total_yawns))

    print("Average OffScreen : " + str(average_offscreen))
    print("Total OffScreen  : " + str(total_offscreen))

    # Create the x-axis labels (e.g., "Minute 1", "Minute 2", ...)
    x_labels = [f"{i + 1}" for i in range(len(blinks))]
    # Create a line chart for the blinks per minute
    plt.plot(x_labels, blinks, marker='o', label="BPM")
    # Create a horizontal line for the average blinks per minute
    plt.axhline(y=average_blinks, color='r', linestyle='--', label="Average Blinks")

    # Set chart title and labels
    plt.title("Blinks per Minute vs. Average Blinks")
    plt.xlabel("Minute")
    plt.ylabel("Blinks in a minute")

    # Add a legend
    plt.legend()
    # Show the chart
    plt.show()

    # Set the data and labels for the bar chart
    data = [total_yawns, total_blinks]
    labels = ['Yawns', 'Blinks']
    # Create the bar chart
    plt.bar(labels, data)

    # Set chart title and labels
    plt.title("Yawns vs. Blinks")
    plt.xlabel("Categories")
    plt.ylabel("Count")

    # Show the chart
    plt.show()

    x = range(len(blinks))
    average_blinks = np.mean(blinks)
    average_yawns = np.mean(yawns)
    average_offscreen = np.mean(off_screen)

    fig, ax = plt.subplots()
    ax.plot(x, blinks, label='Blinks', color='red')
    ax.plot(x, yawns, label='Yawns', color='green')
    ax.plot(x, off_screen, label='Off-Screen', color='blue')

    ax.axhline(y=average_blinks, label='Average Blinks', color='red', alpha=0.5, linestyle='--')
    ax.axhline(y=average_yawns, label='Average Yawns', color='green', alpha=0.5, linestyle='--')
    ax.axhline(y=average_offscreen, label='Average Off-Screen', color='blue', alpha=0.5, linestyle='--')

    ax.legend()
    ax.set_xlabel('Time (in minutes)')
    ax.set_ylabel('Value')

    plt.show()
