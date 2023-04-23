import csv
import midjourney

# Read the prompts from the CSV file
with open("prompts.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    prompts = [row[0] for row in reader]

# Create a Midjourney client
client = midjourney.Client()

# Generate images from the prompts
for prompt in prompts:
    try:
        image = client.generate(prompt)
        print("Generated image:", image.name)
    except midjourney.errors.NoPromptError:
        print("Warning: No prompt provided for prompt '{}'".format(prompt))

