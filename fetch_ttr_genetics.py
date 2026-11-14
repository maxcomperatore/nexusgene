import requests
import json

def fetch_ttr_genetics():
    query = """
    query targetDetails($ensemblId: String!) {
      target(ensemblId: $ensemblId) {
        id
        approvedSymbol
        approvedName
        biotype
        geneticConstraint {
          constraintType
          score
        }
        associatedDiseases(page: {size: 8, index: 0}) {
          count
          rows {
            disease {
              id
              name
            }
            score
          }
        }
      }
    }
    """
    variables = {"ensemblId": "ENSG00000118271"}
    r = requests.post("https://api.platform.opentargets.org/api/v4/graphql", json={"query": query, "variables": variables})
    if r.status_code == 200:
        with open("d:/crew/experiment/reitwave/nexusgene/opentargets_ttr_associations.json", "w") as f:
            json.dump(r.json(), f, indent=2)
        print("TTR OpenTargets data saved!")
        return r.json()
    else:
        print("Error:", r.status_code)
        return None

if __name__ == "__main__":
    fetch_ttr_genetics()
