"""
Assignment 2 - Custom Topology using Mininet
Name : Adhish Singla
Roll Number : 201403004
"""

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def Topology():
    """
    Custom Topology
    Every switch is connected to the next switch.
    Every switch has equal number of hosts connected to it.
    Even Hosts can ping only Even Hosts and Odd Hosts can ping only Odd Hosts.
    """
    num_switches = int(raw_input("Enter Number of switches: "))
    num_hosts = int(raw_input("Enter Number of hosts per switch: "))
    
    net = Mininet( controller=Controller ,  link=TCLink)

    info( '*** Adding controller\n' )
    net.addController( 'c0' )
    
    info( '*** Adding hosts\n' )
    
    switches = []
    count=1

    ip1='10.0.1.'
    ip2='10.0.2.'

    for i in range(num_switches):
        switch = net.addSwitch('s'+str(i+1)) 
        for j in range(num_hosts):
            index = count
            if index % 2 !=0:
                host = net.addHost( 'h'+str(count), ip=ip1+str(index)+'/24')
                net.addLink( host, switch, bw=1 )
            else:
                host = net.addHost( 'h'+str(count), ip=ip2+str(index)+'/24')
                net.addLink( host, switch , bw=2 )
            count= count+1
        switches.append(switch)

    for i in range(num_switches):
        if i < num_switches-1:
            net.addLink(switches[i], switches[i+1], bw=2)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    Topology()