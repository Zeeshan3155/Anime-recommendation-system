import json
import numpy as np
import pandas as pd

__sig = None
indices = None
df_anime = None

def load_artifacts():
    global __sig
    global indices
    global df_anime

    __sig = np.load(r"./artifacts/sig.npy")
    with open(r"./artifacts/index.json") as fp:
        indices = json.load(fp)

    df_anime = pd.read_csv(r"./artifacts/anime.csv")

def get_recommendation(title, top_n):
    title = title.lower()
    try :
        anime_id = indices[title]
    except:
        return "<h2>Wrong name</h2>"
    sig_score = list(enumerate(__sig[anime_id]))
    top10_sig_score = sorted(sig_score, key=lambda x:x[1], reverse=True)[1:top_n+1]
    top10_indices = [x[0] for x in top10_sig_score]
    df1 = pd.DataFrame({"Anime_name": df_anime['name'].iloc[top10_indices].values,
                        'Rating': df_anime['rating'].iloc[top10_indices].values })
    return df1.to_html()
