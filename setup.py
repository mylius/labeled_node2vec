from distutils.core import setup

setup(
    name='labeled_node2vec',
    packages=['labeled_node2vec'],
    version='0.4.3',
    description='Implementation of the node2vec algorithm. Allowing using labeles instead of nodes.',
    author='Jan-Gabriel Mylius & Elior Cohen',
    author_email='mylius@posteo.de',
    license='MIT',
    url='https://github.com/mylius/labeled_node2vec',
    install_requires=[
        'networkx',
        'gensim',
        'numpy',
        'tqdm',
        'joblib>=0.13.2'
    ],
    keywords=['machine learning', 'embeddings'],
)
