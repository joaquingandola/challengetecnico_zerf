import unittest
from fs import FileSystem, Directorio, Archivo

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.assertEqual(self.fs.pwd(), '/raiz')
    
    def test_mkdir_touch_ls(self):
        self.fs.mkdir('dir1')
        self.fs.mkdir('dir2')
        self.fs.touch('file1.txt')
        self.assertEqual(self.fs.ls(), ['dir1', 'dir2', 'file1.txt'])

    def test_cd(self):
        self.fs.mkdir('dir1')
        self.fs.cd('dir1')
        self.assertEqual(self.fs.pwd(), '/raiz/dir1')
        self.fs.cd('..')
        self.assertEqual(self.fs.pwd(), '/raiz')
        self.fs.cd('dir6') # dir6 no existe
        self.assertEqual(self.fs.pwd(), '/raiz')
        self.fs.cd('dir1')
        self.fs.touch('file.txt')
        self.assertEqual(self.fs.ls(), ['file.txt'])

    def test_rm(self):
        self.fs.touch('file1.txt')
        self.fs.rm('file1.txt')
        self.assertEqual(self.fs.ls(), [])
    
    def test_rm_directory(self):
        self.fs.mkdir('dir1')
        self.fs.mkdir('dir2')
        self.fs.cd('dir1')
        self.fs.touch('arch.txt')
        self.fs.cd('..')
        self.fs.rm('dir1')
        self.assertEqual(self.fs.ls(), ['dir2'])
    
    def test_rm_raiz(self):
        self.fs.rm('raiz')  # Intento de borrar la raíz
        self.assertEqual(self.fs.pwd(), '/raiz')  # Debe seguir en la raíz
    
    def test_rm_cwd_desplazo_alpadre(self):
        self.fs.mkdir('dir1')
        self.fs.cd('dir1')
        self.fs.rm('../dir1')
        self.assertEqual(self.fs.pwd(), '/raiz')  # Debe volver al padre

if __name__ == '__main__':
    unittest.main()