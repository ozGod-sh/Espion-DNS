# 📡 Espion-DNS - Outil de Reconnaissance DNS

**Créé par ozGod-sh**

## Description

Espion-DNS est un outil de reconnaissance et d'énumération DNS qui permet d'analyser les enregistrements DNS d'un domaine. Il récupère automatiquement tous les types d'enregistrements courants et présente les informations de manière structurée pour l'analyse de sécurité et la reconnaissance passive.

## Fonctionnalités

### 🔍 Énumération DNS complète
- **Enregistrements A** : Adresses IPv4
- **Enregistrements AAAA** : Adresses IPv6
- **Enregistrements MX** : Serveurs de messagerie
- **Enregistrements TXT** : Informations textuelles (SPF, DKIM, etc.)
- **Enregistrements NS** : Serveurs de noms
- **Enregistrements CNAME** : Alias de domaine
- **Enregistrements SOA** : Autorité de zone

### 🎯 Modes de requête
- **Requête spécifique** : Un seul type d'enregistrement
- **Énumération complète** : Tous les types d'enregistrements
- **Gestion d'erreurs** : Traitement des domaines inexistants
- **Formatage lisible** : Présentation claire des résultats

## Installation

### Prérequis
- Python 3.6+
- pip (gestionnaire de paquets Python)

### Installation des dépendances
```bash
cd Espion-DNS
pip install -r requirements.txt
```

### Dépendances
- `dnspython` : Bibliothèque DNS pour Python

## Utilisation

### Syntaxe de base
```bash
python espion_dns.py <DOMAINE> [OPTIONS]
```

### Options disponibles
- `-t, --type TYPE` : Type d'enregistrement à requêter (A, MX, TXT, etc.) ou 'ALL' pour tous (défaut: ALL)
- `-h, --help` : Affiche l'aide

### Exemples d'utilisation

#### 1. Énumération complète
```bash
python espion_dns.py example.com
```

#### 2. Enregistrements A uniquement
```bash
python espion_dns.py example.com -t A
```

#### 3. Serveurs de messagerie
```bash
python espion_dns.py example.com --type MX
```

#### 4. Enregistrements TXT (SPF, DKIM)
```bash
python espion_dns.py example.com -t TXT
```

## Structure des fichiers

```
Espion-DNS/
├── espion_dns.py       # Script principal
├── requirements.txt    # Dépendances Python
└── README.md          # Cette documentation
```

## Logique de fonctionnement

### 1. Configuration du resolver
```python
resolver = dns.resolver.Resolver()
answers = resolver.resolve(domain, record_type)
```

### 2. Traitement des réponses
```python
for rdata in answers:
    print(f"  {rdata.to_text()}")
```

### 3. Gestion des erreurs
```python
except dns.resolver.NoAnswer:
    print("Aucun enregistrement de ce type trouvé.")
except dns.resolver.NXDOMAIN:
    print("Le domaine n'existe pas.")
```

## Cas d'usage

### Reconnaissance passive
- **Cartographie réseau** : Identifier les serveurs et services
- **Collecte d'informations** : Rassembler des données sur la cible
- **Analyse d'infrastructure** : Comprendre l'architecture réseau
- **OSINT** : Intelligence open source

### Tests de pénétration
- **Phase de reconnaissance** : Première étape d'un pentest
- **Identification de cibles** : Trouver des serveurs intéressants
- **Analyse de surface d'attaque** : Cartographier les points d'entrée
- **Validation de scope** : Vérifier les domaines dans le périmètre

### Administration système
- **Diagnostic DNS** : Vérifier la configuration DNS
- **Migration de domaine** : Valider les enregistrements
- **Monitoring** : Surveiller les changements DNS
- **Documentation** : Inventaire des enregistrements

## Exemple de sortie

### Énumération complète
```
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  📡 Espion-DNS v1.0.0                                    ║
║                                                              ║
║  Outil de reconnaissance et d'énumération DNS.              ║
║  Créé par ozGod                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝

[*] Analyse du domaine : example.com

--- Enregistrements A pour example.com ---
  93.184.216.34

--- Enregistrements AAAA pour example.com ---
  2606:2800:220:1:248:1893:25c8:1946

--- Enregistrements MX pour example.com ---
  0 .

--- Enregistrements TXT pour example.com ---
  "v=spf1 -all"

--- Enregistrements NS pour example.com ---
  a.iana-servers.net.
  b.iana-servers.net.

--- Enregistrements CNAME pour example.com ---
  Aucun enregistrement de ce type trouvé.

--- Enregistrements SOA pour example.com ---
  sns.dns.icann.org. noc.dns.icann.org. 2022091025 7200 3600 1209600 3600
```

### Requête spécifique (MX)
```
[*] Analyse du domaine : gmail.com

--- Enregistrements MX pour gmail.com ---
  5 gmail-smtp-in.l.google.com.
  10 alt1.gmail-smtp-in.l.google.com.
  20 alt2.gmail-smtp-in.l.google.com.
  30 alt3.gmail-smtp-in.l.google.com.
  40 alt4.gmail-smtp-in.l.google.com.
```

## Types d'enregistrements DNS

### A (Address)
- **Fonction** : Associe un nom de domaine à une adresse IPv4
- **Format** : `example.com. 300 IN A 93.184.216.34`
- **Usage** : Résolution de nom vers IP

### AAAA (IPv6 Address)
- **Fonction** : Associe un nom de domaine à une adresse IPv6
- **Format** : `example.com. 300 IN AAAA 2606:2800:220:1:248:1893:25c8:1946`
- **Usage** : Résolution IPv6

### MX (Mail Exchange)
- **Fonction** : Spécifie les serveurs de messagerie
- **Format** : `example.com. 300 IN MX 10 mail.example.com.`
- **Usage** : Routage des emails

### TXT (Text)
- **Fonction** : Stocke des informations textuelles
- **Exemples** : SPF, DKIM, DMARC, vérification de domaine
- **Usage** : Configuration de sécurité email, vérifications

### NS (Name Server)
- **Fonction** : Spécifie les serveurs DNS autoritaires
- **Format** : `example.com. 300 IN NS ns1.example.com.`
- **Usage** : Délégation DNS

### CNAME (Canonical Name)
- **Fonction** : Alias vers un autre nom de domaine
- **Format** : `www.example.com. 300 IN CNAME example.com.`
- **Usage** : Redirection de domaine

### SOA (Start of Authority)
- **Fonction** : Informations sur la zone DNS
- **Contenu** : Serveur primaire, email admin, numéros de série
- **Usage** : Gestion de zone DNS

## Informations extraites

### Enregistrements TXT intéressants
```bash
# SPF (Sender Policy Framework)
"v=spf1 include:_spf.google.com ~all"

# DKIM (DomainKeys Identified Mail)
"v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC..."

# DMARC (Domain-based Message Authentication)
"v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com"

# Vérification de domaine
"google-site-verification=abc123def456"
```

### Analyse des serveurs MX
```python
# Priorité des serveurs mail (plus bas = priorité plus haute)
5 primary-mail.example.com.     # Serveur principal
10 backup-mail.example.com.     # Serveur de sauvegarde
20 fallback-mail.example.com.   # Serveur de secours
```

## Intégration avec d'autres outils

### Avec des outils de reconnaissance
```bash
#!/bin/bash
# Pipeline de reconnaissance
echo "=== Reconnaissance DNS ==="
python espion_dns.py target.com

echo "=== Sous-domaines ==="
subfinder -d target.com

echo "=== Ports ouverts ==="
nmap -sS target.com
```

### Scripts d'automatisation
```python
import subprocess

def dns_recon(domain):
    result = subprocess.run(['python', 'espion_dns.py', domain], 
                          capture_output=True, text=True)
    return result.stdout

# Analyser plusieurs domaines
domains = ['example.com', 'test.com', 'target.com']
for domain in domains:
    print(f"=== {domain} ===")
    print(dns_recon(domain))
```

### Export des résultats
```bash
# Sauvegarder les résultats
python espion_dns.py target.com > dns_recon_target.txt

# Format JSON (extension possible)
python espion_dns.py target.com --format json > dns_recon.json
```

## Techniques avancées

### Résolution inverse
```python
import socket
def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Pas de PTR"
```

### Transfert de zone
```python
def zone_transfer(domain, nameserver):
    try:
        zone = dns.zone.from_xfr(dns.query.xfr(nameserver, domain))
        return zone
    except:
        return None
```

### Brute force de sous-domaines
```python
subdomains = ['www', 'mail', 'ftp', 'admin', 'test']
for sub in subdomains:
    try:
        answers = resolver.resolve(f"{sub}.{domain}", 'A')
        print(f"{sub}.{domain} -> {answers[0]}")
    except:
        pass
```

## Limitations

### Techniques
- **Pas de brute force** : Ne découvre pas les sous-domaines cachés
- **Pas de transfert de zone** : Ne tente pas les transferts DNS
- **Résolution simple** : Utilise les serveurs DNS par défaut
- **Pas de cache** : Pas de stockage des résultats

### Réseau
- **Serveurs DNS** : Dépend de la configuration DNS locale
- **Filtrage** : Peut être bloqué par des firewalls
- **Rate limiting** : Limites des serveurs DNS
- **Timeout** : Peut échouer sur des serveurs lents

## Améliorations futures

### Fonctionnalités avancées
- Brute force de sous-domaines intégré
- Tentative de transfert de zone
- Résolution inverse automatique
- Détection de wildcard DNS

### Interface et export
- Export en JSON/XML/CSV
- Interface graphique
- Mode interactif
- Rapports HTML

### Performance
- Requêtes parallèles
- Cache des résultats
- Configuration de serveurs DNS personnalisés
- Retry automatique

## Contre-mesures (pour les administrateurs)

### Protection DNS
- **Transfert de zone** : Restreindre aux serveurs autorisés
- **Rate limiting** : Limiter les requêtes par IP
- **Monitoring** : Surveiller les requêtes suspectes
- **Filtrage** : Bloquer les requêtes malveillantes

### Bonnes pratiques
- **Minimiser l'exposition** : Limiter les enregistrements publics
- **Validation** : Vérifier régulièrement la configuration
- **Sécurité** : Utiliser DNSSEC si possible
- **Monitoring** : Alertes sur les changements DNS

## Outils complémentaires

### Reconnaissance DNS
- **dig** : Outil de requête DNS standard
- **nslookup** : Utilitaire de résolution DNS
- **host** : Commande de lookup DNS
- **fierce** : Brute force de sous-domaines

### Outils avancés
- **dnsrecon** : Reconnaissance DNS complète
- **sublist3r** : Énumération de sous-domaines
- **amass** : Cartographie de surface d'attaque
- **subfinder** : Découverte de sous-domaines

## Sécurité et éthique

⚠️ **Utilisation responsable uniquement**
- Utilisez uniquement sur vos propres domaines ou avec autorisation
- Respectez les politiques des serveurs DNS
- Ne pas surcharger les serveurs avec trop de requêtes
- Utilisez pour améliorer la sécurité, pas pour nuire

## Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

---

**Espion-DNS v1.0.0** | Créé par ozGod-sh