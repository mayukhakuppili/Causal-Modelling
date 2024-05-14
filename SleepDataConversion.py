import csv
import os
import xml.etree.ElementTree as ET


def convert_xml_to_csv(xml_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(csv_file, 'w', newline='') as csv_data:
        csv_writer = csv.writer(csv_data)

        header = ['SleepStage']
        rows = []

        # Extract SleepStages/SleepStage
        sleep_stages = []
        for sleep_stage in root.findall('SleepStages/SleepStage'):
            stage = sleep_stage.text
            sleep_stages.append(stage)

        rows.append(sleep_stages)
        csv_writer.writerow(header)
        csv_writer.writerows(zip(*rows))


# Specify the folder containing XML files
xml_folder = './'
csv_folder = './'

# Create the output folder if it doesn't exist
os.makedirs(csv_folder, exist_ok=True)

# Iterate over XML files in the folder
for filename in os.listdir(xml_folder):
    if filename.endswith('.xml'):
        xml_file = os.path.join(xml_folder, filename)
        csv_file = os.path.join(csv_folder, os.path.splitext(filename)[0] + '.csv')
        convert_xml_to_csv(xml_file, csv_file)
