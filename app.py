
from flask import Flask, render_template

app = Flask(__name__)

# ==========================
# Single VLAN Project Data
# ==========================
vlan_project = {
    "name": "VLAN and Inter-VLAN Routing Lab",
    "image": "vlan_lab.png",  # file in static/images/
    "summary": "Configured multiple VLANs on a switch and enabled inter-VLAN routing using a router-on-a-stick topology.",
    "config_explanation": """Lab overview:
- Goal: Separate departments into different VLANs and allow communication between them using a router-on-a-stick design.

Key configuration steps (example):

1) On the switch: create VLANs
Switch(config)# vlan 10
Switch(config-vlan)# name SALES
Switch(config)# vlan 20
Switch(config-vlan)# name IT

2) Assign switch ports to VLANs
Switch(config)# interface range fa0/1 - 5
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 10

Switch(config)# interface range fa0/6 - 10
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 20

3) Configure trunk link to the router
Switch(config)# interface fa0/24
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk encapsulation dot1q  ! (if required on your platform)

4) On the router: create subinterfaces for each VLAN
Router(config)# interface g0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0

Router(config)# interface g0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.20.1 255.255.255.0

5) Enable the physical interface
Router(config)# interface g0/0
Router(config-if)# no shutdown

6) Test connectivity
- PCs in VLAN 10 should ping 192.168.10.1
- PCs in VLAN 20 should ping 192.168.20.1
- PCs in VLAN 10 and VLAN 20 should ping each other (inter-VLAN routing working)."""
}


@app.route('/')
def home():
    # Pass ONLY the VLAN project to the template
    return render_template('index.html', project=vlan_project)


if __name__ == '__main__':
    # You are already using: python -m flask run (which is fine)
    app.run(debug=True)
