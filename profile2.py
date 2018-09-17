"""This is a trivial example of a gitrepo-based profile; The profile source code and other software, documentation, etc. are stored in in a publicly accessible GIT repository (say, github.com). When you instantiate this profile, the repository is cloned to all of the nodes in your experiment, to `/local/repository`. 
This particular profile is a simple example of using a single raw PC. It can be instantiated on any cluster; the node will boot the default operating system, which is typically a recent version of Ubuntu.
Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg


# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

#Establish number of nodes wanted
nodes=4
i=1

#Establish local network
link = request.LAN("Test")

while i<=nodes:
	# Add a VM to the request.
	node = request.XenVM("node-"+str(i))
	#Install CentOS7-STD
	node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
	
	#add public IP for first node
	if i=1:
		node.routable_control_ip = True
	
	#add interface
	iface = node.addInterface("if"+str(i))
	#add interface eth1, will be same for all nodes
	iface.component_id = "eth1"
	#set IP per VM
	iface.addAddress(rspec.IPv4Address("192.168.1."+str(i), "255.255.255.0")
	
	#Link nodes together
	link.addInterface(iface)
	
	# Install and execute a script that is contained in the repository.
	node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))
	
	#increment i for next node
	i+=1


# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)


#commands found at
#http://docs.cloudlab.us/
#https://groups.google.com/forum/#!forum/cloudlab-users
