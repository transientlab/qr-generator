# QRgenerator

---

## Description
The program implements the generation of QR codes of three types:
- LINK - opens a URL address
- WIFI - initiates a connection to a WiFi network
- VCARD - imports into the contact list

The program generates PNG files.

---

## Instructions
To generate QR codes, prepare an input file named `input-list.txt` and place it in the directory with the program file `qr-generator.exe`. Each line in the input file corresponds to a QR code:

{code type} `|` {data} `|` {output file name}

Each line can contain any number of spaces and tabs.

### {data} depending on the code type
#### LINK
The {data} field contains a URL address.
#### WIFI
The {data} field contains the following values:
- `T:` Security type: `WPA`, `WEP`, `none`
- `S:` Network name (SSID)
- `P:` Network password matching the security type
#### VCARD
The {data} field contains the file name of a VCF business card [standard](https://datatracker.ietf.org/doc/html/rfc6350).

---

## Example
Sample contents of the input file: