from projen.python import PythonProject


AUTHORS = [
    "Jacob Petterle",
]
project = PythonProject(
    author_email="jacobpetterle@tai-tutor.team",
    author_name=AUTHORS[0],
    module_name="llm_cdk_app_agent",
    name="llm-cdk-app-agent",
    version="0.1.0",
    description="A CDK app for deploying the LLM agent",
    poetry=True,
    deps=["pinecone-client", "openai"],
)


project.synth()
