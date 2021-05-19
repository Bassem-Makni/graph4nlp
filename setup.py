from setuptools import setup, find_packages


# def get_cuda_version():
#     import os
#     nvsmi = os.popen('nvidia-smi')
#     gpu_info_str = nvsmi.read()
#     if gpu_info_str == '':
#         return ''
#     else:
#         cuda_version_prompt = 'CUDA Version: '
#         version_number_start = gpu_info_str.find(cuda_version_prompt) + len(cuda_version_prompt)
#         version_number = gpu_info_str[version_number_start:].split(' ')[0]
#         return '-cu{}'.format(version_number.replace('.', ''))
#         # install_requirement.append('dgl-cuda{} >= 0.4'.format(version_number))

cuda_versions = {
    '1': '9.2',
    '2': '10.1',
    '3': '10.2',
    '4': '11.0',
    '5': 'cpu'
}

if __name__ == '__main__':

    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--cuda_version', type=str, default='cpu')
    # args, unknown = parser.parse_known_args()
    # args = vars(args)
    # cuda_version = args.get('cuda_version')
    try:
        with open('config', 'r') as f:
            version = f.readlines()[0].strip()
    except:
        raise FileNotFoundError('config file not found. Please run ./configure first.')

    cuda_version = cuda_versions[version]

    if cuda_version == 'none':
        cuda_version = ''
    elif cuda_version.find('.') != -1:
        cuda_version = '-cu' + ''.join(cuda_version.split('.'))
    else:
        cuda_version = ''

    install_requirement = ['torch >= 1.8.1', 'pythonds', 'nltk >= 3.5', 'stanfordcorenlp', 'scipy >= 1.5.2',
                           'scikit-learn >= 0.23.2', 'networkx >= 2.5', 'dgl{} >= 0.4'.format(cuda_version),
                           'ogb', 'torchtext']
    setup(
        name='graph4nlp{}'.format(cuda_version),
        version='0.2a02',
        description='A DGL and PyTorch based graph deep learning library for natural language processing',
        author='Graph4NLP Team',
        license='MIT',
        packages=find_packages('.', exclude=(
        "examples.*", "examples", "graph4nlp.pytorch.test.*", "graph4nlp.pytorch.test")),
        install_requires=install_requirement,
    )