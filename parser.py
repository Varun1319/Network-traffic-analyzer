
import pyshark

def parse_pcap(file_path, filters=None):
    """
    Parse a PCAP file with optional filtering.

    filters: dict with optional keys:
        - 'ip': str (source or destination IP)
        - 'protocol': str (e.g., 'TCP', 'UDP', 'HTTP')
        - 'port': str or int (source or destination port)
    """
    capture_filters = []

    if filters:
        if 'ip' in filters:
            capture_filters.append(f"ip.addr == {filters['ip']}")
        if 'protocol' in filters:
            capture_filters.append(f"{filters['protocol'].lower()}")
        if 'port' in filters:
            capture_filters.append(f"tcp.port == {filters['port']} or udp.port == {filters['port']}")

    display_filter = ' and '.join(capture_filters) if capture_filters else None

    try:
        cap = pyshark.FileCapture(
            file_path,
            display_filter=display_filter,
            use_json=True
        )
        return list(cap)
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
