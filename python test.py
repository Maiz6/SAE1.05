import re
from datetime import datetime

# Ouvrez le fichier en mode lecture
with open('/Users/admin/Documents/evenement_15GroupeA1.ics', 'r') as f:
  # Lisez le contenu du fichier
  content = f.read()

# Utilisez une expression régulière pour extraire le sujet de l'événement
subject_regex = r'SUMMARY:(.*)'
subject_match = re.search(subject_regex, content)
subject = subject_match.group(1)

# Utilisez une expression régulière pour extraire la date de début de l'événement
start_date_regex = r'DTSTART:(.*)'
start_date_match = re.search(start_date_regex, content)
start_date = start_date_match.group(1)

start_date_formatted = datetime.strptime(start_date, '%Y%m%dT%H%M%SZ').strftime('%d/%m/%Y')

end_date_regex = r'DTEND:(.*)'
end_date_match = re.search(end_date_regex, content)
end_date = end_date_match.group(1)

end_date_formatted = datetime.strptime(end_date, '%Y%m%dT%H%M%SZ').strftime('%d/%m/%Y')

# Construisez la chaîne de caractères CSV en utilisant les informations extraites
csv_string = f'"{subject}","{start_date_formatted}","{end_date_formatted}"'

# Affichez la chaîne de caractères CSV
print(csv_string)