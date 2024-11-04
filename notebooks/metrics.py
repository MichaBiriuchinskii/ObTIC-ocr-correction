import pandas as pd
import Levenshtein
from Levenshtein import distance
from tqdm.auto import tqdm
import nltk
nltk.download('punkt') 
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

def levenshtein_distance(ref, hyp, show_progress=False):
    """Calculate the Levenshtein distance and Character Error Rate"""
    pairs = zip(ref, hyp)
    if show_progress:
        pairs = tqdm(pairs, total=len(ref))
    
    distances = [distance(r, h) for r, h in pairs]

    results = pd.DataFrame({
        "reference": ref,
        "hypothesis": hyp,
        "distance": distances
    })
    
    results["cer"] = results.apply(lambda row: 100 * row["distance"] / max(len(row["reference"]), 1), axis=1)
    
    return results

def calculate_wer(ref, hyp):
    """Calculate Word Error Rate (WER) for given reference and hypothesis lists."""
    results = []
    
    for reference_text, hypothesis_text in zip(ref, hyp):
        reference_words = word_tokenize(reference_text,language='french')
        hypothesis_words = word_tokenize(hypothesis_text,language='french')

        if len(reference_words) == 0:
            wer = 1.0  # 100% error
        else:
            distance = Levenshtein.distance(' '.join(reference_words), ' '.join(hypothesis_words))

            wer = distance / len(reference_words)

        results.append({
            "reference": reference_text,
            "hypothesis": hypothesis_text,
            "wer": wer * 100  # Convert to percentage
        })
    
    df_results = pd.DataFrame(results)
    return df_results