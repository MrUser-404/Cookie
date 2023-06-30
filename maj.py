import subprocess

repo_path = 'Test.py'

# Exécute la commande "git pull" dans le répertoire spécifié
subprocess.run(['git', '-C', repo_path, 'pull'])


