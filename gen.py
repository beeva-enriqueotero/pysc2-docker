import os

basedockers = [
    'tensorflow/tensorflow:1.3.0-devel-gpu-py3',
    'tensorflow/tensorflow:1.3.0-devel-gpu',
    'tensorflow/tensorflow:1.3.0-devel-py3',
    'tensorflow/tensorflow:1.3.0-devel',
]


if __name__ == '__main__':
    with open('Dockerfile.base', 'r') as f:
        basecontent = f.read()

    for base in basedockers:
        print('processing %s' % base)
        if not os.path.exists('./' + base):
            os.makedirs('./' + base)
        content = basecontent.replace('{{BASEDOCKER}}', base)
        with open('./' + base + '/Dockerfile', 'w') as f:
            f.write(content)

    print('done')

