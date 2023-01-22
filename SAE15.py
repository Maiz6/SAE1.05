import csv
import re

# Ouvrez un fichier en écriture avec l'encodage utf-8
with open('E:/SAE15/DumpFile.csv', 'w', encoding='utf-8') as csvfile:
    # Initialisez un écrivain CSV
    writer = csv.writer(csvfile)
    
    # Écrivez l'en-tête du fichier CSV
    writer.writerow(['Heure', 'Protocole', 'Source', 'Destination', 'Drapeaux TCP', 'Numéro de séquence', "Numéro d'accusé de réception", 'Taille de la fenêtre de réception', 'Longueur'])
    
    # Ouvrez le fichier en lecture
    with open('E:/SAE15/DumpFile.txt', 'r') as f:
        # Parcourez chaque ligne du fichier
        for line in f:
            
            if "IP" in line:
                destination = 0
                # Utilisez une expression régulière pour extraire les informations souhaitées
                time_match = re.search(r'(\d{2}:\d{2}:\d{2}\.\d{6})', line)
                protocol_match = re.search(r'(\w+):', line)
                source_match = re.search(r'([\w-]+\.[\w-]+\.[\w-]+\.[\w-]+\.[\w-]+) >', line) or re.search(r'([\w-]+\.[\w-]+\.[\w-]+\.[\w-]+) >', line) or re.search(r'([\w-]+\.[\w-]+) >', line) or re.search(r'(\d+\.\d+\.\d+\.\d+)  >', line)
                destination_match = re.search(r'([\w-]+\.[\w-]+\.[\w-]+\.[\w-]+):', line) or re.search(r'([\w-]+\.[\w-]+):', line) or re.search(r'(\d+\.\d+\.\d+\.\d+) :', line)
                flags_match = re.search(r'Flags \[(..)\]', line)
                sequence_match = re.search(r'seq (\d+):(\d+),', line)
                ack_match = re.search(r'ack (\d+),', line)
                window_match = re.search(r'win (\d+),', line)
                length_match = re.search(r'length (\d+)', line)

                # Vérifiez si une correspondance a été trouvée pour chaque information
                if time_match:
                    time = time_match.group(1)
                if protocol_match:
                    protocol = protocol_match.group(1)
                if source_match:
                    source = source_match.group(1)
                if destination_match:
                    destination = destination_match.group(1)
                if flags_match:
                    flags = flags_match.group(1)
                if sequence_match:
                    sequence = sequence_match.group(1)
                if ack_match:
                    ack = ack_match.group(1)
                if window_match:
                    window = window_match.group(1)
                if length_match:
                    length = length_match.group(1)
                
                # Écrivez les informations extraites dans le fichier CSV
                writer.writerow([time, protocol, source, destination, flags, sequence, ack, window, length])

