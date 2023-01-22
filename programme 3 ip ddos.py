import csv
import matplotlib.pyplot as plt

# Seuils de connexion
CONNECTION_THRESHOLD = 1000
IP_THRESHOLD = 50

# Initialisation du dictionnaire pour stocker les comptes d'IP
ip_count = {}

# Ouverture du fichier CSV
with open('E:/SAE15/DumpFile.csv', 'r') as csvfile:
    # Initialisation d'un lecteur CSV
    reader = csv.DictReader(csvfile)
    
    # Boucle sur les lignes du fichier CSV
    for row in reader:
        # Extraction de l'IP source
        source_ip = row['Source']
        
        # Vérifie si l'IP existe déjà dans le dictionnaire
        if source_ip in ip_count:
            # Si oui, incrémente le compteur
            ip_count[source_ip] += 1
        else:
            # Si non, l'ajoute au dictionnaire avec un compteur à 1
            ip_count[source_ip] = 1

# Initialisation de la variable pour stocker le compte total de connexion
connection_count = 0
# Boucle sur les comptes d'IP
for ip, count in ip_count.items():
    # Incrémente le compteur total de connexion
    connection_count += count
    
    # Vérifie si le compte d'IP a dépassé le seuil
    if count > IP_THRESHOLD:
        print(f"Attaque DDOS possible de l'IP: {ip} avec {count} connexions")

# Vérifie si le compte total de connexion a dépassé le seuil
if connection_count > CONNECTION_THRESHOLD:
    print(f"Attaque DDOS possible avec {connection_count} connexions totales")
else:
    print("Aucune attaque DDOS détectée")

# Trie les adresses IP par ordre décroissant de compte de connexion
sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)

# Extrait les 5 premières adresses IP
top_3_ips = [ip for ip, count in sorted_ips[:3]]
top_3_counts = [count for ip, count in sorted_ips[:3]]

# Création d'un diagramme à barres des comptes de connexion par IP
plt.bar(top_3_ips, top_3_counts)
plt.xlabel('IP source')
plt.ylabel('Compte de connexion')
plt.title('5 IP sources les plus utilisées')
plt.show()

