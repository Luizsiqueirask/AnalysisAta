import glob, os
import shutil
import sys
import time


def check_directory_exists(directory: str):
    path = "./"
    if not os.path.exists(directory):
        os.mkdir(directory)
        os.chdir(path)
        for directories in glob.glob("*"):
            print(directories)
        sys.exit()
    else:
        print(directory)
        sys.exit()


def create_folder_with_filename():
    # check_directory_exists(directory)

    os.chdir("./PROBLEMAS")
    for idx, pdf in enumerate(glob.glob("*.pdf")):
        if os.path.exists(f"../_PDFs_/{pdf.replace(pdf[-4::], '')}"):
            print(f"{idx} - Diretorio Criado -> {pdf.replace(pdf[-4::], '')}")
        else:
            os.mkdir(f"../_PDFs_/{pdf.replace(pdf[-4::], '')}".replace(pdf[-4::], ""))
            print(f"{idx} - Criando diretório -> {pdf.replace(pdf[-4::], '')}")

    for idx, pdf in enumerate(glob.glob("*.pdf")):
        print(f"{idx} - {pdf}")

'''
def move_file_to_directory():
    source = []
    destiny = []
    os.chdir("./PROBLEMAS")
    source.append([directoryA for directoryA in glob.glob('*.pdf')])

    os.chdir("../_PDFs_")
    destiny.append([directoryB for directoryB in glob.glob('*')])

    # print(f'\t\n{source} \t\n{destiny}')

    def move_data(s: list, d: list):
        print(f'\t\n{s} \t\n{d}')

        def d():
            pass
    move_data(source, destiny)
'''


def move_file_to_directory():
    # source = []
    # destiny = []

    os.chdir("./PROBLEMAS")
    for source in glob.glob('*.pdf'):
        os.chdir("../_PDFs_")
        for destiny in glob.glob('*'):
            if source[0:35] == destiny[0:35]:
                print(f'\n\t{source} \t{destiny}')
                shutil.copy2(f"../PROBLEMAS/{source}", f"../_PDFs_/{destiny}/{destiny}{'.pdf'}")
                # os.rename(f"../_PDFs_/{source}", f"../_PDFs_/{source}.pdf")


'''if __name__ == "__main__":
    directory = "_PDFs_"
    # check_directory_exists(directory)
    # create_folder_with_filename()
    move_file_to_directory()

''os.mkdir(directory)
os.chdir(f"{path}/{directory}")

for file in glob.glob(file):
    os.mkdir(file)
    print(file)''
'''