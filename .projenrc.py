from projen.python import PythonProject, VenvOptions, PoetryPyprojectOptionsWithoutDeps 


AUTHORS = [
    "Jacob Petterle",
]
project = PythonProject(
    author_email="jacobpetterle@tai-tutor.team",
    author_name=AUTHORS[0],
    module_name="llm_cdk_app_agent",
    name="llm-cdk-app-agent",
    version="0.1.0",
    poetry=True,
    description="A CDK app for deploying the LLM agent",
)

project.synth()