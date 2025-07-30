# -*- coding: utf-8 -*-
# Auteur: ozGod

import argparse
import dns.resolver
import sys

def display_banner():
    """Affiche une bannière stylisée pour l'outil."""
    VERSION = "1.0.0"
    AUTHOR = "ozGod"
    banner = f"""
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  📡 Espion-DNS v{VERSION}                                    ║
║                                                              ║
║  Outil de reconnaissance et d'énumération DNS.              ║
║  Créé par {AUTHOR}                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)

def query_dns(domain, record_type):
    """Effectue une requête DNS pour un type d'enregistrement donné."""
    try:
        resolver = dns.resolver.Resolver()
        answers = resolver.resolve(domain, record_type)
        print(f"\n--- Enregistrements {record_type} pour {domain} ---")
        if answers:
            for rdata in answers:
                print(f"  {rdata.to_text()}")
        else:
            print("  Aucun enregistrement trouvé.")
        return True
    except dns.resolver.NoAnswer:
        print(f"\n--- Enregistrements {record_type} pour {domain} ---")
        print("  Aucun enregistrement de ce type trouvé.")
    except dns.resolver.NXDOMAIN:
        print(f"[!] Erreur: Le domaine '{domain}' n'existe pas.", file=sys.stderr)
        return False # Arrête le scan si le domaine n'existe pas
    except Exception as e:
        print(f"[!] Une erreur est survenue lors de la requête {record_type}: {e}", file=sys.stderr)
    return True

def main():
    display_banner()
    parser = argparse.ArgumentParser(
        description="Effectue des requêtes DNS pour énumérer les enregistrements d'un domaine.",
        epilog=f"Créé par ozGod."
    )
    parser.add_argument("domain", help="Le domaine à analyser (ex: exemple.com).")
    parser.add_argument("-t", "--type", help="Type d'enregistrement à requêter (ex: A, MX, TXT). 'ALL' pour tous.", default='ALL')

    args = parser.parse_args()

    record_types_to_query = []
    all_types = ['A', 'AAAA', 'MX', 'TXT', 'NS', 'CNAME', 'SOA']

    if args.type.upper() == 'ALL':
        record_types_to_query = all_types
    elif args.type.upper() in all_types:
        record_types_to_query.append(args.type.upper())
    else:
        print(f"[!] Erreur: Type d'enregistrement '{args.type}' non supporté.", file=sys.stderr)
        print(f"    Types supportés: {', '.join(all_types)} ou 'ALL'", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Analyse du domaine : {args.domain}\n")

    for record_type in record_types_to_query:
        if not query_dns(args.domain, record_type):
            # Arrête tout si le domaine n'existe pas
            break

if __name__ == "__main__":
    main()
