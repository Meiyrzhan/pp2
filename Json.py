import json

# Load the JSON data
with open("sample-data.json", "r") as file:
    data = json.load(file)

# Print the header
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU'}")
print("-" * 80)

# Extract and print the required attributes
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "")  # Default to empty if missing
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu}")
