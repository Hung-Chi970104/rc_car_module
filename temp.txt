# RP2040 Hacker Board
- Demo video (with radio nrf24l01): https://youtu.be/eCMlnlmFBuc
- Demo video (radio control nrf24l01): https://youtu.be/_LA9TkBpY54

![RP2040 V2](assets/RP2040_v2.png)

- Upgraded flash storage from 2MB (W25Q16JVUXIQ TR) to 16MB (W25Q64JVXGIQ)
- Replaced MCP1700x-330xxTT (linear regulator) with RT6154AGQW (buck-boost switching regulator)
- Added Schottky Diode to allow external power supply
- Added a RESET button
- Changed 33pF crystal cap to 15pF to match the crystal I ordered

## Components
- RP2040
- 12MHz Crystal (ABM8-272-T3)
- 8MB Flash Storage (W25Q64JVXGIQ)
- Buck-Boost Switching Regulator (RT6154AGQW)
- USB-C (TYPE-C-31-M-12)

## Pinouts
| Pin Number (Left) | Description | Pin Number (Right) | Description |
| ------------- | ------------- | ------------- | ------------- |
| 1 | GPIO0 | 1 | VBUS |
| 2 | GPIO1 | 2 | VSYS |
| 3 | GND | 3 | GND |
| 4 | GPIO2 | 4 | GPIO28_ADC2 |
| 5 | GPIO3 | 5 | GPIO27_ADC1 |
| 6 | GPIO4 | 6 | 3V3 |
| 7 | GPIO5 | 7 | GPIO26_ADC0 |
| 8 | BOOTSEL | 8 | GND |
| 9 | GPIO6 | 9 | GPIO25 |
| 10 | GPIO7 | 10 | GPIO24 |
| 11 | GPIO8 | 11 | GPIO23 |
| 12 | GPIO9 | 12 | GPIO22 |
| 13 | GND | 13 | GND |
| 14 | GPIO10 | 14 | GPIO21 |
| 15 | GPIO11 | 15 | GPIO20 |
| 16 | GPIO12 | 16 | GPIO19 |
| 17 | GPIO13 | 17 | GND |
| 18 | GND | 18 | GPIO18 |
| 19 | GPIO14 | 19 | GPIO17 |
| 20 | GPIO15 | 20 | GPIO16 |

## PCBs

![comparison](assets/demo_version2.png)

- 2 layers
- Single-sided component placement
- 2.6mm board thickness
- HASL (with lead) surface finish
- 1oz outer copper weight

### PCB Schematic
![schematic](assets/schematic.png)

### PCB Layouts
![pcb_layout_front](assets/RP2040-F_Cu.png)
![pcb_layout_back](assets/RP2040-B_Cu.png)

### 3D Model
![model_front](assets/RP2040_front.png)
![model_back](assets/RP2040_back.png)

## Rendered Demo
![demo_2](assets/demo_2.png)
![demo_3](assets/demo_3.png)
![demo_4](assets/demo_4.png)


