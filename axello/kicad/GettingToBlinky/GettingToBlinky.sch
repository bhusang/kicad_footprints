EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:GTB
LIBS:GettingToBlinky-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L 7555 U1
U 1 1 58DA3579
P 5300 3800
F 0 "U1" H 5850 3000 60  0000 R CNN
F 1 "7555" H 5425 3725 60  0000 C CNN
F 2 "Housings_SOIC:SOIC-8_3.9x4.9mm_Pitch1.27mm" H 4875 4375 60  0001 C CNN
F 3 "" H 4875 4375 60  0001 C CNN
	1    5300 3800
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 58DA3631
P 4050 3150
F 0 "R1" V 4130 3150 50  0000 C CNN
F 1 "1K" V 4050 3150 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3980 3150 50  0001 C CNN
F 3 "" H 4050 3150 50  0001 C CNN
	1    4050 3150
	1    0    0    -1  
$EndComp
$Comp
L R R2
U 1 1 58DA36C3
P 4050 3800
F 0 "R2" V 4130 3800 50  0000 C CNN
F 1 "470K" V 4050 3800 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3980 3800 50  0001 C CNN
F 3 "" H 4050 3800 50  0001 C CNN
	1    4050 3800
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 58DA36F0
P 6300 3850
F 0 "R3" V 6380 3850 50  0000 C CNN
F 1 "1K" V 6300 3850 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 6230 3850 50  0001 C CNN
F 3 "" H 6300 3850 50  0001 C CNN
	1    6300 3850
	1    0    0    -1  
$EndComp
$Comp
L C C1
U 1 1 58DA3730
P 4050 4450
F 0 "C1" H 4075 4550 50  0000 L CNN
F 1 "1µF" H 4075 4350 50  0000 L CNN
F 2 "Capacitors_SMD:C_1206_HandSoldering" H 4088 4300 50  0001 C CNN
F 3 "" H 4050 4450 50  0001 C CNN
	1    4050 4450
	1    0    0    -1  
$EndComp
$Comp
L LED D1
U 1 1 58DA3776
P 6300 4250
F 0 "D1" H 6300 4350 50  0000 C CNN
F 1 "LED" H 6300 4150 50  0000 C CNN
F 2 "LEDs:LED-3MM" H 6300 4250 50  0001 C CNN
F 3 "" H 6300 4250 50  0001 C CNN
	1    6300 4250
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4550 3550 4050 3550
Wire Wire Line
	4050 3300 4050 3650
Connection ~ 4050 3550
Wire Wire Line
	4550 3700 4550 4050
Wire Wire Line
	4550 4050 4050 4050
Wire Wire Line
	4050 3950 4050 4300
Connection ~ 4050 4050
Wire Wire Line
	6050 3550 6300 3550
Wire Wire Line
	6300 3550 6300 3700
Wire Wire Line
	6300 4000 6300 4100
Connection ~ 4550 4050
Wire Wire Line
	4050 4600 4050 4950
Wire Wire Line
	4050 4950 6300 4950
Wire Wire Line
	5175 4950 5175 4725
Connection ~ 5175 4950
Wire Wire Line
	6300 4950 6300 4400
Wire Wire Line
	5250 2875 5250 2775
Wire Wire Line
	4050 2775 5450 2775
Wire Wire Line
	4050 2775 4050 3000
Wire Wire Line
	5450 2775 5450 2875
Connection ~ 5250 2775
Text Label 4125 2775 0    60   ~ 0
VDD
$Comp
L GND #PWR01
U 1 1 58DA3C39
P 4650 5100
F 0 "#PWR01" H 4650 4850 50  0001 C CNN
F 1 "GND" H 4650 4950 50  0000 C CNN
F 2 "" H 4650 5100 50  0001 C CNN
F 3 "" H 4650 5100 50  0001 C CNN
	1    4650 5100
	1    0    0    -1  
$EndComp
$Comp
L Battery BT1
U 1 1 58DA3EDF
P 2725 3900
F 0 "BT1" H 2825 4000 50  0000 L CNN
F 1 "Battery" H 2825 3900 50  0000 L CNN
F 2 "GTB:BatteryHolder" V 2725 3960 50  0001 C CNN
F 3 "" V 2725 3960 50  0001 C CNN
	1    2725 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	2725 3300 2950 3300
Text Label 2825 3300 0    60   ~ 0
VDD
$Comp
L GND #PWR02
U 1 1 58DA3FAB
P 2725 4300
F 0 "#PWR02" H 2725 4050 50  0001 C CNN
F 1 "GND" H 2725 4150 50  0000 C CNN
F 2 "" H 2725 4300 50  0001 C CNN
F 3 "" H 2725 4300 50  0001 C CNN
	1    2725 4300
	1    0    0    -1  
$EndComp
Wire Wire Line
	2725 3300 2725 3700
Connection ~ 4650 4950
Wire Wire Line
	4650 4950 4650 5100
Wire Wire Line
	2725 4100 2725 4300
Text Notes 5525 5125 0    60   ~ 0
N.B. Pin 5 should NOT be grounded!
NoConn ~ 5475 4725
Connection ~ 5475 4950
$EndSCHEMATC
