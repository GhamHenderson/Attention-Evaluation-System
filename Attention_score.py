import time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def attention_score(iris, blinks, yawns, off_screen, name):
    now = datetime.now()
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

    filename = now.strftime("reports/average_info_%m-%d_%H.png")
    plt.savefig(filename, dpi=100)
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

    filename = now.strftime("reports/yawns_blinks_%m-%d_%H.png")
    plt.savefig(filename, dpi=100)
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

    now = datetime.now()
    filename = now.strftime("reports/summary_%m-%d_%H.png")
    plt.savefig(filename, dpi=100)
    plt.show()

    import tkinter as tk

    # Create a new Tkinter window
    window = tk.Tk()

    # Set the size of the window
    window.geometry("600x300")

    # Create a frame for the text label
    text_frame = tk.Frame(window, padx=10, pady=10, bd=1, relief="solid")
    text_frame.pack(side="top", fill="both", expand=True)

    # Add a label with some Lorem Ipsum text
    text = "Thank you for Using The Attention Evaluation System. \n" \
           "Please take note that the score is an estimated value based on physical traits. \n" \
           "Results are based on estimates therefore it is not 100% accurate. \n" \
           "Check Score Below and In the Reports Folder for more detailed information."

    text_label = tk.Label(text_frame, text=text, justify="left", wraplength=500, font=("Arial", 10))
    text_label.pack(expand=True)

    # Create a frame for the statistics
    stats_frame = tk.Frame(window, padx=10, pady=10, bd=1, relief="solid")
    stats_frame.pack(side="top", fill="both", expand=True)

    # Add a title to the statistics frame
    title_label = tk.Label(stats_frame, text="Session Statistics", font=("Arial", 16))
    title_label.pack(side="top", pady=10)

    # Create labels for each output
    blinks_label = tk.Label(stats_frame, text="Average Blinks: " + str(average_blinks))
    total_blinks_label = tk.Label(stats_frame, text="Total Blinks in Session: " + str(total_blinks))
    yawns_label = tk.Label(stats_frame, text="Average Yawns: " + str(average_yawns))
    total_yawns_label = tk.Label(stats_frame, text="Total Yawns in session: " + str(total_yawns))
    offscreen_label = tk.Label(stats_frame, text="Average OffScreen: " + str(average_offscreen))
    total_offscreen_label = tk.Label(stats_frame, text="Total OffScreen in session: " + str(total_offscreen))

    # Pack the labels into the statistics frame
    blinks_label.pack()
    total_blinks_label.pack()
    yawns_label.pack()
    total_yawns_label.pack()
    offscreen_label.pack()
    total_offscreen_label.pack()

    # Create a frame for the attention score
    score_frame = tk.Frame(window, padx=10, pady=10, bd=1, relief="solid")
    score_frame.pack(side="bottom", fill="x", padx=10, pady=10)

    # Add a label for the attention score title
    score_title_label = tk.Label(score_frame, text="Attention Score", font=("Arial", 16))
    score_title_label.pack(side="top", pady=10)

    # Add a label for the attention score
    attention_score_label = tk.Label(score_frame, text="86 / 100", font=("Arial", 24))
    attention_score_label.pack(expand=True)

    # Start the Tkinter event loop
    window.mainloop()
