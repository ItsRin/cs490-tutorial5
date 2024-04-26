import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('loki-bot-analysis.csv')

# Histogram for the 'payload' column
plt.figure(figsize=(10, 6))
plt.hist(data['payload'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Payload Sizes')
plt.xlabel('Payload Size')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 2D Histogram for the 'payload' against itself
plt.figure(figsize=(8, 6))
plt.hist2d(data['payload'], data['payload'], bins=(50, 50), cmap=plt.cm.BuPu)
plt.colorbar()
plt.title('2D Histogram of Payload vs. Payload')
plt.xlabel('Payload Size')
plt.ylabel('Payload Size')
plt.grid(True)
plt.show()

# Scatter plots for 'payload' vs each categorical column
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# 'payload' vs 'source'
axs[0].scatter(data['source'], data['payload'], alpha=0.5)
axs[0].set_title('Payload vs. Source')
axs[0].set_xlabel('Source')
axs[0].set_ylabel('Payload')
axs[0].tick_params(labelrotation=90)

# 'payload' vs 'destination'
axs[1].scatter(data['destination'], data['payload'], alpha=0.5, color='red')
axs[1].set_title('Payload vs. Destination')
axs[1].set_xlabel('Destination')
axs[1].tick_params(labelrotation=90)

# 'payload' vs 'protocol'
axs[2].scatter(data['protocol'], data['payload'], alpha=0.5, color='green')
axs[2].set_title('Payload vs. Protocol')
axs[2].set_xlabel('Protocol')

plt.tight_layout()
plt.show()
