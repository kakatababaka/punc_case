from distutils.core import setup

setup(
    name="sbert_punc_case_ru",
    version="0.2",
    description="Punctuation and Case Restoration model based on https://huggingface.co/sberbank-ai/sbert_large_nlu_ru",
    author="Almira Murtazina",
    author_email="ar.murtazina@skbkontur.ru",
    packages=["sbert_punc_case_ru"],
    install_requires=[
        "transformers>=4.36.2",
        "torch",
        "numpy"
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
