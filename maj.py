import subprocess

def git_pull():
    try:
        subprocess.check_call(['git', 'pull'])
        print("Les modifications ont été récupérées et fusionnées avec succès.")
    except subprocess.CalledProcessError as e:
        print("Une erreur s'est produite lors de l'exécution de 'git pull':", e)

# Exécution de la fonction git_pull
git_pull()
