import os
import subprocess  
import shutil
import argparse
from pwn import info, error, success

def parse_args():
    parser = argparse.ArgumentParser(description='Setup a challenge')
    parser.add_argument('-m', '--machine', type=str, help='machine image name (e.g. "ubuntu:22.04")')
    parser.add_argument('-b', '--bin_name', type=str, help='binary file name (e.g. "chal")')
    parser.add_argument('-p', '--port', type=int, help='port number (e.g. 1337)')
    parser.add_argument('-c', '--clean', action='store_true', help='clean the setup')
    return parser.parse_args()

def clean():
    pass_file_dict = ['template', 'setup.py', '.gitignore', 'README.md', 'requirements.txt', 'flag', 'flag.txt', 'LICENSE']
    pass_dir_dict = ['template', '.git', 'tmp']
    try:
        # traverse root directory, and list directories as dirs and files as files
        # do not go into pass_dir_dict
        for root, dirs, files in os.walk('.'):
            dirs[:] = [d for d in dirs if d not in pass_dir_dict]
            files[:] = [f for f in files if f not in pass_file_dict]
            for file in files:
                info('Removing file: ' + os.path.join(root, file))
                os.remove(os.path.join(root, file))
            for dir in dirs:
                info('Removing directory: ' + os.path.join(root, dir))
                shutil.rmtree(os.path.join(root, dir))
    except:
        pass
    info('Cleaned up all files and directories')

def setup(machine, bin_name, port):
    # SETUP directory structure
    os.makedirs('./bin', exist_ok=True)
    os.makedirs('./src', exist_ok=True)
    success('Created directories "./bin" and "./src"')
    info('Put the binary file to "./bin"')
    info('Put the flag file to "./bin" if needed')

    # SETUP xinetd
    xinetd_fd = open('./template/xinetd.template', 'r+')
    xinetd_content = xinetd_fd.read()
    xinetd_content = xinetd_content.replace('$PORT', str(port))
    xinetd_content = xinetd_content.replace('$BIN_NAME', bin_name)
    xinetd = open('./xinetd', 'w')
    xinetd.write(xinetd_content)
    xinetd_fd.close()
    success('Created "xinetd" file')

    # SETUP Dockerfile
    dockerfile_fd = open('./template/Dockerfile.template', 'r+')
    dockerfile_content = dockerfile_fd.read()
    dockerfile_content = dockerfile_content.replace('$MACHINE', machine)
    dockerfile = open('./Dockerfile', 'w')
    dockerfile.write(dockerfile_content)
    dockerfile_fd.close()
    success('Created "Dockerfile"')

    # SETUP start.sh
    start_fd = open('./template/start.sh.template', 'r+')
    start_content = start_fd.read()
    start = open('./start.sh', 'w')
    start.write(start_content)
    start_fd.close()
    success('Created "start.sh"')

    info('Setup completed')
    info('To build the image, run "docker build -t <image_name> ."')


def main():
    argv = parse_args()

    if argv.clean:
        clean()
        return

    if argv.machine is None or argv.bin_name is None or argv.port is None:
        info('Please provide all the required arguments, use -h for help')
        return

    setup(argv.machine, argv.bin_name, argv.port)

if __name__=='__main__':
    main()