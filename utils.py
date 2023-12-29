from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import DuckDuckGoSearchRun

def generate_script(prompt,video_length,creativity):
    
    # Template for generating 'Title'
    title_template = PromptTemplate(
        input_variables = ['subject'], 
        template='Come up with a title for a YouTube video on the  {subject}. make it interesting, catchy and with a hint of clickbait.'
        )

    # Template for generating 'Video Script' using DuckDuckGo search engine
    script_template = PromptTemplate(
        input_variables = ['title', 'duration', 'web_search_results'], 
        template='Create a script for a YouTube video based on this title: "{title}". The content should be of {duration} minutes. use the following search data: {web_search_results}'
    )

    #Setting up OpenAI LLM
    llm = ChatOpenAI(
        temperature=creativity,
        model_name='gpt-3.5-turbo'
    ) 
    
    #Creating chain for 'Title' & 'Video Script'
    title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
    script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)

    
    # https://python.langchain.com/docs/modules/agents/tools/integrations/ddg
    search = DuckDuckGoSearchRun()

    # Executing the chains we created for 'Title'
    title = title_chain.run(prompt)

    # Executing the chains we created for 'Video Script' by taking help of search engine 'DuckDuckGo'
    search_result = search.run(prompt) 
    script = script_chain.run(title=title, duration=video_length, web_search_results=search_result)

    # Returning the output
    return search_result, title, script

if __name__ == "__main__":
    search_result, title, script = generate_script(prompt="how to setup your camera for low light photography",video_length="5",creativity=0.2)
    print(search_result)
    print(title)
    print(script)
