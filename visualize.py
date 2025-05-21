
import matplotlib.pyplot as plt

def visualize_stats(stats):
    protocols = stats.get("Protocol Statistics", {})
    if not protocols:
        print("No protocol data to visualize.")
        return

    labels = list(protocols.keys())
    sizes = list(protocols.values())

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Protocol Distribution")
    plt.axis("equal")
    plt.show()
