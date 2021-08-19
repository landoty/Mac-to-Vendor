# MAC to Vendor
This tool utilizes records from the IEEE to relate MAC addresses within
an Excel file with their respective vendors, outputting each in the adjacent
column

# Tool Overview
Without a local database or a reliable and free API, the best way to relate
MAC addresses to their vendors is through some intuitive file I/O. This tool
searches from a publicly-available text file from the IEEE of `Organizationally
Unique Identifiers (OUI)` and writes the vendor name to the same Excel
file as the MAC address is pulled from

### Time and Power Considerations
In situations where many MAC addresses need relating, a brute force solution `-
where each OUI is searched for within the IEEE file -` is far too cumbersome. I
originally developed this tool for the University of Kansas Network Architecture
team, in which we required this tool to be ran across 50,000+ records in a
single report.

As such, this tool stores each entry within a dictionary `- key = OUI and
value = Vendor -` and is searched before searching within the IEEE file.
Institutions, like KU, often use similar devices from the same Vendors, so we
can see how it much more efficient.

More specifically, this tool reduced runtime by nearly **eighty percent**.

### Getting IEEE file
How would you get a text file from a public website? **cURL**. This tool utilizes
cURL by sending a cURL command directly to the local machine via the Python `os`
library. This could of course be complicated with a HTTP request via the `requests`
library, but this is automation. Let's make things simple

Running the `remove_lines.py` file will remove unnecessary information from the
raw IEEE file as it contains Vendor address and contact information as well as
the Hex form of the OUI. For this tool, we are using Base16

# How to Use
Using this tool is quite simple. Simply follow the proceeding steps

1. Ensure you have the oui_vendors.txt file
```sh
$ python3 remove_lines.py
```
2. Provide Excel file name and run
```sh
$ python3 mac_to_device.py <excel_mac_name>.xlsx
```
3. Provide column number where MAC addresses are stored
```sh
$ python3 mac_to_device.py <excel_mac_name>.xlsx
-----------------------------------
MAC Address Column Number: <enter column here>
-----------------------------------
```
4. View and analyze report

# Contact
For any inquiry regarding this tool, please submit an Issue, Pull Request, or
contact me personally via email or LinkedIn
