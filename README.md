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
3. Running the Scripts
   1. Run the [Demo Scripts Single](demo_scripts_single_gen_eval.ipynb) and [Demo Scripts Batch](demo_scripts_batch_gen_eval.ipynb) notebook to explore example Generation (zero/three shot) and Evaluation with GPT-4o codes for a single example and for the whole batch of the data respectively. The batch script will generate two files (CT-Pub-With-Examples-Corrected-allgen.csv, CT-Pub-With-Examples-Corrected-allgpteval.csv). The first one contains generation responses from our models (GPT4o and Llama3.1) in both 0/3 shot setting. The second one contains matched responses for all 4 model/ICL settings evaluated by GPT4o. 
   2. For getting scores (precision, recall, f1) based on GPT4o evaluation, explore the [GPT 4 Scoring](demo_scripts_batch_scoring.ipynb) notebook. Use the CT-Pub-With-Examples-Corrected-allgpteval.csv file as input which was generated after 3.1.  
   3. Also run the [BERT Score Calculate](BERT_Score_Pipeline_CT_PUB.ipynb) notebook to explore the BERT Score evaluations at 0.7 threshold for CT_PUB data (use CT-Pub-With-Examples-Corrected-allgen.csv generated in step 3.1). This can be modified for CT_REPO data as well in same process. 

# Data (Version 1.0)
1. [CT-Pub Dataset (including 3 examples for three-shot setting) - 103 Trials](data_new/CT-Pub-With-Examples-Corrected.csv)
2. [CT-Repo Dataset (including 3 examples for three-shot setting) after pre-processing - 1693 Trials](data_new/CT-Repo-With-Examples-Processed-Version-Corrected.csv)

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
      "@id": "CT-Pub-With-Examples-Corrected.csv",
      "name": "CT-Pub-With-Examples-Corrected.csv",
      "contentUrl": "data_new/CT-Pub-With-Examples-Corrected.csv",
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
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
            "extract": {
              "column": "EligibilityCriteria"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "TrialGroup",
          "description": "The one of the big 5 trial categories",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
            "extract": {
              "column": "TrialGroup"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "API_BaselineMeasures",
          "description": "Baseline features collected from the API.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
            "extract": {
              "column": "API_BaselineMeasures"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "API_BaselineMeasures_Corrected",
          "description": "Baseline features collected from the API and then Processed/Cleaned.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
            "extract": {
              "column": "API_BaselineMeasures_Corrected"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "Paper_BaselineMeasures",
          "description": "Baseline features manually collected from related publications.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
            "extract": {
              "column": "Paper_BaselineMeasures"
            }
          }
        }
        {
          "@type": "cr:Field",
          "name": "Paper_BaselineMeasures_Corrected",
          "description": "Baseline features manually collected from related publications and cleaned/processed.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Pub-With-Examples-Corrected.csv" },
            "extract": {
              "column": "Paper_BaselineMeasures_Corrected"
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
      "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv",
      "name": "CT-Repo-With-Examples-Processed-Version-Corrected.csv",
      "contentUrl": "data/CT-Repo-With-Examples-Processed-Version-Corrected.csv",
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
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv" },
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
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv" },
            "extract": {
              "column": "EligibilityCriteria"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "TrialGroup",
          "description": "The one of the big 5 trial categories",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv" },
            "extract": {
              "column": "TrialGroup"
            }
          }
        },
        {
          "@type": "cr:Field",
          "name": "API_BaselineMeasures",
          "description": "Baseline features collected from the API.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv" },
            "extract": {
              "column": "API_BaselineMeasures"
            }
          }
        }
        {
          "@type": "cr:Field",
          "name": "API_BaselineMeasures_Corrected",
          "description": "Baseline features collected from the API and clean/processed.",
          "dataType": "sc:Text",
          "references": {
            "fileObject": { "@id": "CT-Repo-With-Examples-Processed-Version-Corrected.csv" },
            "extract": {
              "column": "API_BaselineMeasures_Corrected"
            }
          }
        }
      ]
    }
  ]
}

```



