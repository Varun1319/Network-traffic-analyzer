
from parser import parse_pcap
from stats import generate_stats
from visualize import visualize_stats

def main():
    file_path = input("Enter path to PCAP file: ").strip()

    # Filter options
    print("\n=== Optional Packet Filters ===")
    use_filters = input("Apply filters? (y/n): ").lower() == 'y'
    filters = {}

    if use_filters:
        ip = input("Filter by IP (leave blank to skip): ").strip()
        protocol = input("Filter by Protocol (TCP, UDP, HTTP, etc.): ").strip()
        port = input("Filter by Port (leave blank to skip): ").strip()

        if ip:
            filters['ip'] = ip
        if protocol:
            filters['protocol'] = protocol.upper()
        if port:
            filters['port'] = port

    print(f"\nReading: {file_path}")
    packets = parse_pcap(file_path, filters)

    if not packets:
        print("No packets found with given filters.")
        return

    stats = generate_stats(packets)

    for key, value in stats.items():
        print(f"\n{key}:")
        for subkey, subval in value.items():
            print(f"  {subkey}: {subval}")

    visualize_stats(stats)

if __name__ == "__main__":
    main()
