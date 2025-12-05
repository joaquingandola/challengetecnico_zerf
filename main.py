from fs import FileSystem


def main():
    fileSystem = FileSystem()

    while True:
        comando = input(f'{fileSystem.pwd()} $ ').strip().split()
        if not comando:
            continue
        cmd = comando[0]
        args = comando[1:]

        if cmd == 'mkdir' and len(args) == 1:
            fileSystem.mkdir(args[0])
        elif cmd == 'touch' and len(args) == 1:
            fileSystem.touch(args[0])
        elif cmd == 'ls' and len(args) == 0:
            print(' '.join(fileSystem.ls()))
        elif cmd == 'cd' and len(args) == 1:
            fileSystem.cd(args[0])
        elif cmd == 'rm' and len(args) == 1:
            fileSystem.rm(args[0])
        elif cmd == 'pwd' and len(args) == 0:
            print(fileSystem.pwd())
        elif cmd == 'exit':
            break
        else:
            print('Comando no reconocido o argumentos incorrectos.')

if __name__ == '__main__':
    main()