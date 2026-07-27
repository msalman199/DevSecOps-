import json
import re
from datetime import datetime
from collections import Counter

def analyze_security_logs(log_file='security.log'):
    """Analyze security logs for threats"""
    
    security_events = []
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                if 'SECURITY_EVENT' in line:
                    # Extract JSON part
                    json_match = re.search(r'SECURITY_EVENT: ({.*})', line)
                    if json_match:
                        try:
                            event_data = json.loads(json_match.group(1).replace("'", '"'))
                            security_events.append(event_data)
                        except json.JSONDecodeError:
                            continue
    except FileNotFoundError:
        print("No security log file found.")
        return
    
    if not security_events:
        print("No security events found in logs.")
        return
    
    print("=== Security Log Analysis ===")
    print(f"Total security events: {len(security_events)}")
    
    # Analyze event types
    event_types = Counter(event['event_type'] for event in security_events)
    print("\nEvent Types:")
    for event_type, count in event_types.items():
        print(f"  {event_type}: {count}")
    
    # Analyze IP addresses
    ip_addresses = Counter(event['ip_address'] for event in security_events)
    print("\nTop IP Addresses:")
    for ip, count in ip_addresses.most_common(5):
        print(f"  {ip}: {count}")
    
    # Recent events
    print("\nRecent Security Events:")
    for event in security_events[-5:]:
        print(f"  {event['timestamp']}: {event['event_type']} from {event['ip_address']}")

if __name__ == '__main__':
    analyze_security_logs()
