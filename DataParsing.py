import argparse
import csv
import json
import xml.etree.ElementTree as ET

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="name of the input file")
parser.add_argument("-c", "--csv", action="store_true", help="output in CSV format")
parser.add_argument("-j", "--json", action="store_true", help="output in JSON format")
parser.add_argument("-x", "--xml", action="store_true", help="output in XML format")
args = parser.parse_args()

# Open input file
with open(args.input_file, "r") as f:
    data = [line.strip().split("\t") for line in f.readlines()]

# Convert data to output format
if args.csv:
    output_file = args.input_file.replace(".txt", ".csv")
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"File saved as {output_file} in CSV format.")
elif args.json:
    output_file = args.input_file.replace(".txt", ".json")
    with open(output_file, "w") as f:
        json.dump(data, f)
    print(f"File saved as {output_file} in JSON format.")
elif args.xml:
    root = ET.Element("data")
    for row in data:
        record = ET.SubElement(root, "record")
        for i, field in enumerate(row):
            ET.SubElement(record, f"field_{i}").text = field
    output_file = args.input_file.replace(".txt", ".xml")
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"File saved as {output_file} in XML format.")
else:
    print("Please specify an output format with the -c, -j, or -x option.")
