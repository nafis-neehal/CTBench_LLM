from openai import OpenAI 
import re

############################ generate message templete ##############################

#mistral template
def assistant_user_template(system_message, question):
    return [{"role": "assistant", 
             "content": system_message,
            "role": "user", 
            "content": question}]

#ask llama
def system_user_template(system_message, question):
    return [{"role": "system", "content": system_message},
            {"role": "user", "content": question}]

#ask phi, gemma, command-r
def user_template(system_message, question):
    return [{"role": "user", "content": system_message + question}]


############################ generate prompts ##############################

def build_gold_example_questions_from_row(data):
    ids = ['NCT00000620', 'NCT01483560', 'NCT04280783']
    examples = data[data['NCTId'].isin(ids)]
    question = ""
    for index, row in examples.iterrows():
      question += "##Question:\n"
      question += f"<Title> \n {row['BriefTitle']}\n"
      question += f"<Brief Summary> \n {row['BriefSummary']}\n"
      question += f"<Condition> \n {row['Conditions']}\n"
      question += f"<Eligibility Criteria> \n {row['EligibilityCriteria']}\n"
      question += f"<Intervention> \n {row['Interventions']}\n"
      question += f"<Outcome> \n {row['PrimaryOutcomes']}\n"
      question += "##Answer:\n"
      question += f"{row['Paper_BaselineMeasures']}\n\n"

    return question

def build_silver_example_questions_from_row(data):
    ids = ['NCT00000620', 'NCT01483560', 'NCT04280783']
    examples = data[data['NCTId'].isin(ids)]
    question = ""
    for index, row in examples.iterrows():
      question += "##Question:\n"
      question += f"<Title> \n {row['BriefTitle']}\n"
      question += f"<Brief Summary> \n {row['BriefSummary']}\n"
      question += f"<Condition> \n {row['Conditions']}\n"
      question += f"<Eligibility Criteria> \n {row['EligibilityCriteria']}\n"
      question += f"<Intervention> \n {row['Interventions']}\n"
      question += f"<Outcome> \n {row['PrimaryOutcomes']}\n"
      question += "##Answer:\n"
      question += f"{row['BaselineMeasures']}\n\n"

    return question

def build_example_questions_from_row(data, ref_col_name):
    ids = ['NCT00000620', 'NCT01483560', 'NCT04280783']
    examples = data[data['NCTId'].isin(ids)]
    question = ""
    for index, row in examples.iterrows():
      question += "##Question:\n"
      question += f"<Title> \n {row['BriefTitle']}\n"
      question += f"<Brief Summary> \n {row['BriefSummary']}\n"
      question += f"<Condition> \n {row['Conditions']}\n"
      question += f"<Eligibility Criteria> \n {row['EligibilityCriteria']}\n"
      question += f"<Intervention> \n {row['Interventions']}\n"
      question += f"<Outcome> \n {row['PrimaryOutcomes']}\n"
      question += "##Answer:\n"
      question += f"{row[ref_col_name]}\n\n"

    return question

def build_zeroshot_prompt(_, row):

    #prompt structure
    system_message = "You are a helpful assistant with experience in the clinical domain and clinical trial design. \
    You'll be asked queries related to clinical trials. These inquiries will be delineated by a '##Question' heading. \
    Inside these queries, expect to find comprehensive details about the clinical trial structured within specific subsections, \
    indicated by '<>' tags. These subsections include essential information such as the trial's title, brief summary, \
    condition under study, inclusion and exclusion criteria, intervention, and outcomes."

    #baseline measure defintion
    # system_message += "In answer to this question, return a list of probable baseline features (separated by commas) of the clinical trial. \
    # Baseline features are the set of baseline or demographic characteristics that are assessed at baseline and used in the analysis of the \
    # primary outcome measure(s) to characterize the study population and assess validity. Clinical trial-related publications typically \
    # include a table of baseline features assessed  by arm or comparison group and for the entire population of participants in the clinical trial."
    system_message += "In answer to this question, return a list of probable baseline features (each feature should be enclosed within a pair of backticks \
    and each feature should be separated by commas from other features) of the clinical trial. \
    Baseline features are the set of baseline or demographic characteristics that are assessed at baseline and used in the analysis of the \
    primary outcome measure(s) to characterize the study population and assess validity. Clinical trial-related publications typically \
    include a table of baseline features assessed  by arm or comparison group and for the entire population of participants in the clinical trial."

    #additional instructions
    system_message += "Do not give any additional explanations or use any tags or headers, only return the list of baseline features. "

    #divide row information to generatie the query
    title = row['BriefTitle']
    brief_summary = row['BriefSummary']
    condition = row['Conditions']
    eligibility_criteria = row['EligibilityCriteria']
    intervention = row['Interventions']
    outcome = row['PrimaryOutcomes']

    question = "##Question:\n"
    question += f"<Title> \n {title}\n"
    question += f"<Brief Summary> \n {brief_summary}\n"
    question += f"<Condition> \n {condition}\n"
    question += f"<Eligibility Criteria> \n {eligibility_criteria}\n"
    question += f"<Intervention> \n {intervention}\n"
    question += f"<Outcome> \n {outcome}\n"
    question += "##Answer:\n"

    return system_message, question


def build_three_shot_prompt(data, row, ref_col_name):
    #prompt structure
    system_message = "You are a helpful assistant with experience in the clinical domain and clinical trial design. \
    You'll be asked queries related to clinical trials. These inquiries will be delineated by a '##Question' heading. \
    Inside these queries, expect to find comprehensive details about the clinical trial structured within specific subsections, \
    indicated by '<>' tags. These subsections include essential information such as the trial's title, brief summary, \
    condition under study, inclusion and exclusion criteria, intervention, and outcomes."

    #baseline measure defintion
    # system_message += "In answer to this question, return a list of probable baseline features (separated by commas) of the clinical trial. \
    # Baseline features are the set of baseline or demographic characteristics that are assessed at baseline and used in the analysis of the \
    # primary outcome measure(s) to characterize the study population and assess validity. Clinical trial-related publications typically \
    # include a table of baseline features assessed  by arm or comparison group and for the entire population of participants in the clinical trial."
    system_message += "In answer to this question, return a list of probable baseline features (each feature should be enclosed within a pair of backticks \
    and each feature should be separated by commas from other features) of the clinical trial. \
    Baseline features are the set of baseline or demographic characteristics that are assessed at baseline and used in the analysis of the \
    primary outcome measure(s) to characterize the study population and assess validity. Clinical trial-related publications typically \
    include a table of baseline features assessed  by arm or comparison group and for the entire population of participants in the clinical trial."

    #additional instructions
    system_message += "You will be given three examples. In each example, the question is delineated by '##Question' heading and the corresponding answer is delineated by '##Answer' heading. \
    Follow a similar pattern when you generate answers. Do not give any additional explanations or use any tags or headings, only return the list of baseline features."

    #example = build_silver_example_questions_from_row(data)
    example = build_example_questions_from_row(data, ref_col_name)

    #divide row information to generatie the query
    title = row['BriefTitle']
    brief_summary = row['BriefSummary']
    condition = row['Conditions']
    eligibility_criteria = row['EligibilityCriteria']
    intervention = row['Interventions']
    outcome = row['PrimaryOutcomes']

    question = "##Question:\n"
    question += f"<Title> \n {title}\n"
    question += f"<Brief Summary> \n {brief_summary}\n"
    question += f"<Condition> \n {condition}\n"
    question += f"<Eligibility Criteria> \n {eligibility_criteria}\n"
    question += f"<Intervention> \n {intervention}\n"
    question += f"<Outcome> \n {outcome}\n"
    question += "##Answer:\n"

    return system_message, example + question

def build_gpt4_eval_prompt(reference, candidate, qstart):
    system = """
        You are an expert assistant in the medical domain and clinical trial design. You are provided with details of a clinical trial.
        Your task is to determine which candidate baseline features match any feature in a reference baseline feature list for that trial. 
        You need to consider the context and semantics while matching the features.

        For each candidate feature:

            1. Identify a matching reference feature based on similarity in context and semantics.
            2. Remember the matched pair.
            3. A reference feature can only be matched to one candidate feature and cannot be further considered for any consecutive matches.
            4. If there are multiple possible matches (i.e. one reference feature can be matched to multiple candidate features or vice versa), choose the most contextually similar one.
            5. Also keep track of which reference and candidate features remain unmatched.

        Once the matching is complete, provide the results in a JSON format as follows:
        {
        "matched_features": [
            ["<reference feature 1>", "<candidate feature 1>"],
            ["<reference feature 2>", "<candidate feature 2>"]
        ],
        "remaining_reference_features": [
            "<unmatched reference feature 1>",
            "<unmatched reference feature 2>"
        ],
        "remaining_candidate_features": [
            "<unmatched candidate feature 1>",
            "<unmatched candidate feature 2>"
        ]
        }
    """

    question = f"\n Here is the trial information: \n\n"
    question += f"{qstart}"

    question += f"\n\nHere is the list of reference features: \n\n"
    ir = 1
    for ref_item in reference:
        question += (
            f"{ir}. {ref_item}\n"
        )
        ir += 1


    question += f"\nCandidate features: \n\n"
    ic = 1
    for can_item in candidate:
        question += (
            f"{ic}. {can_item}\n"
        )
        ic += 1

    return system, question

def get_question_from_row(row):
    title = row['BriefTitle']
    brief_summary = row['BriefSummary']
    condition = row['Conditions']
    eligibility_criteria = row['EligibilityCriteria']
    intervention = row['Interventions']
    outcome = row['PrimaryOutcomes']

    question = ""
    question += f"<Title> \n {title}\n"
    question += f"<Brief Summary> \n {brief_summary}\n"
    question += f"<Condition> \n {condition}\n"
    question += f"<Eligibility Criteria> \n {eligibility_criteria}\n"
    question += f"<Intervention> \n {intervention}\n"
    question += f"<Outcome> \n {outcome}\n"

    return question


############################ generation scripts ##############################

def run_generation_single_hf_models(message, hf_url, huggingface_token, temperature=0.0):

    base_url = "https://api-inference.huggingface.co/models/" 

    client = OpenAI(
        base_url=base_url + hf_url + "/v1/",
        api_key =huggingface_token 
    )

    chat_completion = client.chat.completions.create(
        model="tgi",
        messages=message,
        seed = 42,
        temperature=temperature,
        stream=False,
        max_tokens=1000
    )
    return chat_completion.choices[0].message.content

def run_generation_single_openai(message, model_name, openai_token, temperature=0.0):

    client = OpenAI(
        api_key=openai_token
    )

    response = client.chat.completions.create(
      model=model_name,
      messages=message,
      seed = 42,
      temperature=temperature,
      stream=False,
      max_tokens=1000
    )
    return response.choices[0].message.content

############################ evaluation scripts ##############################

def extract_elements(text):

    # Remove the '##Answer:' tag from some responses at the beginning
    text = text.replace("##Answer:", "").strip()

    # Regex pattern to correctly handle nested commas within parentheses
    # This pattern matches non-parenthetical text or text within balanced parentheses
    # Example: "a, b, (c, d), e" -> ['a', 'b', '(c, d)', 'e']
    pattern = r'\([^()]*\)|[^,]+'

    # Use findall to get all matches, adjusting for nested structure
    matches = re.findall(pattern, text)

    # Clean and combine the elements
    elements = []
    temp = ''
    for match in matches:
        # Continue appending to temp if it starts with an unmatched '('
        if temp.count('(') != temp.count(')'):
            temp += ',' + match
        else:
            if temp:
                elements.append(temp.strip())
            temp = match
    if temp:  # Append the last collected item
        elements.append(temp.strip())

    #remove special characters if they appear as single elements
    special_characters = ["(", ")", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "-", "+", "=", 
                          "|", "\\", "{", "}", "[", "]", ":", ";", '"', "'", "<", ">", ",", ".", "?", "/", "_"]
    
    elements = [item for item in elements if item not in special_characters]
    return elements

def extract_elements_with_cleaning(text):
    # Remove the '##Answer:' tag from some responses at the beginning
    text = text.replace("##Answer:", "").strip()

    # Regex pattern to correctly handle nested commas within parentheses
    # This pattern matches non-parenthetical text or text within balanced parentheses
    # Example: "a, b, (c, d), e" -> ['a', 'b', '(c, d)', 'e']
    pattern = r'\([^()]*\)|[^,]+'

    # Use findall to get all matches, adjusting for nested structure
    matches = re.findall(pattern, text)

    # Clean and combine the elements
    elements = []
    temp = ''
    for match in matches:
        # Continue appending to temp if it starts with an unmatched '('
        if temp.count('(') != temp.count(')'):
            temp += ',' + match
        else:
            if temp:
                elements.append(temp.strip())
            temp = match
    if temp:  # Append the last collected item
        elements.append(temp.strip())

    # Remove special characters if they appear as single elements
    special_characters = ["(", ")", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "-", "+", "=", 
                          "|", "\\", "{", "}", "[", "]", ":", ";", '"', "'", "<", ">", ",", ".", "?", "/", "_"]
    elements = [item for item in elements if item not in special_characters]

    # Remove duplicates while maintaining order
    seen = set()
    unique_list = []
    for item in elements:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)

    # Filter out items containing any banned keywords (case insensitive)
    banned_keywords = ['Continuous', 'Customized']
    processed_list = [item for item in unique_list if not any(banned_keyword.lower() in item.lower() for banned_keyword in banned_keywords)]

    return processed_list

def extract_elements_v2(s):
  """
  Extracts elements enclosed within backticks (`) from a string.

  Args:
    s: The input string.

  Returns:
    A list of elements enclosed within backticks.
  """
  pattern = r"`(.*?)`"
  elements = re.findall(pattern, s)
  return elements

def run_evaluation_with_gpt4o(system_message, question, openai_token):

    client = OpenAI(
        api_key=openai_token
    )

    response = client.chat.completions.create(
      model="gpt-4o",
      response_format = { "type": "json_object" },
      messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": question},
      ],
      seed = 42,
      temperature=0.0,
      stream=False,
      max_tokens=1000
    )
    return response.choices[0].message.content

def match_to_score(matched_pairs, remaining_reference_features, remaining_candidate_features):
    """
    Calculates precision, recall, and F1 score based on the given matched pairs and remaining features.

    Parameters:
    matched_pairs (list): A list of matched feature pairs.
    remaining_reference_features (list): A list of remaining reference features.
    remaining_candidate_features (list): A list of remaining candidate features.

    Returns:
    dict: A dictionary containing the precision, recall, and F1 score.
    """
    precision = len(matched_pairs) / (len(matched_pairs) + len(remaining_candidate_features)) # TP/(TP+FP)
    recall = len(matched_pairs) /  (len(matched_pairs) + len(remaining_reference_features)) #TP/(TP+FN)
    
    if precision == 0 or recall == 0:
        f1 = 0
    else:
        f1 = 2 * (precision * recall) / (precision + recall) # F1

    return {"precision": precision, "recall": recall, "f1": f1}
