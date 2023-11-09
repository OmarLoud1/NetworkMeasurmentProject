import csv
import os

def script4(input_file_path, reference_file_path, output_file_path):
    with open(reference_file_path, 'r') as file1:
        file1_contents = set(file1.readlines())

    with open(input_file_path) as file2:
        file2_lines = file2.readlines()

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for line in file2_lines:
            line_stripped = line.strip()
            if line in file1_contents:
                csv_writer.writerow([line_stripped, 1])

folders = ['Legal', 'Illegal']
reference_file_path = '1.txt'
for folder in folders:
    input_folder_path = f'IPS/{folder}'
    output_folder_path = f'Results/ipSum/{folder}'
    for file_name in os.listdir(input_folder_path):
        input_file_path = f'{input_folder_path}/{file_name}'
        output_file_path = f'{output_folder_path}/{file_name}.csv'
        script4(input_file_path, reference_file_path, output_file_path)
