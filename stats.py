
from collections import defaultdict

def generate_stats(packets):
    protocol_count = defaultdict(int)
    ip_count_src = defaultdict(int)
    ip_count_dst = defaultdict(int)

    for pkt in packets:
        try:
            if hasattr(pkt, 'ip'):
                src = pkt.ip.src
                dst = pkt.ip.dst
                ip_count_src[src] += 1
                ip_count_dst[dst] += 1

            if hasattr(pkt, 'highest_layer'):
                protocol_count[pkt.highest_layer] += 1
        except AttributeError:
            continue

    return {
        "Protocol Statistics": dict(protocol_count),
        "Top Source IPs": dict(sorted(ip_count_src.items(), key=lambda x: x[1], reverse=True)[:5]),
        "Top Destination IPs": dict(sorted(ip_count_dst.items(), key=lambda x: x[1], reverse=True)[:5]),
    }
