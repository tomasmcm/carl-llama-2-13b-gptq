# pip3 install banana-dev

import banana_dev as client

# Create a reference to your model on Banana
my_model = client.Client(
    api_key="playgrou-nds1-4fc7-886c-d86d3772b1b6",
    model_key="0f524747-3edc-44d4-bd51-12cd6f54ef66",
    url="https://demo-dolphin-llama2-7b-gptq-ll5i1cajpl.run.banana.dev",
)

# Specify the model's input JSON, what you expect 
# to receive in your Potassium app. Here is an 
# example for a basic BERT model:
inputs = {
    "prompt": "Tell me about AI",
}

# Call your model's inference endpoint on Banana.
# If you have set up your Potassium app with a
# non-default endpoint, change the first 
# method argument ("/")to specify a 
# different route.
result, meta = my_model.call("/", inputs)

print(result)
