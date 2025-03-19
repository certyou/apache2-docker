import re
import pandas as pd
import matplotlib.pyplot as plt

# Expression régulière pour extraire les champs des logs Apache
LOG_PATTERN = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<method>\w+) (?P<url>.*?) (?P<protocol>HTTP/\d\.\d)" (?P<status>\d+) (?P<size>\d+)'

def parse_log_line(line):
    match = re.match(LOG_PATTERN, line)
    if match:
        return match.groupdict()
    return None

def parse_log_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        logs = [parse_log_line(line) for line in file]
    return [log for log in logs if log]

def analyze_logs(logs):
    print(logs)
    df = pd.DataFrame(logs)
    df['errors'] = df['status'].astype(int)
    df['status'] = df['status'][0]
    
    # Compter les occurrences de chaque code de statut HTTP
    status_counts = df['status'].value_counts()
    
    # Affichage des statistiques
    print("Statistiques des codes HTTP:")
    print(status_counts)
    
    # Visualisation des statuts HTTP
    plt.figure(figsize=(8, 5))
    status_counts.plot(kind='bar', color='skyblue')
    plt.title("Répartition des codes HTTP")
    plt.xlabel("Code HTTP")
    plt.ylabel("Nombre de requêtes")
    plt.xticks(rotation=0)
    plt.savefig("http_status_distribution.png")
    plt.show()

if __name__ == "__main__":
    log_file = "/var/log/apache2/access.log"  # Remplace avec ton fichier de logs
    logs = parse_log_file(log_file)
    analyze_logs(logs)