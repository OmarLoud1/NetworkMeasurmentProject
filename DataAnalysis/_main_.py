# main.py
import script1
import script2
import script3
import script4
import os

folders = ['Legal', 'Illegal']

for folder in folders:
    input_folder_path = f'IPS/{folder}'
    output_folder_path = f'Results/{folder}'

    for file_name in os.listdir(input_folder_path):
        input_file_path = f'{input_folder_path}/{file_name}'
        file_base_name, _ = os.path.splitext(file_name)
        
        # Run script 1
        # output_file_path = f'{output_folder_path}/focsec/{file_base_name}.csv'
        # script1.script1(input_file_path, output_file_path)
        
        # Run script 2
        output_file_path = f'{output_folder_path}/httpbl/{file_base_name}.csv'
        script2.script2(input_file_path, output_file_path)
        
        # Run script 3
        output_file_path = f'{output_folder_path}/abuseipdb/{file_base_name}.csv'
        script3.script3(input_file_path, output_file_path)
        
        # Run script 4
        reference_file_path = '1.txt'
        output_file_path = f'{output_folder_path}/ipSum/{file_base_name}.csv'
        script4.script4(input_file_path, reference_file_path, output_file_path)
