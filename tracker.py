import matplotlib.pyplot as plt
import numpy as np
from pyscript import display
from js import document

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
absences = np.array([1, 0, 7, 4, 9])

def plot_graph():
    plt.clf()
    fig, ax = plt.subplots(figsize=(6, 4))
    
    ax.plot(days, absences, marker='o', color='#9b111e', linewidth=3, 
            markersize=10, markerfacecolor='#9b111e', markeredgecolor='white')
    
    ax.fill_between(days, absences, color='#9b111e', alpha=0.1)
    
    ax.set_title('Weekly Attendance Overview', fontsize=12, fontweight='bold', color='#9b111e')
    ax.set_ylabel('Absences', fontweight='bold', color='#636e72')
    ax.grid(True, linestyle='--', alpha=0.3)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    display(fig, target="mpl-output", append=False)

def update_data(event):
    day_idx = int(document.getElementById("day").value)
    raw_val = int(document.getElementById("absence").value)
    
    val = max(0, raw_val)
    document.getElementById("absence").value = str(val)
    
    absences[day_idx] = val
    plot_graph()

plot_graph()