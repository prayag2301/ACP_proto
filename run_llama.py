import torch
from transformers import LlamaForCausalLM, LlamaTokenizer

# Path to your downloaded LLaMA model and tokenizer
model_path = "/Users/prayagsharma/.llama/checkpoints/Llama3.2-1B-Instruct-int4-qlora-eo8"

# Load the tokenizer
tokenizer = LlamaTokenizer.from_pretrained(model_path)

# Load the model
model = LlamaForCausalLM.from_pretrained(model_path)

# Move the model to the M1 GPU (MPS backend) or CPU
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model.to(device)

# Encode the input text
input_text = "Once upon a time"
input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)

# Generate text
with torch.no_grad():
    output_ids = model.generate(input_ids, max_length=50)

# Decode the output text
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(output_text)