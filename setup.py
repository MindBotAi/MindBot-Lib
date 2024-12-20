from setuptools import setup, find_packages

setup(
    name="mindbotai",  # Name of your library
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "google-generativeai",  # Google Gemini library dependency
    ],
    description="MindBot AI: A library for Ai integerations",
    author="Ahmed Helmy Ali",
    author_email="ahmedhelmyali.dev@gmail.com",
    url="https://github.com/MindBotAi",  # Replace with your GitHub URL
)
