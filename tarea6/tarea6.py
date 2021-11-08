class nodoArbol:
  def __init__( self, value, left=None, right=None):
    self.data = value
    self.left = left
    self.right = right

class arbolBB:
  def __init__(self):
    self.__root = None

  def insert(self, value):
    if self.__root == None:
      self.__root = nodoArbol(value)
    else:
      self.__insert_nodo__(self.__root, value)

  def __insert_nodo__(self, nodo, value):
    if nodo.data == value:
      print("ya existe")
      pass
    elif value < nodo.data:
      if nodo.left == None:
        nodo.left = nodoArbol(value)
      else:
        self.__insert_nodo__(nodo.left, value)
    else:
      if nodo.right == None:
        nodo.right = nodoArbol(value)
      else:
        self.__insert_nodo__(nodo.right, value)

  def transversal(self, formato = "inorden"):
    if formato == "inorden":
      self.recorrido_in(self.__root)
      print("recorrido in")
    elif formato == "preorden":
      self.recorrido_pre(self.__root)
      print("recorrido pre")
    else: #Post
      self.recorrido_pos(self.__root)
      print("recorrido pos")

  def recorrido_in(self, nodo):
    if nodo != None:
      self.recorrido_in(nodo.left)
      print(nodo.data, end="  ")
      self.recorrido_in(nodo.right)

  def recorrido_pre(self, nodo):
    if nodo != None:
      print(nodo.data, end="  ")
      self.recorrido_pre(nodo.left)
      self.recorrido_pre(nodo.right)

  def recorrido_pos(self, nodo):
    if nodo != None:
      self.recorrido_pos(nodo.left)
      self.recorrido_pos(nodo.right)
      print(nodo.data, end="  ")


  def buscar(self, value):
    if self.__root == None:
      print("Arbol vacio")
      return None
    else:
      return self.busca_nodo(self.__root, value)

  def busca_nodo(self, nodo, value):
    if nodo == None:
      print("no existe")
      return "no existe el valor"
    elif nodo.data == value:
      print("Encontrado", nodo.data)
      return nodo.data
    elif value < nodo.data:
      #print("Buscar del lado izquierdo")
      return self.busca_nodo(nodo.left, value)
    else:
      #print("buscar del lado derecho")
      return self.busca_nodo(nodo.right, value)

  def eliminar(self , value):
      if self.__root == None:
          print("Nada que eliminar")
      else:
          self.eliminar_nodo( None, None, self.__root, value)

  def eliminar_nodo(self, padre_hi, padre_hd, actual, value):
      if actual == None:
          print("no hay arbol")
          return None
      elif actual.data == value:
          if actual.left == None and actual.right == None:
              if padre_hi != None:
                  padre_hi.left = None
              else:
                  padre_hd.right = None
          if (actual.left != None and actual.right == None) or (actual.left == None and actual.right != None):
              if actual.left != None:
                  actual.data = actual.left.data
                  actual.left = None
              else:
                  actual.data = actual.right.data
                  actual.right = None
          if (actual.left != None and actual.right != None):
              actual.data = actual.left.data
              actual.left = None
      elif value < actual.data:
          self.eliminar_nodo(actual, None, actual.left, value)
      else:
          self.eliminar_nodo(None, actual, actual.right, value)


abb = arbolBB()

abb.insert(6)
abb.insert(8)
abb.insert(3)
abb.insert(2)
abb.insert(5)
abb.insert(7)
abb.insert(10)
print("antes de eliminar")
abb.transversal("preorden")
abb.eliminar(3)
print("con el numero eliminado")
abb.transversal("preorden")
abb.insert(3)
print("agregando el mismo numero y se acomoda en una posicion diferente")
abb.transversal("preorden")
