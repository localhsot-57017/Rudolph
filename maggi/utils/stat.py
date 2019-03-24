import subprocess
import json

def statistics(containerid):
    print("gathering stats ...")
    stats = subprocess.run(["docker", "stats", containerid, "--no-stream"],
                   stdout=subprocess.PIPE)

    print(set(str(stats.stdout).strip().split(" ")))

# statistics("instantbox_managed_fJd5HD2eizTuL0yS")