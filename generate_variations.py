from itertools import product as itertools_product
from models.variation import Variation

def generate_variations(product_id, attributes):
    attr_values = [values for values in attributes.values()]
    variations = []
    
    for combination in itertools_product(*attr_values):
        variation = Variation(product_id, combination)
        variations.append(variation)
    
    return variations
