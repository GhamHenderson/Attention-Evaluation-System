import matplotlib.pyplot as plt


def attention_score(iris, blinks, yawn_total, name):
    total_blinks = 0
    for b in blinks:
        total_blinks = b + total_blinks
    average_blinks = total_blinks / len(blinks)

    print("\n")
    if name != "":
        print("User : " + str(name))
    else:
        print("User : Not Specified")

    print("Average Blinks : " + str(average_blinks))
    print("Total Blinks Over Session : " + str(total_blinks))
    print("Iris Info : " + str(iris))
    print("Total Yawns  : " + str(yawn_total))

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
    data = [yawn_total, total_blinks]
    labels = ['Yawns', 'Blinks']
    # Create the bar chart
    plt.bar(labels, data)

    # Set chart title and labels
    plt.title("Yawns vs. Blinks")
    plt.xlabel("Categories")
    plt.ylabel("Count")

    # Show the chart
    plt.show()
