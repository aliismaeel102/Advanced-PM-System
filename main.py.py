import os

def get_risk_level(score):
    if score >= 20: return "CRITICAL"
    if score >= 12: return "HIGH"
    if score >= 6: return "MEDIUM"
    return "LOW"

def calculate_npv(initial_cost, cash_flows, rate):
    npv = -initial_cost
    for t, cash in enumerate(cash_flows, 1):
        npv += cash / ((1 + rate) ** t)
    return round(npv, 2)

def generate_report(name, risk_data, finance_data, resource_data):
    filename = f"{name}_Project_Report.txt"
    with open(filename, "w") as f:
        f.write(f"PROJECT MANAGEMENT REPORT: {name}\n")
        f.write("Prepared by: Ali Ismail Ali Bayoumi Mohamed\n")
        f.write("="*40 + "\n\n")
        
        f.write("1. RISK ANALYSIS\n")
        for r in risk_data:
            f.write(f"- {r['desc']}: Score {r['score']} ({r['level']})\n")
        
        f.write("\n2. FINANCIAL ANALYSIS\n")
        f.write(f"- Total Investment: ${finance_data['inv']}\n")
        f.write(f"- Calculated NPV: ${finance_data['npv']}\n")
        f.write(f"- ROI: {finance_data['roi']}%\n")
        
        f.write("\n3. RESOURCE ALLOCATION\n")
        for res, amount in resource_data.items():
            f.write(f"- {res}: ${amount}\n")
            
    print(f"\nReport generated successfully: {filename}")

def main():
    print("--- ADVANCED PROJECT MANAGEMENT SYSTEM ---")
    print("Student: Ali Ismail Ali Bayoumi Mohamed | Dept: IS\n")

    p_name = input("Enter Project Name: ")
    
    # Risk Section
    risks = []
    print("\n[Section 1: Risk Assessment]")
    for i in range(3):
        desc = input(f"Enter Risk {i+1} Description: ")
        prob = int(input("Probability (1-5): "))
        imp = int(input("Impact (1-5): "))
        score = prob * imp
        risks.append({'desc': desc, 'score': score, 'level': get_risk_level(score)})

    # Finance Section
    print("\n[Section 2: Financial Planning]")
    inv = float(input("Initial Investment Cost: "))
    annual_rev = float(input("Expected Annual Revenue: "))
    years = int(input("Project Duration (Years): "))
    
    c_flows = [annual_rev] * years
    npv_val = calculate_npv(inv, c_flows, 0.1)
    roi_val = round(((annual_rev * years) - inv) / inv * 100, 2)
    finance = {'inv': inv, 'npv': npv_val, 'roi': roi_val}

    # Resources Section
    print("\n[Section 3: Resource Budgeting]")
    res_data = {
        "Human Resources": float(input("Budget for Staff: ")),
        "Equipment/Tech": float(input("Budget for Hardware: ")),
        "Marketing": float(input("Budget for Marketing: "))
    }

    generate_report(p_name, risks, finance, res_data)

if __name__ == "__main__":
    main()