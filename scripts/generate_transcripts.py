from local_llm import Llama

def generate_transcript(data):
    """
    Generate a two-person conversational transcript from data.
    """
    model = Llama()
    prompt = "Create a dialogue based on the following content:\n" + data
    transcript = model.generate(prompt)
    return transcript
