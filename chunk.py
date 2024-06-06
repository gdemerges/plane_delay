import pandas as pd

# Chemin du fichier CSV
fichier_csv = 'data_cleaned.csv'

# Taille de l'échantillon souhaité
sample_size = 100000

# Lire le fichier CSV par morceaux
chunk_size = 10000  # Taille du chunk
chunks = pd.read_csv(fichier_csv, chunksize=chunk_size)

# Initialiser un DataFrame pour stocker l'échantillon
sampled_df = pd.DataFrame()

# Lire et ajouter des morceaux jusqu'à atteindre la taille de l'échantillon
for chunk in chunks:
    if len(sampled_df) < sample_size:
        sampled_df = pd.concat([sampled_df, chunk], ignore_index=True)
        if len(sampled_df) > sample_size:
            sampled_df = sampled_df.sample(n=sample_size, random_state=42)
            break
    else:
        break

# Sauvegarder l'échantillon dans un nouveau fichier CSV
sampled_df.to_csv('sampled_data.csv', index=False)

print(f"Échantillon de {sample_size} lignes sauvegardé dans 'sampled_data.csv'.")
