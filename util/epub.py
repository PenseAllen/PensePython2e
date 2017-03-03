#!/usr/bin/env python3
from glob import glob
from shutil import rmtree
from subprocess import call
from os import path, makedirs

def _project_path():
    return path.dirname(path.dirname(path.abspath(__file__)))


def _get_path(p):
    return path.join(_project_path(), p)


def _fix_images_url(files, tmp_dir):
    """ Corrige as urls das imagens.
        Por algum motivo o pandoc não estava conseguindo baixar as imagens do site para embedar no epub.
        Com esse código eu utilizo gero arquivos temporários com as essas referências acertadas para a mesma imagem dentro do projeto.
    """
    makedirs(tmp_dir)
    fixed_files = []
    fixed_path = path.relpath(_project_path())
    for fp in files:
        file_name = path.split(fp)[1]
        output = path.join(tmp_dir, file_name)
        with open(fp) as input_file:
            fixed_str = input_file.read().replace('https://github.com/PenseAllen/PensePython2e/raw/master', fixed_path)
            with open(output, 'w') as output_file:
                output_file.write(fixed_str)
            fixed_files.append(output)
    return fixed_files



def main():
    glob_filter = _get_path('docs/*.md')
    capa = _get_path('img/Capa_PenseEmPython332x461-borda.png')
    metadata = _get_path('docs/metadata.xml')
    output = _get_path('docs/PenseEmPython.epub')
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
    call(args)
    # Remove arquivos temporários
    rmtree(tmp_dir)
    print('Gerado epub em', output)


if __name__ == '__main__':
    main()
