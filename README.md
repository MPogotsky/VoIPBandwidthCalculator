# ViIP Bandwidth Calculator

Rapid growth of computer networks led to an increase in the popularity of
internet telephony in the late 20th century. Today it is widely used by both large
companies and individual users. The use of modern IP telephony technologies
allows users to significantly reduce the cost of calls and integrate telephone services
with internet services, which causes problems with the dimensioning of network
resources needed to maintain a decent quality of services.

For such needs a calculator has been implemented. Based
on the key parameters of VoIP technology, it is intended to facilitate the calculation
of the necessary bandwidth for the implementation of a given service.

## Parameters
In the calculator you can specify following parameters described below to find needed bandwidth.

### Codecs
VoIP Bandwidth calculator works with stack of codecs defined by **ITU-T** and **IETF**. Table 
below describes all used codecs, but codec-stack can be easily extended.

Standard | Codec | Bitrate | Frame Size |
:------------: | :------------: | :------------: | :------------: |
ITU-T     | G.711   | 64kbps    | 10ms  |
ITU-T     | G.726   | 16kbps    | 5ms   |
ITU-T     | G.728   | 12.8kbps  | 5ms |
ITU-T     | G.729   | 8kbps     | 10ms |
ITU-T     | G.723.1 | 5.3kbps   | 30ms  |
IETF      | iLBC    | 15.2kbps  | 20ms |

### Protocols
VoIP Bandwidth calculator works with stack of protocols of different layers. Table 
below describes all used protocols with their header sizes used while transmission.

Protocol | Header |
:------------: | :------------: |
RTP             | 12 byte|
UDP             | 8 byte|
IPv4            | 20 byte|
IPv6            | 40 byte|
Ethernet 802.3  | 38 byte|

## Overview

VoIP calculator is a relatively simple application. It consists of one window.
divided into two sections, the first section is for setting parameters and the other one
is used to demonstrate the results.
![VoIP Calculator main window](C:\Users\matve\Pictures\Screenshots\MainWindow.PNG "Figure_1")

Checkout other figures below, to get used to VoIP Calculator UI.

1. Selection of the codec and its parameters
![VoIP Calculator codecs](C:/Users/matve/Pictures/Screenshots/CodecWindow.png "Figure_2")
2. Protocol stack selection with IP version selection
![VoIP Calculator protocols for IP](C:/Users/matve/Pictures/Screenshots/ProtocolWindow.png)
3. Number of channels
![VoIP Calculator number of channels](C:/Users/matve/Pictures/Screenshots/CahnnelWindow.png)
