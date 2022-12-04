



Contents
========

* [OOMP Codes Described](#oomp-codes-described)
	* [OOMP Tag Summary](#oomp-tag-summary)

# OOMP Codes Described
  
A part's ID has five parts

    TYPE-SIZE-COLOR-DESCRIPTION-INDEX

	* TYPE - This defines the part type (Ex. HEAD - Header, LEDS - LED)
	* SIZE - This is the size category or package of a part (Ex.  I01 - 0.1", W04 - 1.4 Watt Resistor, 0603 - 0603 (SMD))
	* COLOR - This is the parts color or material (Ex. R - Red, M - Metal ) (Default X)
	* DESCRIPTION - This is a defining charachteristic of the part and is the same across a type (Ex. (HEAD) PI03 - 3 Pins, (RESE) O561 - 560 Ohms) (Default XXXX)
	* INDEX - This is an additional piece of information that differentiates a part and can change within type (Ex. 67 - 1% tolerance, RA - right angle) (Default 01)

## OOMP Tag Summary

### typeTags
  

|Code|Name|Description|
| :---: | :---: | :---: |
|ANTE|Antenna|Antenna|
|BAHO|Battery Holder|Battery Holder|
|BAPI|Badge Pin|Badge Pin|
|BREB|Breadboard|Breadboard|
|BUTA|Pushbutton (Tactile)|Pushbutton (Tactile)|
|BUTP|Pushbutton|Pushbutton|
|BUZZ|Buzzer|Buzzer|
|CABL|Cable|Cable|
|CAPC|Capacitor (Ceramic)|Capacitor (Ceramic)|
|CAPE|Capacitor (Electrolytic)|Capacitor (Electrolytic)|
|CAPT|Capacitor (Tantalum)|Capacitor (Tantalum)|
|CERE|Ceramic Resonator|Ceramic Resonator|
|DBCO|Connector|Connector|
|CRHO|Crimp Housing|Crimp Housing|
|DCJP|DC Jack|DC Jack|
|DCPP|DC Plug|DC Plug|
|DIOD|Diode|Diode|
|DIOS|Diode (Schottky)|Diode (Schottky)|
|DISP|Display|Display|
|FERB|Ferrite Bead|Ferrite Bead|
|HEAD|Header|Header|
|HEAS|Header (Socket)|Header (Socket)|
|HEAL|Header (Long)|Header (Long)|
|HEDS|Headphone Socket|Headphone Socket|
|HELF|Female Header (Long)|Female Header (Long)|
|HESH|Heat Shrink|Heat Shrink|
|ICIC|||
|MCUU|MCU|MCU|
|ICSO|IC Socket|IC Socket|
|INDU|Inductor|Inductor|
|JSTS|JST Socket|JST Socket|
|JUMP|Jumper|Jumper|
|LEDS|LED|LED|
|MICR|Microphone|Microphone|
|MOSN|N-Ch. MOSFET|N-Ch. MOSFET|
|MOSP|P-Ch. MOSFET|P-Ch. MOSFET|
|MOTO|Motor|Motor|
|MOTV|Motor (Vibrating)|Motor (Vibrating)|
|NHFF|Nylon Standoff (F-F)|Nylon Standoff (F-F)|
|NNUT|Nylon Nut|Nylon Nut|
|NSCR|Nylon Screw|Nylon Screw|
|NUTT|Nut|Nut|
|OPAM|Op Amp|Op Amp|
|PHTR|Phototransistor|Phototransistor|
|POTE|Potentiometer|Potentiometer|
|PIEZ|Piezo Element|Piezo Element|
|POAD|Power Adapter|Power Adapter|
|PRIV|Plastic Rivet|Plastic Rivet|
|RBCC|Crimped Ribbon Cable|Crimped Ribbon Cable|
|REFU|Resetable Fuse|Resetable Fuse|
|RELA|Relay|Relay|
|RESA|Resistor Array|Resistor Array|
|RESE|Resistor|Resistor|
|RJ45|RJ45|RJ45|
|SCRE|Machine Screw|Machine Screw|
|SDCS|SD Card Socket|SD Card Socket|
|SENS|Sensor|Sensor|
|SERV|Servo|Servo|
|SWIS|Switch (Slide)|Switch (Slide)|
|TERS|Screw Terminal|Screw Terminal|
|THER|Thermistor|Thermistor|
|TILS|Tilt Switch|Tilt Switch|
|TINB|Tin Box|Tin Box|
|TRNN|NPN Transistor|NPN Transistor|
|TRNP|PNP Transistor|PNP Transistor|
|USBS|USB Socket|USB Socket|
|UFLS|UFL Socket|UFL Socket|
|VARI|Varistor|Varistor|
|VREG|Voltage Regulator|Voltage Regulator|
|WIRS|Stranded Wire|Stranded Wire|
|XTAL|Crystal|Crystal|
||||

### sizeTags
  

|Code|Name|Description|
| :---: | :---: | :---: |
|0402|SMD (0402)|SMD (0402)|
|0603|SMD (0603)|SMD (0603)|
|06038|SMD (0603-8)|SMD (0603-8)|
|0805|SMD (0805)|SMD (0805)|
|0806|SMD (0806)|SMD (0806)|
|1206|SMD (1206)|SMD (1206)|
|1263|SMD (1206-3)|SMD (1206-3)|
|1210|SMD (1210)|SMD (1210)|
|1812|SMD (1812)|SMD (1812)|
|12068|SMD (1206-8)|SMD (1206-8)|
|2312|SMD (2312)|SMD (2312)|
|2917|SMD (2917)|SMD (2917)|
|D214|SMD (DO-214)|SMD (DO-214)|
|MMA|SMD (Mini MELF)|SMD (Mini MELF)|
|3025|SMD (3025)|SMD (3025)|
|1515|SMD (1515)|SMD (1515)|
|2020|SMD (2020)|SMD (2020)|
|2121|SMD (2121)|SMD (2121)|
|3215|SMD (3215)|SMD (3215)|
|3216|SMD (3216)|SMD (3216)|
|3528|SMD (3528)|SMD (3528)|
|3535|SMD (3535)|SMD (3535)|
|3643|SMD (3643)|SMD (3643)|
|4628|SMD (4628)|SMD (4628)|
|4632|SMD (4632)|SMD (4632)|
|4735|SMD (4735)|SMD (4735)|
|5032|SMD (5032)|SMD (5032)|
|5050|SMD (5050)|SMD (5050)|
|5252|SMD (5252)|SMD (5252)|
|6032|SMD (6032)|SMD (6032)|
|6060|SMD (6060)|SMD (6060)|
|6727|SMD (6727)|SMD (6727)|
|7135|SMD (7135)|SMD (7135)|
|7343|SMD (7343)|SMD (7343)|
|7827|SMD (7827)|SMD (7827)|
|AVA|SMD (AVX-A)|SMD (AVX-A)|
|AVB|SMD (AVX-B)|SMD (AVX-B)|
|AVC|SMD (AVX-C)|SMD (AVX-C)|
|S123|SMD (SOD-123)|SMD (SOD-123)|
|S323|SMD (SOD-323)|SMD (SOD-323)|
|S523|SMD (SOD-523)|SMD (SOD-523)|
|SC8|8 Pin SMD (SOIC)|8 Pin SMD (SOIC)|
|SC14|14 Pin SMD (SOIC)|14 Pin SMD (SOIC)|
|SC16|16 Pin SMD (SOIC)|16 Pin SMD (SOIC)|
|SC75|5 Pin SMD (SC70)|5 Pin SMD (SC70)|
|PS20|SMD (Power SO-20)|SMD (Power SO-20)|
|T92|TO-92|TO-92|
|T220|TO-220|TO-220|
|T252|TO-252 (SMD)|TO-252 (SMD)|
|G28|28 AWG|28 AWG|
|CR1220|CR1220|CR1220|
|W04|1/4 Watt|1/4 Watt|
|W08|1/8 Watt|1/8 Watt|
|W1|1 Watt|1 Watt|
|W2|2 Watt|2 Watt|
|W3|3 Watt|3 Watt|
|W4|4 Watt|4 Watt|
|W5|5 Watt|5 Watt|
|W6|6 Watt|6 Watt|
|W7|7 Watt|7 Watt|
|W8|8 Watt|8 Watt|
|W9|9 Watt|9 Watt|
|W10|10 Watt|10 Watt|
|W11|11 Watt|11 Watt|
|W12|12 Watt|12 Watt|
|W13|13 Watt|13 Watt|
|W14|14 Watt|14 Watt|
|W15|15 Watt|15 Watt|
|W16|16 Watt|16 Watt|
|W17|17 Watt|17 Watt|
|W18|18 Watt|18 Watt|
|W19|19 Watt|19 Watt|
|W20|20 Watt|20 Watt|
|W21|21 Watt|21 Watt|
|W22|22 Watt|22 Watt|
|W23|23 Watt|23 Watt|
|W24|24 Watt|24 Watt|
|W25|25 Watt|25 Watt|
|W26|26 Watt|26 Watt|
|W27|27 Watt|27 Watt|
|W28|28 Watt|28 Watt|
|W29|29 Watt|29 Watt|
|W30|30 Watt|30 Watt|
|W31|31 Watt|31 Watt|
|W32|32 Watt|32 Watt|
|W33|33 Watt|33 Watt|
|W34|34 Watt|34 Watt|
|W35|35 Watt|35 Watt|
|W36|36 Watt|36 Watt|
|W37|37 Watt|37 Watt|
|W38|38 Watt|38 Watt|
|W39|39 Watt|39 Watt|
|W40|40 Watt|40 Watt|
|W41|41 Watt|41 Watt|
|W42|42 Watt|42 Watt|
|W43|43 Watt|43 Watt|
|W44|44 Watt|44 Watt|
|W45|45 Watt|45 Watt|
|W46|46 Watt|46 Watt|
|W47|47 Watt|47 Watt|
|W48|48 Watt|48 Watt|
|W49|49 Watt|49 Watt|
|W50|50 Watt|50 Watt|
|W51|51 Watt|51 Watt|
|W52|52 Watt|52 Watt|
|W53|53 Watt|53 Watt|
|W54|54 Watt|54 Watt|
|W55|55 Watt|55 Watt|
|W56|56 Watt|56 Watt|
|W57|57 Watt|57 Watt|
|W58|58 Watt|58 Watt|
|W59|59 Watt|59 Watt|
|W60|60 Watt|60 Watt|
|W61|61 Watt|61 Watt|
|W62|62 Watt|62 Watt|
|W63|63 Watt|63 Watt|
|W64|64 Watt|64 Watt|
|W65|65 Watt|65 Watt|
|W66|66 Watt|66 Watt|
|W67|67 Watt|67 Watt|
|W68|68 Watt|68 Watt|
|W69|69 Watt|69 Watt|
|W70|70 Watt|70 Watt|
|W71|71 Watt|71 Watt|
|W72|72 Watt|72 Watt|
|W73|73 Watt|73 Watt|
|W74|74 Watt|74 Watt|
|W75|75 Watt|75 Watt|
|W76|76 Watt|76 Watt|
|W77|77 Watt|77 Watt|
|W78|78 Watt|78 Watt|
|W79|79 Watt|79 Watt|
|W80|80 Watt|80 Watt|
|W81|81 Watt|81 Watt|
|W82|82 Watt|82 Watt|
|W83|83 Watt|83 Watt|
|W84|84 Watt|84 Watt|
|W85|85 Watt|85 Watt|
|W86|86 Watt|86 Watt|
|W87|87 Watt|87 Watt|
|W88|88 Watt|88 Watt|
|W89|89 Watt|89 Watt|
|W90|90 Watt|90 Watt|
|W91|91 Watt|91 Watt|
|W92|92 Watt|92 Watt|
|W93|93 Watt|93 Watt|
|W94|94 Watt|94 Watt|
|W95|95 Watt|95 Watt|
|W96|96 Watt|96 Watt|
|W97|97 Watt|97 Watt|
|W98|98 Watt|98 Watt|
|W99|99 Watt|99 Watt|
|TH|||
|SM|||
|ST|Standard|Standard|
|MC|Micro|Micro|
|MN|Mini|Mini|
|TA|Type A|Type A|
|TB|Type B|Type B|
|TC|Type C|Type C|
|SC|Solid|Solid|
|SS16|16 Pin SMD (SSOP)|16 Pin SMD (SSOP)|
|SS24|24 Pin SMD (SSOP)|24 Pin SMD (SSOP)|
|SS28|28 Pin SMD (SSOP)|28 Pin SMD (SSOP)|
|MS08|8 Pin SMD (MSOP)|8 Pin SMD (MSOP)|
|TS14|14 Pin SMD (TSSOP)|14 Pin SMD (TSSOP)|
|TS20|20 Pin SMD (TSSOP)|20 Pin SMD (TSSOP)|
|TS24|24 Pin SMD (TSSOP)|24 Pin SMD (TSSOP)|
|128X64|128 x 64 Pixels|128 x 64 Pixels|
|16X2|16 x 2 Character|16 x 2 Character|
|7SEL|7 Segment LED|7 Segment LED|
|10SEL|10 Segment LED Bargraph|10 Segment LED Bargraph|
|RJ45|128 x 64 Pixels|128 x 64 Pixels|
|DB09|DB9|DB9|
|DB15|DB15|DB15|
|DB25|DB25|DB25|
|ACUS|American Style (120v)|American Style (120v)|
|SMA|SMA|SMA|
|DPAK|DPAK|DPAK|
|ADAF|Adafruit|Adafruit|
|ARDC|Compatible Arduino|Compatible Arduino|
|ARDU|Arduino|Arduino|
|OOML|Oomlout|Oomlout|
|RASP|Raspberry Pi Foundation|Raspberry Pi Foundation|
|SEEE|SEEED Studios|SEEED Studios|
|SPAR|Sparkfun|Sparkfun|
|ELLA|Electro Lama|Electro Lama|
|HC49|HC49|HC49|
|HC49S|SMD (HC49)|SMD (HC49)|
|['###']|['### mm']|['### mm']|
||||

### colorTags
  

|Code|Name|Description|
| :---: | :---: | :---: |
|N|Brown|Brown|
|R|Red|Red|
|O|Orange|Orange|
|Y|Yellow|Yellow|
|G|Green|Green|
|L|Blue|Blue|
|V|Purple|Purple|
|E|Grey|Grey|
|W|White|White|
|B|Black|Black|
|P|Pink|Pink|
|Z|Rainbow|Rainbow|
|RGB|RGB|RGB|
|GYR|Green, Yellow, Red|Green, Yellow, Red|
|C|Clear|Clear|
|X|||
|U|||
|T|||
|M|Metal|Metal|
|DUE|DUE|DUE|
|MEGA|Mega|Mega|
|MICRO|Micro|Micro|
|NANO|Nano|Nano|
|PICO|Pico|Pico|
|SHEN|Shennie|Shennie|
|HQBS|HQB Special|HQB Special|
|UNO|Uno|Uno|
|LEO|Leonardo|Leonardo|
||||

### descTags
  

|Code|Name|Description|
| :---: | :---: | :---: |
|ADJU|Adjustable|Adjustable|
|BUCA|Adjustable Buck|Adjustable Buck|
|BOSA|Adjustable Boost|Adjustable Boost|
|BOS5|5v Boost|5v Boost|
|CREE|Cree|Cree|
|FROS|Frosted|Frosted|
|TINT|Tinted|Tinted|
|TEHU|Temperature and Humidity|Temperature and Humidity|
|CLER|Clear|Clear|
|THTH|Through Hole|Through Hole|
|DPDT|DPDT|DPDT|
|OLED|OLED|OLED|
|LCD|LCD|LCD|
|SMDS|SMD|SMD|
|SPDT|SPDT|SPDT|
|SPST|SPST|SPST|
|SOCK|Socket|Socket|
|STAN|||
|ESDP|ESD Protection|ESD Protection|
|SIGN|Signal|Signal|
|BOTT|BOttom|BOttom|
|SUBR|Super Bright|Super Bright|
|NH15|15 nH|15 nH|
|UH10|10 uH|10 uH|
|LIRE|Light (Resistive)|Light (Resistive)|
|K222|2222A|2222A|
|K328|AtMega328P|AtMega328P|
|K125|Quad Buffer (74HC125)|Quad Buffer (74HC125)|
|K232|FTDI USB-Serial|FTDI USB-Serial|
|G24|2.4 Ghz|2.4 Ghz|
|GROV|Grove|Grove|
|HUTE|Humidity and Temperature|Humidity and Temperature|
|PHRE|Photo Reflective|Photo Reflective|
|PIRS|PIRS|PIRS|
|UVUV|Ultraviolet|Ultraviolet|
|PIVB|Piezo Vibration|Piezo Vibration|
|K555|555 Timer|555 Timer|
|KCH340|USB-Serial (CH340)|USB-Serial (CH340)|
|KFT232|USB-Serial (FT232RL)|USB-Serial (FT232RL)|
|K168|AtMega168P|AtMega168P|
|K345|Digital Accelerometer (ADXL345)|Digital Accelerometer (ADXL345)|
|K343|Digital Accelerometer (ADXL343)|Digital Accelerometer (ADXL343)|
|K8|AtMega8A|AtMega8A|
|K2560|AtMega2560|AtMega2560|
|K4988|Stepper Motor Driver (A4988)|Stepper Motor Driver (A4988)|
|K1555|Lithium Ion Battery Charger (1 Cell) (MAX1555)|Lithium Ion Battery Charger (1 Cell) (MAX1555)|
|K125LS|Single Buffer (74LVC1G125)|Single Buffer (74LVC1G125)|
|K595|74HC595 8-Bit Shift Register (Latching)|74HC595 8-Bit Shift Register (Latching)|
|K2515|CAN Controller SPI (MCP2515)|CAN Controller SPI (MCP2515)|
|K2551|CAN Tranceiver (MCP2521)|CAN Tranceiver (MCP2521)|
|K73831|Lithium Cell Charger One Cell (MCP73831)|Lithium Cell Charger One Cell (MCP73831)|
|K2803|ULN2803A Octal Transistor Array|ULN2803A Octal Transistor Array|
|K2003|ULN2003A Heptal Transistor Array|ULN2003A Heptal Transistor Array|
|K2904|LM2904 Dual|LM2904 Dual|
|K333|OPA333|OPA333|
|KDS1307|Real Time Clock (DS1307)|Real Time Clock (DS1307)|
|KDS1337|Real Time Clock (DS1337)|Real Time Clock (DS1337)|
|KLPC33|LPC11U35FHI33 (Cortex M0)|LPC11U35FHI33 (Cortex M0)|
|KLPC11|LPC11U24 (Cortex M0)|LPC11U24 (Cortex M0)|
|KLPC14|LPC1114 (Cortex M0)|LPC1114 (Cortex M0)|
|KLPC17|LPC1768 (Cortex M3)|LPC1768 (Cortex M3)|
|K108|8-bit Level Shifter (TXS108E)|8-bit Level Shifter (TXS108E)|
|K6612|Dual H-Bridge (TB6612)|Dual H-Bridge (TB6612)|
|K9221|12 Channel Constant Current LED Driver (MY9221)|12 Channel Constant Current LED Driver (MY9221)|
|K1550|Photo Reflective (LTH1550)|Photo Reflective (LTH1550)|
|K1637|7 Segment 8 Digit LED Driver (TM1637)|7 Segment 8 Digit LED Driver (TM1637)|
|K1620|7 Segment 8 Digit LED Driver (TM1620)|7 Segment 8 Digit LED Driver (TM1620)|
|KHT46|Holtek HT46R066|Holtek HT46R066|
|K108B|8 bit Level Shifter (TXB0108PW)|8 bit Level Shifter (TXB0108PW)|
|K1820|Voice Recorder (ISD1820P)|Voice Recorder (ISD1820P)|
|K2659|GPS Amplifier (MAX2659)|GPS Amplifier (MAX2659)|
|K2812|Smart Controller (WS2812B)|Smart Controller (WS2812B)|
|K2811|Smart Controller (WS2811)|Smart Controller (WS2811)|
|K102|Smart Controller (APA102)|Smart Controller (APA102)|
|KFLA|Flashing (50F503)|Flashing (50F503)|
|K2291|PIR Motion Sensing (TM2291)|PIR Motion Sensing (TM2291)|
|K5883|3-Axis Digital Compass (HMC5883L)|3-Axis Digital Compass (HMC5883L)|
|K9250|9-Axis Inertial Measurement Unit (MPU-9250)|9-Axis Inertial Measurement Unit (MPU-9250)|
|K36|Temperature (TMP36)|Temperature (TMP36)|
|K7660|3-Axis Accelerometer (MMA7660FCR1)|3-Axis Accelerometer (MMA7660FCR1)|
|KS8050|S8050|S8050|
|KBC337|BC337|BC337|
|KBC327|BC327|BC327|
|KS8550|S8550|S8550|
|KC1815|C1815|C1815|
|KBSS138|BSS138|BSS138|
|K6401|IRLML6401|IRLML6401|
|KMIC5225|MIC5225|MIC5225|
|KMIC5205|MIC5205|MIC5205|
|KLD1117|LD1117|LD1117|
|KXC6206|XC6206|XC6206|
|K4184|MNAOD4184A|MNAOD4184A|
|KMBR120|MBR120|MBR120|
|K5053|SGPT5053C|SGPT5053C|
|LEDS|LED|LED|
|COCA|Common Cathode|Common Cathode|
|COAN|Common Anode|Common Anode|
|ATTINY|ATTiny|ATTiny|
|K18B20|DS18B20 (1-Wire Digital Thermometer)|DS18B20 (1-Wire Digital Thermometer)|
|K31|TYPE-C-31-M-12|TYPE-C-31-M-12|
|HINGE|Hinged|Hinged|
|FLAT|Flat|Flat|
|EVERY|Every|Every|
|LG32|(LGT8F328P)|(LGT8F328P)|
|AT32|(Atmel328)|(Atmel328)|
|INLI|(Inline)|(Inline)|
|K4148|1N4148|1N4148|
|KRB520S30T|RB520S30T1G|RB520S30T1G|
|KCH32V|CH32V|CH32V|
|K5551|MMBT5551|MMBT5551|
|KSS8050|SS8050|SS8050|
|KS9013|S9013|S9013|
|KS9015|S9015|S9015|
|KMMBT5401|MMBT5401|MMBT5401|
|KMMBT2222A|MMBT2222A|MMBT2222A|
|KSS8550|SS8550|SS8550|
|KS9012|S9012|S9012|
|KD882|D882|D882|
|KMMBT3904|MMBT3904|MMBT3904|
|KLBSS84LT1G|LBSS84LT1G|LBSS84LT1G|
|KB772|B772|B772|
|KIRLB8721|IRLB8721|IRLB8721|
|['MZ###']|['### MHz']|['### MHz']|
|['UF###']|['### Uf']|['### Uf']|
|['NF###']|['### nf']|['### nf']|
|['PF###']|['### pf']|['### pf']|
|['V###']|['### v']|['### v']|
|['PI###']|['### pins']|['### pins']|
|['O###']|['### Ohms']|['3 digit code for Ohms, (ie 103 10k,102 1k)']|
||||

### indexTags
  

|Code|Name|Description|
| :---: | :---: | :---: |
|CA|Common Anode|Common Anode|
|CC|Common Cathode|Common Cathode|
|LI|w/Lights|w/Lights|
|ML|Male|Male|
|FM|Female|Female|
|AI|25 mA|25 mA|
|AH|100 mA|100 mA|
|AC|150 mA|150 mA|
|AD|250 mA|250 mA|
|AE|200 mA|200 mA|
|AB|1.2 A|1.2 A|
|SM|(SMD)|(SMD)|
|RA|Right Angle|Right Angle|
|RS|Right Angle (SMD)|Right Angle (SMD)|
|RO|(Round)|(Round)|
|OOEB|(OOEB)|(OOEB)|
|TH|(Through Hole)|(Through Hole)|
|LW|(Lead Wire)|(Lead Wire)|
|WS2811|(WS2811)|(WS2811)|
|TC3590|(3590)|(3590)|
|SHRO|Shrouded (IDC)|Shrouded (IDC)|
|SHRR|Shrouded (IDC) Right Angle|Shrouded (IDC) Right Angle|
|VADJ|Adjustable Voltage|Adjustable Voltage|
||||
