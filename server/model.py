import pickle
import os
from llama_index import GPTSimpleVectorIndex

os.environ['OPENAI_API_KEY'] = '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'

from llama_index import download_loader
download_loader("GithubRepositoryReader")

from llama_index.readers.llamahub_modules.github_repo import GithubClient, GithubRepositoryReader

docs = None
if os.path.exists("docs.pkl"):
    with open("docs.pkl", "rb") as f:
        docs = pickle.load(f)

if docs is None:
    github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
    loader = GithubRepositoryReader(
        github_client,
        owner =                  "ankorstore",
        repo =                   "ankorstore",
        filter_directories =     (["docs/external"], GithubRepositoryReader.FilterType.INCLUDE),
        filter_file_extensions = ([".md"], GithubRepositoryReader.FilterType.INCLUDE),
        verbose =                True,
        concurrent_requests =    10,
    )

    # docs_branch = loader.load_data(branch="develop")
    docs = loader.load_data(branch="develop")

    with open("docs.pkl", "wb") as f:
        pickle.dump(docs, f)

# index = GPTSimpleVectorIndex(docs)
# index.save_to_disk("index.json")

index = GPTSimpleVectorIndex.load_from_disk("index.json")

# function to query the index
def ask(query):
    # return index.query("How to create a test order on Ankorstore public API?")
    return "this is a dummy response"