import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples['has_start'] = 0
    samples['has_stop'] = 0
    samples['has_atat'] = 0
    samples['has_ggg'] = 0

    samples.loc[samples['dna_sequence'].str.startswith('ATG'),'has_start'] = 1
    samples.loc[(samples['dna_sequence'].str.endswith('TAA'))|(samples['dna_sequence'].str.endswith('TAG'))|(samples['dna_sequence'].str.endswith('TGA')),'has_stop'] = 1
    samples.loc[samples['dna_sequence'].str.contains('ATAT'),'has_atat'] = 1
    samples.loc[samples['dna_sequence'].str.contains('GGG'),'has_ggg'] = 1

    return samples.sort_values('sample_id')