# OpenCaster 

### Original authors
 - Lorenzo Pallara
 - Andrea Venturi  
(domain `avalpa.com` is down, so e-mail addresses have been removed)

### Introduction
This package is a collection of softwares for Linux system to play out and multiplex MPEG2 transport stream format.

### About this fork
Fork done by Konrad Dąbek for internal purposes. This is still a work in progress! Goals:
 - Merge own patches & cherry-picked patches created by the community
 - Enable possibility to build partially under Windows (Cygwin), with some limitations (e.g. no network stack), I've made that successfully back in 2020, but never authored this in the form of commit. Some tools are working fine under Windows through Cygwin, e.g. sec2ts, ts2sec, building DSM-CC OC/DC, DVB-SSU
 - Move to Python3

Please be aware that as of 2025, OpenCaster hasn't received any updates for more than 12 years, with last changes originating from 2013.  
In the meantime a lot of things have changed in the DVB world.  
My (Konrad Dąbek) personal beliefs are that in 2025 OpenCaster should be used only if there's no open source alternative is present (e.g. DSMCC, DVB-SSU, TTX, Subtitling, MHP/HbbTV), at least until original authors or their successors will take over the development.  
For most of other purposes you should seek for modern alternatives.  
For tables management, monitoring, debugging, lab and demo purposes please consider to check [TSDuck](https://tsduck.io/)  
For generation of MPEG TS with A/V please consider to check [FFmpeg](https://www.ffmpeg.org/) (FFmpeg is far from being perfect in DVB-SI tables generation, so teaming it up with TSDuck is a wise idea)  
  
I'm (Konrad Dąbek) providing no support for this fork, I cannot give any guarantee that it will reflect robustness of Pyhton 2 version.  
There are no plans to introduce any fixes, updates or improvements except of continuation of attempts to make it work with Python 3 and Cygwin, at least partially.  
Before reporting any issue please check behaviour on the original Python 2 release.  

### Use-cases
 - MHP, MHEG5, HbbTv and others interactive tv standards object carousel broadcast
 - Playout of locally stored, offline encoded audio and video for non-live tv and radio stations
 - Multiplexing of input multicasted UDP transport stream to output multicasted UDP transport stream
 - VOD system based on mpeg2 transport stream over IP or over DVB for walled garden network like hotels with coax or ethernet
 - DVB-SSU update
 - Data casting
 - Teletext generator
 - IP encapsualtor
 - PSI/SI generator
 - EPG generator

### Integration
OpenCaster output has been successfully integrated with a long list of dvb products, among them there are products by Cisco/Scientific Atlanta, Ericsson/Tandberg, Dektec, Eurotek, Harmonic/Scopus, MainConcept, Mitan, Screen Service, Adtec, Wellav, Arris, Sr-Systems, Deltacast...

### Manual
Avalpa Broadcast Server manual is available here: [AvalpaBroadcastServerUserManual-v3.0.pdf](docs/AvalpaBroadcastServerUserManual-v3.0.pdf)

### Test
OpenCaster has been tested with Rohde & Schwarz DVM100L, Rohde & Schwarz DVM 400, DekTec StreamXpert and a countless number of set top boxes, digital receivers and television sets.

### Technical features
 - PSI generation (PAT, PMT, NIT, SDT, TDT, AIT, TOT...)
 - EPG/EIT generation
 - Object and data carousel generation and receivement (MHP, MHEG5, HbbTv, DVB-SSU, DSMCC...)
 - third party software AC-3, MPEG2 audio, MPEG2 video and H264 video encoders support
 - Audio Description generation support
 - IP encapsulation (MPE)
 - Teletext generation
 - CBR transport stream muxing
 - PCR stamping
 - Null packet replacement
 - PID filtering
 - PID remapping
 - Null packet insertion
 - Video buffer verifier
 - PCR timing verifier
 - PES headers analyzer
 - MPEG2 video and MPEG2/AC-3 audio ES header analyzer
 - M2TS file generation from TS file

### Demo
A demonstration transport stream is available at this address: [https://web.archive.org/web/20221006041331/http://www.avalpa.com/the-key-values/15-free-software/59-opencaster-demo-roll](https://web.archive.org/web/20221006041331/http://www.avalpa.com/the-key-values/15-free-software/59-opencaster-demo-roll) (OC3.demo.ts might be hard to be downloaded from WebArchive, original website is down, author of this fork has got the TS, but decided against uploading it to GitHub to avoid bloating the repo).

### Handy tables
#### DVB-T Modulations:
Modulation | Coding rate | GI: 1/4 | GI: 1/8 | GI: 1/16 | GI: 1/32
--|--|--|--|--|--
QPSK | 1/2 | 4.976 | 5.529 | 5.855 | 6.032
QPSK | 2/3 | 6.635 | 7.373 | 7.806 | 8.043
QPSK | 3/4 | 7.465 | 8.294 | 8.782 | 9.048
QPSK | 5/6 | 8.294 | 9.216 | 9.758 | 10.053
QPSK | 7/8 | 8.709 | 9.676 | 10.246 | 10.556
16-QAM | 1/2 | 9.953 | 11.059 | 11.709 | 12.064
16-QAM | 2/3 | 13.271 | 14.745 | 15.612 | 16.086
16-QAM | 3/4 | 14.929 | 16.588 | 17.564 | 18.096
16-QAM | 5/6 | 16.588 | 18.431 | 19.516 | 20.107
16-QAM | 7/8 | 17.418 | 19.353 | 20.491 | 21.112
64-QAM | 1/2 | 14.929 | 16.588 | 17.564 | 18.096
64-QAM | 2/3 | 19.906 | 22.118 | 23.419 | 24.128
64-QAM | 3/4 | 22.394 | 24.882 | 26.346 | 27.144
64-QAM | 5/6 | 24.882 | 27.647 | 29.273 | 30.160
64-QAM | 7/8 | 26.126 | 29.029 | 30.737 | 31.668

#### Channel to frequency table:

Channel | Frequency [MHz]
-- | --
21 | 474
22 | 482
23 | 490
24 | 498
25 | 506
26 | 514
27 | 522
28 | 530
29 | 538
30 | 546
31 | 554
32 | 562
33 | 570
34 | 578
35 | 586
36 | 594
37 | 602
38 | 610
39 | 618
40 | 626
41 | 634
42 | 642
43 | 650
44 | 658
45 | 666
46 | 674
47 | 682
48 | 690
49 | 698
50 | 706
51 | 714
52 | 722
53 | 730
54 | 738
55 | 746
56 | 754
57 | 762
58 | 770
59 | 778
60 | 786
61 | 794
62 | 802
63 | 810
64 | 818
65 | 826
66 | 834
67 | 842
68 | 850
69 | 858

#### MPEG Audio Layer 2 suggested bit rates:
 - 56 kbps -> 1 pes packet -> 1 ts packet
 - 112 kbps -> 1 pes packet -> 2 ts packets 
 - 160 kbps -> 1 pes packet -> 3 ts packets
 - 224 kbps -> 1 pes packet -> 4 ts packets  
All the others fall in the middle and are not a wise choice.