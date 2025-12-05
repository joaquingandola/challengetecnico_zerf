class Directorio:
    def __init__(self, nombre, padre = None):
        self.nombre = nombre
        self.padre = padre
        self.hijos = {} 
    
    def touch(self, nombre):
        if nombre not in self.hijos:  # asi se evitan los duplicados
            self.hijos[nombre] = Archivo(nombre, padre = self)
        return self.hijos[nombre]

    def mkdir(self, nombre):
        if nombre not in self.hijos:  # asi se evitan los duplicados
            self.hijos[nombre] = Directorio(nombre, padre = self)
        return self.hijos[nombre]
    
    def pwd(self):
        ruta = self.nombre
        actual = self.padre
        while actual:
            ruta = actual.nombre + '/' + ruta
            actual = actual.padre
        return '/' + ruta 
    
    def ls(self):
        return sorted(self.hijos.keys())
    
    def rm(self):
        nombres_hijos = list(self.hijos.keys())
        for nombre in nombres_hijos:
            hijo = self.hijos[nombre]
            hijo.rm()
        if self.padre:
            del self.padre.hijos[self.nombre]
            return True
        return False

class Archivo:
    def __init__(self, nombre, padre):
        self.nombre = nombre
        self.padre = padre

    def __str__(self):
        return self.nombre
    
    def rm(self):
        if self.padre:
            del self.padre.hijos[self.nombre]
            return True
        return False    
    

class FileSystem:
    def __init__(self):
        self.raiz = Directorio('raiz') # raiz es 'raiz' porque sino el pwd quedaria con doble barra al inicio
        self.cwd = self.raiz

    def cd(self, dir):
        if dir == '..':
            if self.cwd.padre:
                self.cwd = self.cwd.padre #si existe un directorio padre, "subo" a él
            else:
                print("Error: Ya estás en el directorio raíz")
            return
        
        if dir in self.cwd.hijos:
            hijo = self.cwd.hijos[dir]
            if isinstance(hijo, Directorio):
                self.cwd = hijo
            else:
                print(f"Error: {dir} no es un directorio")  # es un archivo
        else:
            print(f"Error: {dir} no existe")

    def touch(self, fileName):  # FS funciona como un facade
        return self.cwd.touch(fileName)
    
    def mkdir(self, dirName):
        return self.cwd.mkdir(dirName)
    
    def ls(self):
        return self.cwd.ls()
    
    def pwd(self):
        return self.cwd.pwd()

    def rm(self, path):
        nodo_a_eliminar = self._resolve_path(path)
        if nodo_a_eliminar == self.raiz:
            print("Error: No se puede borrar la raíz")
        else:
            if nodo_a_eliminar:
                nodo_a_eliminar.rm()
                if nodo_a_eliminar == self.cwd:
                    self.cwd = nodo_a_eliminar.padre
            else:
                print(f"Error: La ruta {path} no existe")

    def _resolve_path(self, path):
        if path.startswith('/'):
            actual = self.raiz
            partes = path.strip('/').split('/')
            if partes[0] == 'raiz':
                partes = partes[1:]
        else:
            actual = self.cwd
            partes = path.split('/')

        for parte in partes:
            if parte == '..':
                if actual.padre:
                    actual = actual.padre
            elif parte in actual.hijos:
                actual = actual.hijos[parte] #va buscando en los hijos
            else:
                return None
        return actual