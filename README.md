# CTBench_LLM
This repository contains the CT-Repo and CT-Pub datasets and demo codes to run the benchmark. 

[![DOI](https://zenodo.org/badge/806204687.svg)](https://zenodo.org/doi/10.5281/zenodo.11604074)

# Steps to run 
1. Create a separate virtual environment in Python3. Let's name it 'my_venv'.
```
python3 -m venv my_venv
```
Then activate the virtual environment - 
```
source my_venv/bin/activate
```
2. Install the requirements from requirements.txt
```
pip3 install -r requirements.txt 
```
3. Run the [Demo Scripts](demo_scripts.ipynb) notebook to explore example Generation (zero/three shot) and Evaluation with GPT-4o codes. Also run the [BERT Score Calculate](BERT_Score_Calculate.ipynb) notebook to explore the BERT Score evaluations at different thresholds.

# Data (Version 1.0)
1. [CT-Pub Dataset (including 3 examples for three-shot setting) - 103 Trials](data/CT-Pub-With-Examples.csv)
2. [CT-Repo Dataset (including 3 examples for three-shot setting) without any pre-processing - 1798 Trials](data/CT-Repo-With-Examples-Full-Version.csv)
3. [CT-Repo Dataset (including 3 examples for three-shot setting) after pre-processing - 1693 Trials](data/CT-Repo-With-Examples-Processed-Version.csv)

# Metadata (Croissant Format) of CT-Pub Dataset
```
{
  "@type": "sc:Dataset",
  "name": "CT-Pub Dataset",
  "description": "This dataset includes clinical trial metadata with additional manually annotated baseline features from related publications. Each instance represents a clinical trial study and contains textual information such as the title, brief summary, conditions, interventions, primary outcome, eligibility criteria, and baseline features collected from the API and publications.",
  "license": "CC0-1.0 license",
  "url": "https://github.com/nafis-neehal/CTBench_LLM",
  "distribution": [
    {
      "@type": "cr:FileObject",
      "@id": "CT-Pub-With-Examples.csv",
      "name": "CT-Pub-With-Examples.csv",
      "contentUrl": "data/CT-Pub-With-Examples.csv",
      "encodingFormat": "text/csv",
      "sha256": "your_file_hash_here"
    }
  ],
  "recordSet": [
    {
      "@type": "cr:RecordSet",
      "name": "Clinical Trial Data",
      "description": "Records from clinical trials, with their schema.",
      "field": [
         {
          "@type": "cr:Field",
          "name": "NCTId",
          "description": "Unique ID of the clinical Trial",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples.csv" },
            "extract": {
              "column": "NCTId"
            }
          }
        }
        {
          "@type": "cr:Field",
          "name": "BriefTitle",
          "description": "The title of the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples.csv" },
            "extract": {
              "column": "BriefTitle"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "BriefSummary",
          "description": "A brief summary of the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples.csv" },
            "extract": {
              "column": "BriefSummary"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "Conditions",
          "description": "The conditions being studied in the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples.csv" },
            "extract": {
              "column": "Conditions"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "Interventions",
          "description": "The interventions used in the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples.csv" },
            "extract": {
              "column": "Interventions"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "PrimaryOutcomes",
          "description": "The primary outcome(s) of the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples.csv" },
            "extract": {
              "column": "PrimaryOutcomes"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "EligibilityCriteria",
          "description": "The eligibility criteria for participants in the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples.csv" },
            "extract": {
              "column": "EligibilityCriteria"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "BaselineMeasures",
          "description": "Baseline features collected from the API.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples.csv" },
            "extract": {
              "column": "BaselineMeasures"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "Paper_BaselineMeasures",
          "description": "Baseline features manually collected from related publications.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples.csv" },
            "extract": {
              "column": "Paper_BaselineMeasures"
            }
          }
        }
      ]
    }
  ]
}

```

# Metadata (Croissant Format) of CT-Repo Dataset
```
{
  "@type": "sc:Dataset",
  "name": "CT-Repo Dataset",
  "description": "This dataset includes clinical trial metadata and corresponding baseline features. Each instance represents a clinical trial study and contains textual information such as the title, brief summary, conditions, interventions, primary outcome, eligibility criteria, and baseline features collected from the clinicaltrials.gov API.",
  "license": "CC0-1.0 license",
  "url": "https://github.com/nafis-neehal/CTBench_LLM",
  "distribution": [
    {
      "@type": "cr:FileObject",
      "@id": "CT-Repo-With-Examples-Processed-Version.csv",
      "name": "CT-Repo-With-Examples-Processed-Version.csv",
      "contentUrl": "data/CT-Repo-With-Examples-Processed-Version.csv",
      "encodingFormat": "text/csv",
      "sha256": "your_file_hash_here"
    }
  ],
  "recordSet": [
    {
      "@type": "cr:RecordSet",
      "name": "Clinical Trial Data",
      "description": "Records from clinical trials, with their schema.",
      "field": [
         {
          "@type": "cr:Field",
          "name": "NCTId",
          "description": "Unique ID of the clinical Trial",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version.csv" },
            "extract": {
              "column": "NCTId"
            }
          }
        }
        {
          "@type": "cr:Field",
          "name": "BriefTitle",
          "description": "The title of the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version.csv" },
            "extract": {
              "column": "BriefTitle"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "BriefSummary",
          "description": "A brief summary of the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version.csv" },
            "extract": {
              "column": "BriefSummary"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "Conditions",
          "description": "The conditions being studied in the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version.csv" },
            "extract": {
              "column": "Conditions"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "Interventions",
          "description": "The interventions used in the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version.csv" },
            "extract": {
              "column": "Interventions"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "PrimaryOutcomes",
          "description": "The primary outcome(s) of the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version.csv" },
            "extract": {
              "column": "PrimaryOutcomes"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "EligibilityCriteria",
          "description": "The eligibility criteria for participants in the clinical trial.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version.csv" },
            "extract": {
              "column": "EligibilityCriteria"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "BaselineMeasures",
          "description": "Baseline features collected from the API.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version.csv" },
            "extract": {
              "column": "BaselineMeasures"
            }
          }
        }
      ]
    }
  ]
}

```



