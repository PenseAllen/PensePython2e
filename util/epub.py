#!/usr/bin/env python3

from glob import glob
import shutil
import subprocess
import os


URL_REPO = 'https://github.com/PenseAllen/PensePython2e/raw/master'


def _project_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _get_path(p):
    return os.path.join(_project_path(), p)


def _fix_images_url(files, tmp_dir):
    """ Corrige as urls das imagens.
        Por algum motivo o pandoc não estava conseguindo baixar as imagens
        do site para embedar no epub. Com esse código eu gero arquivos 
        temporários com as essas referências acertadas para a mesma imagem
        dentro do projeto.
    """
    os.makedirs(tmp_dir)
    fixed_files = []
    fixed_path = os.path.relpath(_project_path())
    for fp in files:
        file_name = os.path.split(fp)[1]
        output = os.path.join(tmp_dir, file_name)
        with open(fp) as input_file:
            fixed_str = input_file.read().replace(URL_REPO, fixed_path)
            with open(output, 'w') as output_file:
                output_file.write(fixed_str)
            fixed_files.append(output)
    return fixed_files


def main():
    glob_filter = _get_path('docs/*.md')
    capa = _get_path('img/Capa_PenseEmPython332x461-borda.png')
    metadata = _get_path('ebooks/metadata.xml')
    output = _get_path('ebooks/PenseEmPython2e.epub')
    files = glob(glob_filter)
    files.sort()
    files.pop()
    tmp_dir = _get_path('tmp')
    files = _fix_images_url(files, tmp_dir)
    # Monta os argumentos do pandoc
    args = ['pandoc', '--epub-cover-image=' + capa, '--epub-metadata=' + metadata]
    args.extend(files)
    args.append('-o')
    args.append(output)
    # Executa o pandoc
    subprocess.call(args)
    # Remove arquivos temporários
    shutil.rmtree(tmp_dir)
    print('Gerado epub em', output)


if __name__ == '__main__':
    main()
