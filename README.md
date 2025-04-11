* All relevant scripts :
    1. The entire workflow can be found in finalWorkflow.ipynb
    2. the unit tests for CVs, JD, flagging and questionnaire can be found in step_2.ipynb
    
* Create a .env file in the root folder to include openAI_api_key and API_KEY(Deepseek)

# *Folder Structure*

## sample CVs

contains all sample CVs generated by GPT saved as pdf

## Affinda parsed CVs

contains all sample CVs parsed through Affinda resume parser(legacy) and stored as json

## gpt parsed CVs

contains all sample CVs parsed through openAI api (GPT-4) and stored as json 
 
## gpt enriched CVs

contains test results for enrichment parameters using DeepSeek(DeepSeek-chat) and openAI(o3-mini) on gpt parsed CVs stored as json

## JD_pdfs

contains all sample JDs generated by GPT saved as pdf

## JD_parsed

contains all sample JDs parsed through openAI api (GPT-4) and stored as json 

## JD_enriched

contains test results for enrichment parameters using openAI(GPT-4) on gpt parsed JDs stored as json

## flagging_output

contains key information extracted for Daniel Carter's CV and CLO JD:
1. overview of candidate
2. potential missing info from `enriched CV`
3. potential missing info from `enriched CV`, given an `enriched JD`
   
## questionnaire

contains a questionnaire for the sales team based on `flagging`, `enriched CV` and `enriched JD`

