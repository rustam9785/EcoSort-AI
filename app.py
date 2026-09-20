# EcoSort AI - Intelligent Waste Segregation System
# Developed for 1M1B AI for Sustainability Virtual Internship

import sys

def classify_waste(item_description):
    """
    Simulated AI Waste Classification Engine
    """
    item = item_description.lower().strip()
    
    recyclable = ['plastic bottle', 'cardboard', 'paper', 'glass bottle', 'aluminum can', 'metal container']
    wet_waste = ['food scraps', 'vegetable peel', 'fruit core', 'tea leaves', 'garden waste']
    e_waste = ['battery', 'old phone', 'charger', 'circuit board', 'electronic component']
    
    print("\n--- EcoSort AI Analysis Result ---")
    print(f"Input Item: {item_description}")
    
    if any(k in item for k in recyclable):
        return "Category: RECYCLABLE (Dry Waste)\nBin: BLUE BIN\nAction: Rinse and crush before recycling."
    elif any(k in item for k in wet_waste):
        return "Category: ORGANIC / WET WASTE\nBin: GREEN BIN\nAction: Suitable for composting."
    elif any(k in item for k in e_waste):
        return "Category: E-WASTE / HAZARDOUS\nBin: BLACK / E-WASTE BIN\nAction: Handover to authorized e-waste collector."
    else:
        return "Category: GENERAL RESIDUAL WASTE\nBin: BLACK BIN\nAction: Dispose in standard municipal waste collection."

if __name__ == "__main__":
    print("========================================")
    print("      EcoSort AI Waste Classifier       ")
    print("========================================")
    test_item = input("Enter waste item (e.g. plastic bottle, apple core, battery): ")
    if not test_item:
        test_item = "plastic bottle"
    result = classify_waste(test_item)
    print(result)